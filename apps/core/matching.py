"""Linking a Resighting back to the Capture where the bird was ringed,
by comparing their tags structurally.

Colour rings don't change, so if a Capture and a Resighting describe
the exact same set of tags, they're almost certainly the same bird.
This only works because Tag is structured data (position, colour,
inscription as real fields) rather than an opaque encoded string --
see apps.core.models.Tag.
"""

from .models import Resighting

# inscription_direction is how ambiguous text is read, not part of the
# bird's identity; uncertain tags are excluded from matching entirely
# (see link_matching_resightings) rather than compared.
_SIGNATURE_FIELDS = (
    "position",
    "order",
    "kind",
    "colour",
    "second_colour",
    "inscription",
    "inscription_colour",
)


def tag_signature(tags) -> frozenset:
    """The set of tags on a Capture or Resighting, as a hashable,
    order-independent value two records can be compared by.
    """
    return frozenset(tuple(getattr(tag, field) for field in _SIGNATURE_FIELDS) for tag in tags)


def link_matching_resightings(capture) -> int:
    """Link every not-yet-linked Resighting whose tags exactly match
    this Capture's tags. Returns how many were linked.

    Resightings with any uncertain tag are skipped -- an unsure reading
    shouldn't silently claim a match against a real ringing record.
    """
    signature = tag_signature(capture.tags.all())
    if not signature:
        return 0

    candidates = (
        Resighting.objects.filter(capture__isnull=True)
        .exclude(tags__uncertain=True)
        .prefetch_related("tags")
    )

    linked = 0
    for resighting in candidates:
        if tag_signature(resighting.tags.all()) == signature:
            resighting.capture = capture
            resighting.save(update_fields=["capture"])
            linked += 1
    return linked
