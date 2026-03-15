import pytest

from core.models import Event, Position, Species
from core.utils.matching import (
    exact_signature,
    find_candidate_projects,
    find_claimable_observer,
    link_same_bird,
    link_to_known_bird,
    loose_signature,
    possible_sightings,
)

from .factories import (
    ObservationFactory,
    ObserverFactory,
    OriginFactory,
    RuleFactory,
    TagFactory,
    UserFactory,
)

LA, LB, RA = Position.LEFT_ABOVE, Position.LEFT_BELOW, Position.RIGHT_ABOVE


def _observation(codes: dict, **kwargs):
    """An Observation with a Tag per {position: code}."""
    observation = ObservationFactory(**kwargs)
    for position, code in codes.items():
        TagFactory(observation=observation, position=position, code=code)
    return observation


class TestSignatures:
    def test_exact_includes_uncertainty(self):
        a = [TagFactory.build(position=LA, code="R,WN(KY)")]
        b = [TagFactory.build(position=LA, code="R?,WN(KY)")]
        assert exact_signature(a) != exact_signature(b)

    def test_loose_ignores_uncertainty(self):
        a = [TagFactory.build(position=LA, code="R,WN(KY)")]
        b = [TagFactory.build(position=LA, code="R?,WN(KY)?")]
        assert loose_signature(a) == loose_signature(b)

    def test_position_matters(self):
        a = [TagFactory.build(position=LA, code="Y")]
        b = [TagFactory.build(position=LB, code="Y")]
        assert exact_signature(a) != exact_signature(b)

    def test_order_of_tags_does_not(self):
        a = [TagFactory.build(position=LA, code="Y"), TagFactory.build(position=RA, code="M")]
        assert exact_signature(a) == exact_signature(list(reversed(a)))


@pytest.mark.django_db
class TestLinkSameBird:
    def test_links_open_sightings_with_exactly_the_same_tags(self):
        origin = OriginFactory()
        linked = _observation({LA: "R,WN(KY)", RA: "M"}, origin=origin)
        same = _observation({LA: "R,WN(KY)", RA: "M"}, origin=None)

        assert link_same_bird(linked) == [same]

        same.refresh_from_db()
        assert same.origin == origin
        assert same.events.get().description.startswith("Linked: same tags as another sighting")

    @pytest.mark.parametrize(
        "codes",
        [
            {LA: "R,WN(KY)?", RA: "M"},  # uncertain
            {LA: "R,WN(KY)"},  # a position missing
            {LA: "R,WN(KY)", RA: "M", LB: "Y"},  # an extra position
        ],
    )
    def test_anything_less_than_exact_is_left_for_review(self, codes):
        linked = _observation({LA: "R,WN(KY)", RA: "M"}, origin=OriginFactory())
        other = _observation(codes, origin=None)

        assert link_same_bird(linked) == []
        other.refresh_from_db()
        assert other.origin is None

    def test_other_species_are_left_alone(self):
        linked = _observation({LA: "Y"}, origin=OriginFactory(), species=Species.COMMON_OSTRICH)
        other = _observation({LA: "Y"}, origin=None, species=Species.RED_THROATED_LOON)

        assert link_same_bird(linked) == []
        other.refresh_from_db()
        assert other.origin is None

    def test_already_linked_sightings_are_left_alone(self):
        linked = _observation({LA: "Y"}, origin=OriginFactory())
        elsewhere = OriginFactory()
        other = _observation({LA: "Y"}, origin=elsewhere)

        assert link_same_bird(linked) == []
        other.refresh_from_db()
        assert other.origin == elsewhere

    def test_a_sighting_with_no_tags_links_nothing(self):
        linked = _observation({}, origin=OriginFactory())
        _observation({}, origin=None)
        assert link_same_bird(linked) == []


@pytest.mark.django_db
class TestLinkToKnownBird:
    def test_links_to_the_origin_of_an_identical_identified_sighting(self):
        origin = OriginFactory()
        _observation({LA: "R,WN(KY)"}, origin=origin)
        new = _observation({LA: "R,WN(KY)"}, origin=None)

        assert link_to_known_bird(new) == origin
        new.refresh_from_db()
        assert new.origin == origin
        assert new.events.count() == 1

    def test_near_matches_are_not_linked(self):
        _observation({LA: "R,WN(KY)"}, origin=OriginFactory())
        new = _observation({LA: "R?,WN(KY)"}, origin=None)

        assert link_to_known_bird(new) is None

    def test_ambiguous_matches_are_not_linked(self):
        """Two different birds recorded with the same tags -- don't
        guess which one this is."""
        _observation({LA: "Y"}, origin=OriginFactory())
        _observation({LA: "Y"}, origin=OriginFactory())
        new = _observation({LA: "Y"}, origin=None)

        assert link_to_known_bird(new) is None
        assert not Event.objects.filter(observation=new).exists()

    def test_leaves_an_already_linked_observation_alone(self):
        _observation({LA: "Y"}, origin=OriginFactory())
        mine = OriginFactory()
        observation = _observation({LA: "Y"}, origin=mine)

        assert link_to_known_bird(observation) is None
        observation.refresh_from_db()
        assert observation.origin == mine


@pytest.mark.django_db
class TestPossibleSightings:
    def test_offers_near_matches_with_their_differences(self):
        origin = OriginFactory()
        _observation({LA: "R,WN(KY)", RA: "M"}, origin=origin)
        candidate = _observation({LA: "R?,WN(KY)", RA: "M"}, origin=None)

        [possible] = possible_sightings(origin)

        assert possible.observation == candidate
        assert [(d.position, d.code, d.linked_code) for d in possible.differences] == [
            (LA, "R?,WN(KY)", "R,WN(KY)")
        ]

    def test_exact_matches_are_offered_with_no_differences(self):
        """e.g. recorded before the Origin existed, and not re-saved since."""
        origin = OriginFactory()
        _observation({LA: "Y"}, origin=origin)
        candidate = _observation({LA: "Y"}, origin=None)

        [possible] = possible_sightings(origin)
        assert possible.observation == candidate
        assert possible.differences == []

    def test_ignores_different_birds_and_species(self):
        origin = OriginFactory(species=Species.COMMON_OSTRICH)
        _observation({LA: "WN(KY)"}, origin=origin, species=Species.COMMON_OSTRICH)
        _observation({LA: "WN(KX)"}, origin=None, species=Species.COMMON_OSTRICH)
        _observation({LA: "WN(KY)"}, origin=None, species=Species.RED_THROATED_LOON)

        assert possible_sightings(origin) == []

    def test_matches_any_of_the_birds_sightings(self):
        origin = OriginFactory()
        _observation({LA: "WN(KY)"}, origin=origin)
        _observation({LA: "WN(KY)", RA: "M"}, origin=origin)
        candidate = _observation({LA: "WN(KY)", RA: "M?"}, origin=None)

        assert [p.observation for p in possible_sightings(origin)] == [candidate]

    def test_nothing_without_linked_sightings_or_tags(self):
        origin = OriginFactory()
        assert possible_sightings(origin) == []
        _observation({}, origin=origin)
        _observation({}, origin=None)
        assert possible_sightings(origin) == []


@pytest.mark.django_db
class TestFindCandidateProjects:
    def test_matches_a_rule_against_the_whole_stack_at_a_position(self):
        rule = RuleFactory(position=LA, regex=r"^R,WN\([A-Z]{2}\)$")
        observation = _observation({LA: "R,WN(KY)"}, species=rule.species)

        assert find_candidate_projects(observation) == [rule.project]

    def test_uncertainty_is_ignored(self):
        rule = RuleFactory(position=LA, regex=r"^R,WN\(KY\)$")
        observation = _observation({LA: "R?,WN(KY)"}, species=rule.species)

        assert find_candidate_projects(observation) == [rule.project]

    def test_a_partial_read_needs_its_own_rule(self):
        """Rules aren't loosened for a partly-read stack -- only the
        red ring above was missed here, but the full-stack rule still
        doesn't match; a project adds a rule for the partial code."""
        full = RuleFactory(position=LA, regex=r"^R,WN\([A-Z]{2}\)$")
        observation = _observation({LA: "WN(KY)"}, species=full.species)
        assert find_candidate_projects(observation) == []

        partial = RuleFactory(position=LA, regex=r"^WN\([A-Z]{2}\)$", project=full.project)
        assert find_candidate_projects(observation) == [partial.project]

    def test_no_match_when_species_differs(self):
        RuleFactory(position=LA, regex="W")
        observation = _observation({LA: "W"}, species=Species.RED_THROATED_LOON)
        assert find_candidate_projects(observation) == []

    def test_no_match_when_position_differs(self):
        rule = RuleFactory(position=LA, regex="W")
        observation = _observation({RA: "W"}, species=rule.species)
        assert find_candidate_projects(observation) == []

    def test_each_project_once_however_many_rules_match(self):
        rule = RuleFactory(position=LA, regex="W")
        RuleFactory(position=RA, regex="W", project=rule.project)
        observation = _observation({LA: "W", RA: "W"}, species=rule.species)
        assert find_candidate_projects(observation) == [rule.project]

    def test_rules_are_shared_regardless_of_observation_owner(self):
        """Rules are shared reference data, not owned by any one user
        (see core.models.Rule)."""
        rule = RuleFactory(position=LA, regex="W")
        observation = _observation({LA: "W"}, species=rule.species, owner=None)
        assert find_candidate_projects(observation) == [rule.project]

    def test_an_invalid_regex_is_skipped_rather_than_raising(self):
        RuleFactory(position=LA, regex="[unclosed")
        observation = _observation({LA: "W"})
        assert find_candidate_projects(observation) == []

    def test_an_origin_linked_observation_still_matches_rules_directly(self):
        """Deciding when the known Origin wins over a rule-based guess is
        the caller's job (see ObservationDetailView)."""
        rule = RuleFactory(position=LA, regex="W")
        observation = _observation({LA: "W"}, species=rule.species, origin=OriginFactory())
        assert find_candidate_projects(observation) == [rule.project]


@pytest.mark.django_db
class TestFindClaimableObserver:
    def test_single_unclaimed_match(self):
        observer = ObserverFactory(name="Jo Smith", user=None)
        assert find_claimable_observer("Jo Smith") == observer

    def test_match_is_case_insensitive(self):
        observer = ObserverFactory(name="Jo Smith", user=None)
        assert find_claimable_observer("jo smith") == observer

    def test_no_match_returns_none(self):
        assert find_claimable_observer("Nobody Real") is None

    def test_ambiguous_match_returns_none(self):
        ObserverFactory(name="Jo Smith", user=None)
        ObserverFactory(name="Jo Smith", user=None)
        assert find_claimable_observer("Jo Smith") is None

    def test_already_claimed_observer_is_not_offered(self):
        ObserverFactory(name="Jo Smith", user=UserFactory())
        assert find_claimable_observer("Jo Smith") is None
