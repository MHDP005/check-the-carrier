(function () {
  // Mobile menu toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  // Desktop dropdowns: only one open at a time; close on outside click or Escape
  var groups = Array.prototype.slice.call(document.querySelectorAll(".nav-group"));
  groups.forEach(function (g) {
    g.addEventListener("toggle", function () {
      if (g.open) groups.forEach(function (o) { if (o !== g) o.open = false; });
    });
  });
  document.addEventListener("click", function (e) {
    groups.forEach(function (g) { if (!g.contains(e.target)) g.open = false; });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") groups.forEach(function (g) { g.open = false; });
  });
  // Area picker on the home page
  var picker = document.querySelector("form.picker");
  if (picker) {
    picker.addEventListener("submit", function (e) {
      e.preventDefault();
      var sel = picker.querySelector("select");
      if (sel && sel.value) window.location.href = sel.value;
    });
  }
  // Open a collapsed section when someone follows a link to it
  function openTarget() {
    if (!location.hash) return;
    var el = document.getElementById(location.hash.slice(1));
    if (el && el.tagName === "DETAILS") el.open = true;
    if (el) { var d = el.closest("details"); if (d) d.open = true; }
  }
  window.addEventListener("hashchange", openTarget);
  openTarget();
})();
