/**
 * Behaviour specific to the location-picking section (see
 * core/_location_form_fields.html) that the generic autocomplete
 * widget (see autocomplete.js) doesn't cover:
 *
 * - Selecting an existing location fills in (and locks) the region
 *   and country fields with that location's own -- they're informational
 *   once a match is picked, not something this form can edit.
 * - Typing a name with no match (autocomplete.js's "create" option)
 *   unlocks region and country instead, for describing a new one, and
 *   shows which name is about to be added.
 * - "Use this location's default coordinates" copies a matched
 *   location's own latitude, longitude, and accuracy (already fetched
 *   when it was matched, see onLocationChange()) into the coordinate
 *   fields -- an explicit fallback for when the observer doesn't have
 *   their own reading, not something offered automatically, since
 *   those coordinate fields are otherwise blank rather than
 *   prefilled/hidden.
 * - A matched location's own notes (also already fetched) are shown
 *   as read-only text in place of the notes textarea -- LocationForm
 *   never saves typed notes against an existing Location (see
 *   resolve()), so editing them here would be misleading busywork;
 *   showing the existing ones instead surfaces information that's
 *   actually useful (site access, hazards, etc).
 */
(function () {
  // Must match autocomplete.js's own NEW_ITEM_PREFIX.
  var NEW_ITEM_PREFIX = "__new__:";

  function setSelectValue(select, value, label) {
    if (!select) return;
    if (select.tomselect) {
      if (value) {
        select.tomselect.addOption({value: value, label: label});
        select.tomselect.setValue(value, true);
      } else {
        select.tomselect.clear(true);
      }
    } else {
      select.value = value || "";
    }
  }

  function setHidden(el, hidden) {
    // Plain `el.hidden = ...` isn't enough for the notes textarea --
    // it's styled with Tailwind's `block` utility (see
    // core.forms._style_widgets), an author-level rule that wins over
    // the `[hidden]` UA stylesheet default regardless of specificity,
    // so the attribute alone silently does nothing.
    if (!el) return;
    el.hidden = hidden;
    el.style.display = hidden ? "none" : "";
  }

  function setSelectDisabled(select, disabled) {
    if (!select) return;
    if (select.tomselect) {
      if (disabled) {
        select.tomselect.disable();
      } else {
        select.tomselect.enable();
      }
    } else {
      select.disabled = disabled;
    }
  }

  function initLocationForm(root) {
    const searchSelect = root.querySelector("#id_location-search");
    if (!searchSelect || searchSelect.dataset.locationFormInit) {
      return;
    }
    searchSelect.dataset.locationFormInit = "true";

    const countrySelect = root.querySelector("#id_location-country");
    const regionSelect = root.querySelector("#id_location-region");
    const matchedHint = root.querySelector("#location-matched-hint");
    const newHint = root.querySelector("#location-new-hint");
    const newHintName = root.querySelector("#location-new-hint-name");
    const useDefaultsButton = root.querySelector("#use-default-coordinates");
    const latitudeInput = root.querySelector("#id_location-latitude");
    const longitudeInput = root.querySelector("#id_location-longitude");
    const accuracyInput = root.querySelector("#id_location-accuracy");
    const notesTextarea = root.querySelector("#id_location-notes");
    const notesHint = root.querySelector("#location-notes-hint");
    const notesReadonly = root.querySelector("#location-notes-readonly");

    let currentDetail = null;

    function reset() {
      currentDetail = null;
      setSelectDisabled(countrySelect, false);
      setSelectDisabled(regionSelect, false);
      setHidden(matchedHint, true);
      setHidden(newHint, true);
      setHidden(useDefaultsButton, true);
      setHidden(notesReadonly, true);
      setHidden(notesTextarea, false);
      setHidden(notesHint, false);
    }

    function showDescribingNew(name) {
      reset();
      if (newHint && newHintName) {
        newHintName.textContent = name;
        setHidden(newHint, false);
      }
    }

    function applyMatch(detail) {
      currentDetail = detail;
      setSelectValue(countrySelect, detail.country, detail.country_label);
      setSelectValue(regionSelect, detail.region, detail.region_label);
      setSelectDisabled(countrySelect, true);
      setSelectDisabled(regionSelect, true);
      setHidden(matchedHint, false);
      setHidden(newHint, true);
      setHidden(useDefaultsButton, false);
      if (notesReadonly) {
        notesReadonly.textContent = detail.notes || "No notes recorded for this location.";
      }
      setHidden(notesReadonly, false);
      setHidden(notesTextarea, true);
      setHidden(notesHint, true);
    }

    function onLocationChange() {
      const value = searchSelect.value;
      if (!value) {
        reset();
        return;
      }
      if (value.indexOf(NEW_ITEM_PREFIX) === 0) {
        showDescribingNew(value.slice(NEW_ITEM_PREFIX.length));
        return;
      }
      fetch("/locations/" + value + "/detail/")
        .then(function (response) {
          return response.ok ? response.json() : null;
        })
        .then(function (detail) {
          if (detail) applyMatch(detail);
        });
    }

    searchSelect.addEventListener("change", onLocationChange);

    if (useDefaultsButton) {
      useDefaultsButton.addEventListener("click", function () {
        if (!currentDetail) return;
        if (latitudeInput) latitudeInput.value = currentDetail.latitude || "";
        if (longitudeInput) longitudeInput.value = currentDetail.longitude || "";
        if (accuracyInput) accuracyInput.value = currentDetail.accuracy || "";
      });
    }

    // Already selected on page load (editing an observation/origin
    // that already has a location) -- reflect the same locked state
    // without waiting for a change event.
    if (searchSelect.value) {
      onLocationChange();
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initLocationForm(document);
  });
})();
