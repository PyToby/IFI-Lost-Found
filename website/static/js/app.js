/* ============================================================
   IFILAF — progressive enhancements only.
   The app fully works without this file: filters, search, menu
   open/close, the Found-only field and validation messages all
   render from the server or pure CSS. What's left here:

   1. Account menu: outside-click / Escape dismissal (<details>
      already handles open/close and keyboard).
   2. Photo preview + remove on the item form.
   3. Inline validation of the two required fields, mirroring
      the server's messages; server re-renders them when JS is off.
   4. Search clear button.
   5. Delete confirmation.
   ============================================================ */
(function () {
  'use strict';

  /* 1 — account menu: dismiss on outside click / Escape ---------- */
  var userMenu = document.querySelector('.nav__user');
  if (userMenu) {
    document.addEventListener('click', function (e) {
      if (userMenu.open && !userMenu.contains(e.target)) userMenu.open = false;
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && userMenu.open) {
        userMenu.open = false;
        userMenu.querySelector('summary').focus();
      }
    });
  }

  /* 2 — photo preview on the item form --------------------------- */
  var form = document.querySelector('[data-item-form]');
  if (form) {
    var file = form.querySelector('#in-photo');
    var prev = form.querySelector('#photoPrev');
    var img = form.querySelector('#photoImg');
    var url = null;

    file.addEventListener('change', function () {
      var f = file.files && file.files[0];
      if (!f) return;
      if (url) URL.revokeObjectURL(url);          // don't leak blob URLs
      url = URL.createObjectURL(f);
      img.src = url;
      prev.hidden = false;
    });

    form.querySelector('[data-remove-photo]').addEventListener('click', function () {
      if (url) { URL.revokeObjectURL(url); url = null; }
      file.value = '';
      img.removeAttribute('src');
      prev.hidden = true;
      file.focus();
    });

    /* 3 — inline validation of name + location ------------------- */
    var MSGS = {
      name: 'Give the item a name.',
      location: 'Add where it was lost or found.'
    };

    function setError(key, msg) {
      var field = form.querySelector('#f-' + key);
      var out = form.querySelector('#e-' + key);
      var input = form.querySelector('#in-' + key);
      field.classList.toggle('is-error', !!msg);
      out.textContent = msg || '';
      out.hidden = !msg;
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    }

    // Clear an error the moment the field becomes valid again.
    ['name', 'location'].forEach(function (key) {
      form.querySelector('#in-' + key).addEventListener('input', function (e) {
        if (e.target.value.trim()) setError(key, '');
      });
    });

    form.addEventListener('submit', function (e) {
      var firstBad = null;
      ['name', 'location'].forEach(function (key) {
        var input = form.querySelector('#in-' + key);
        if (!input.value.trim()) {
          setError(key, MSGS[key]);
          firstBad = firstBad || input;
        } else {
          setError(key, '');
        }
      });
      if (firstBad) { e.preventDefault(); firstBad.focus(); }
    });
  }

  /* 4 — search clear button -------------------------------------- */
  var search = document.querySelector('.search');
  if (search) {
    var input = search.querySelector('input[name="q"]');
    var clear = search.querySelector('[data-clear-search]');
    if (clear) clear.addEventListener('click', function (e) {
      e.preventDefault();                           // let the GET run without the button's value
      input.value = '';
      search.submit();
    });
  }

  /* 5 — delete confirmation on the detail page -------------------- */
  document.querySelectorAll('form[data-confirm]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      if (!window.confirm(f.dataset.confirm)) e.preventDefault();
    });
  });
})();
