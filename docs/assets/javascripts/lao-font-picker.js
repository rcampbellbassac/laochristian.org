// Lets the Lao review team preview each candidate Lao font site-wide and
// keeps their pick across page loads. Not tied to Material's instant-nav
// (not enabled in mkdocs.yml), so a plain load-time listener is enough.
// Preset ids are kept in sync with lao-christian-app's src/utils/laoFonts.ts.
(function () {
  var STORAGE_KEY = "lcLaoFont";

  function apply(value) {
    if (value) {
      document.documentElement.setAttribute("data-lao-font", value);
    } else {
      document.documentElement.removeAttribute("data-lao-font");
    }
  }

  var stored = window.localStorage.getItem(STORAGE_KEY) || "";
  apply(stored);

  document.addEventListener("DOMContentLoaded", function () {
    var select = document.getElementById("lc-lao-font-select");
    if (!select) return;
    select.value = stored;
    select.addEventListener("change", function () {
      stored = select.value;
      window.localStorage.setItem(STORAGE_KEY, stored);
      apply(stored);
    });
  });
})();
