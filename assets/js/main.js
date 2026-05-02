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

window.shareProduct = function() {
  const url = window.location.href;
  if (navigator.share) {
    navigator.share({
      title: document.title,
      url: url
    }).catch(err => {
      console.log('Error sharing', err);
    });
  } else {
    navigator.clipboard.writeText(url).then(() => {
      const shareBtn = document.querySelector('.share-btn');
      if (shareBtn) {
        shareBtn.classList.add('copied');
        // change color to indicate copied
        shareBtn.style.color = '#fff';
        shareBtn.style.background = 'var(--accent)';
        setTimeout(() => {
          shareBtn.classList.remove('copied');
          shareBtn.style.color = 'var(--muted)';
          shareBtn.style.background = 'var(--white)';
        }, 2000);
      }
      alert('Link copied to clipboard!');
    }).catch(err => {
      console.log('Failed to copy', err);
    });
  }
};
