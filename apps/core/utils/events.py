"""Events recorded automatically against an Observation, alongside the
ones people add by hand (e.g. "Emailed the coordinator") on its events
page -- see core.models.Event.
"""

from ..models import Event, Observation


def record_origin_linked(observation: Observation, how: str = "Ringing details added") -> Event:
    """Note that `observation` has just been linked to its Origin, which
    closes it -- `how` says what linked it (see core.utils.matching).
    """
    origin = observation.origin
    description = how
    if origin.date:
        description += f": ringed {origin.date:%d-%b-%Y}"
    if origin.project_id:
        description += f" by {origin.project.name}"
    return Event.objects.create(observation=observation, description=description)
