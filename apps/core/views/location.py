from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from ..models import Location


class LocationDetailView(View):
    """A Location's own region, country, coordinates, and notes, as
    JSON -- powers three bits of client-side behaviour on the
    location-picking forms (see core/static/core/location_form.js):
    showing the region and country a matched search result belongs to
    (LocationForm never submits them for an existing Location -- they
    aren't editable through it), the "Use default coordinates" link,
    and showing the Location's own notes as read-only text (its notes
    field, like region/country, isn't editable through LocationForm
    for an existing Location -- see resolve()).

    """

    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        return JsonResponse(
            {
                "region": location.region,
                "region_label": location.get_region_display(),
                "country": location.get_country_code(),
                "country_label": location.get_country_display(),
                "latitude": location.latitude,
                "longitude": location.longitude,
                "accuracy": location.accuracy,
                "notes": location.notes,
            }
        )
