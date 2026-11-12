// =====================================================================
// main.js - the website's only JavaScript.
//
// It does one job: the "Menu" button on phones. The site works fully
// without it (on a computer the menu is always visible). This approach
// is called "progressive enhancement": build a page that works for
// everyone, then add extras for browsers that can use them.
// =====================================================================

// Wait until the browser has finished reading the HTML. Otherwise the
// button we look for below might not exist yet.
document.addEventListener("DOMContentLoaded", () => {

  // Find the button and the menu by their id="..." in base.html.
  const toggle = document.getElementById("nav-toggle");
  const nav = document.getElementById("site-nav");

  // Only continue if both exist on this page.
  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    // classList.toggle adds the class "open" if it is missing, or
    // removes it if it is there. It returns true when it was added.
    // style.css shows the menu only when it has the "open" class.
    const isOpen = nav.classList.toggle("open");

    // Tell screen readers whether the menu is now open or closed.
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });
});