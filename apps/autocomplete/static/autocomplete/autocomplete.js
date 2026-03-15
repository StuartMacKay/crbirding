/**
 * Progressively enhances every [data-autocomplete-field] <select> into
 * a Tom Select search box backed by /autocomplete/<field>/. Re-run on
 * htmx swaps and Django admin's "formset:added" too, since new fields
 * (e.g. an added formset row) can arrive without a full page load.
 */
(function () {
  function fetchResults(field, query, parentEl) {
    const params = new URLSearchParams({ q: query });
    if (parentEl && parentEl.value) {
      const parentField = parentEl.dataset.autocompleteField;
      if (parentField) {
        params.set(parentField, parentEl.value);
      }
    }
    return fetch("/autocomplete/" + field + "/?" + params.toString()).then(function (response) {
      return response.ok ? response.json() : { results: [] };
    });
  }

  // Prefix marking a Tom Select "create" result as free-typed text with
  // no matching record, rather than a real match's own value -- e.g.
  // LocationForm reads this back to tell "an existing Location was
  // picked" from "describe a new one with this name" server-side.
  var NEW_ITEM_PREFIX = "__new__:";

  function initOne(el) {
    if (el.tomselect || !window.TomSelect) {
      return;
    }
    // A Django admin inline's hidden template row -- left as a plain
    // <select> so the rows cloned from it can each be enhanced afresh.
    if (el.name.indexOf("__prefix__") !== -1) {
      return;
    }

    const field = el.dataset.autocompleteField;
    const dependsOn = el.dataset.autocompleteDependsOn;
    const parentEl = dependsOn ? document.getElementById(dependsOn) : null;
    const allowCreate = el.dataset.autocompleteAllowCreate === "true";

    const instance = new TomSelect(el, {
      valueField: "value",
      labelField: "label",
      searchField: "label",
      maxOptions: 50,
      create: allowCreate
        ? function (input) {
            return { value: NEW_ITEM_PREFIX + input, label: input };
          }
        : false,
      // Typing something with no match and moving on counts as
      // "create" too -- the user shouldn't have to notice and click
      // an "Add ..." row just to describe a new location.
      createOnBlur: allowCreate,
      render: allowCreate
        ? {
            option_create: function (data, escape) {
              return '<div class="create">Add a new location: "' + escape(data.input) + '"</div>';
            },
          }
        : {},
      // Load an initial page of results as soon as the field is
      // focused, not only once the user starts typing -- otherwise
      // opening the dropdown shows nothing but the current value.
      preload: "focus",
      // Render into <body> rather than in place: several containers
      // this widget ends up inside (Django admin's .form-row, some of
      // this site's own rounded cards) clip overflowing content, which
      // would otherwise hide the dropdown.
      dropdownParent: "body",
      load: function (query, callback) {
        fetchResults(field, query, parentEl)
          .then(function (data) {
            callback(data.results);
          })
          .catch(function () {
            callback();
          });
      },
    });

    if (parentEl) {
      parentEl.addEventListener("change", function () {
        instance.clear(true);
        instance.clearOptions();
      });
    }
  }

  function initAll(root) {
    root.querySelectorAll("[data-autocomplete-field]").forEach(initOne);
  }

  document.addEventListener("DOMContentLoaded", function () {
    initAll(document);
  });
  // Listened for on document, not document.body -- Django admin loads
  // this script in <head>, before <body> exists.
  document.addEventListener("htmx:afterSwap", function (event) {
    initAll(event.target);
  });
  document.addEventListener("formset:added", function (event) {
    initAll(event.target);
  });
})();
