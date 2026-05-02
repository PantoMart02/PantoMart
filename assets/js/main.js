/* ===== GLOBAL HELPERS & INIT ===== */
(function () {
  'use strict';
  window.$ = (sel, ctx = document) => ctx.querySelector(sel);
  window.$$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

  /* ---------- ANIMATE ON SCROLL ---------- */
  function initAOS() {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0.1 });
    window.$$('.aos').forEach(el => obs.observe(el));
  }

  /* ---------- GALLERY ---------- */
  function initGallery() {
    const main = window.$('#main-product-image');
    if (!main) return;
    window.$$('.thumb').forEach(th => {
      th.addEventListener('click', () => {
        window.$$('.thumb').forEach(t => t.classList.remove('active'));
        th.classList.add('active');
        main.src = th.dataset.src || th.querySelector('img')?.src || th.src;
      });
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initAOS();
    initGallery();
  });
})();
