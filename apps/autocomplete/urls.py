from django.urls import path

from .views import AutocompleteView

app_name = "autocomplete"

urlpatterns = [
    path("<str:field>/", AutocompleteView.as_view(), name="search"),
]
