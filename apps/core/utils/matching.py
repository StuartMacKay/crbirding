"""Working out which bird an Observation is of, from its Tags.

Two ways, for two different questions:

- Is it a bird that's already been identified? Colour marks don't
  change, so an Observation whose every Position has exactly the same
  code as one already linked to an Origin -- same species too -- is the
  same bird, and is linked automatically (link_same_bird,
  link_to_known_bird). Codes that differ only in "?" -- one observer
  unsure of a ring another read clearly -- are probably the same bird,
  but that's for a person to decide, so they're only offered up for
  review (possible_sightings).

- Which project marked it? Matched against each project's Rules, one
  Position's code at a time (find_candidate_projects).
"""

import re
from dataclasses import dataclass

from ..models import Observation, Observer, Origin, Project, Rule
from .codes import match_code
from .events import record_origin_linked


def exact_signature(tags) -> frozenset:
    """Every (position, code) -- exactly as read, "?" included."""
    return frozenset((tag.position, tag.code) for tag in tags)


def loose_signature(tags) -> frozenset:
    """Every (position, code) with "?" left out."""
    return frozenset((tag.position, match_code(tag.code)) for tag in tags)


def _open_observations(species: str):
    return Observation.objects.filter(species=species, origin__isnull=True).prefetch_related("tags")


def link_same_bird(observation: Observation) -> list[Observation]:
    """Link every Open observation of the same species with exactly the
    same tags as `observation` (itself already linked) to its Origin --
    other sightings of the same bird. Returns those linked.
    """
    signature = exact_signature(observation.tags.all())
    if not signature or observation.origin_id is None:
        return []

    linked = []
    for other in _open_observations(observation.species).exclude(pk=observation.pk):
        if exact_signature(other.tags.all()) == signature:
            other.origin = observation.origin
            other.save(update_fields=["origin"])
            record_origin_linked(other, "Linked: same tags as another sighting")
            linked.append(other)
    return linked


def link_to_known_bird(observation: Observation) -> Origin | None:
    """Link an Open `observation` to the Origin of an already-identified
    sighting with exactly the same tags and species, if there's one such
    Origin -- e.g. a new sighting of a bird whose ringing details are
    already known. Returns the Origin linked to, or None.
    """
    signature = exact_signature(observation.tags.all())
    if not signature or observation.origin_id is not None:
        return None

    identified = (
        Observation.objects.filter(species=observation.species, origin__isnull=False)
        .exclude(pk=observation.pk)
        .select_related("origin__project")
        .prefetch_related("tags")
    )
    origins = {
        other.origin for other in identified if exact_signature(other.tags.all()) == signature
    }
    if len(origins) != 1:
        return None

    observation.origin = origins.pop()
    observation.save(update_fields=["origin"])
    record_origin_linked(observation, "Linked: same tags as another sighting")
    return observation.origin


@dataclass
class Difference:
    position: str
    code: str
    linked_code: str


@dataclass
class PossibleSighting:
    observation: Observation
    differences: list[Difference]


def possible_sightings(origin: Origin) -> list[PossibleSighting]:
    """Open observations that might be `origin`'s bird: same species,
    and the same tags as one of its sightings once "?" is ignored. Each
    comes with the positions whose codes differ as read, for a person to
    review before linking it (see core.views.observation.LinkObservationView).
    """
    linked = list(origin.observations.prefetch_related("tags"))
    if not linked:
        return []
    by_signature = {loose_signature(obs.tags.all()): obs for obs in linked}
    by_signature.pop(frozenset(), None)

    found = []
    for candidate in _open_observations(origin.species).order_by("date", "pk"):
        match = by_signature.get(loose_signature(candidate.tags.all()))
        if match is None:
            continue
        linked_codes = {tag.position: tag.code for tag in match.tags.all()}
        differences = [
            Difference(tag.position, tag.code, linked_codes[tag.position])
            for tag in candidate.tags.all()
            if tag.code != linked_codes[tag.position]
        ]
        found.append(PossibleSighting(candidate, differences))
    return found


def find_candidate_projects(observation: Observation) -> list[Project]:
    """Projects with a Rule matching one of this Observation's Tags --
    a best guess at who to send it to while it isn't yet linked to its
    Origin.

    A Rule is matched against one Position's whole code -- every ring,
    flag, etc. there, top to bottom -- with "?" left out (see
    match_code): being unsure of a reading doesn't change which project
    a scheme belongs to. Rules aren't loosened to allow for a partly-read stack; a
    project that wants a partial read to still narrow things down adds
    a Rule for that partial code too.

    Species-scoped (Rule has its own `species` field), unlike the bird
    matching above -- a Rule is an administrator's deliberate claim
    about one project's scheme. Rules are shared data, not owned by any
    one user (see core.models.Rule), so every Rule is a candidate here.
    """
    rules = list(Rule.objects.filter(species=observation.species).select_related("project"))

    projects = {}
    for tag in observation.tags.all():
        code = match_code(tag.code)
        for rule in rules:
            if rule.position != tag.position:
                continue
            try:
                matched = re.search(rule.regex, code)
            except re.error:
                # A Rule's regex is free text an administrator can get
                # wrong; one bad pattern shouldn't break matching for
                # every other rule.
                continue
            if matched:
                projects[rule.project_id] = rule.project
    return list(projects.values())


def find_claimable_observer(name: str) -> Observer | None:
    """The one unclaimed Observer named `name` (case-insensitively), if
    there's exactly one -- used to offer "is this you?" before linking a
    new user account to an existing, historical Observer record (see
    apps.users.views.ObserverSetupView and
    core.views.observation.SubmitObservationView._observer_for).

    Restricted to Observer.user__isnull=True: an Observer already linked
    to someone else's account is never offered up for claiming, even if
    the name happens to match -- two people can coincidentally share a
    display name without it being a conflict. Zero or more than one
    unclaimed match both return None deliberately -- "don't guess" is the
    same rule core.utils.bulk_import's own name matching follows, just
    without the hard error, since here a person is present to just
    create a new Observer instead.
    """
    matches = list(Observer.objects.filter(name__iexact=name, user__isnull=True))
    return matches[0] if len(matches) == 1 else None
