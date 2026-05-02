/* ===== DELIVERY SYSTEM ===== */
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', () => {
    if(!window.$$) return;
    const els = window.$$('.dynamic-delivery');
    if (!els.length) return;
    const today = new Date();
    const d1 = new Date(today); d1.setDate(today.getDate() + 3);
    const d2 = new Date(today); d2.setDate(today.getDate() + 6);
    const fmt = d => d.toLocaleDateString('en-IN', { weekday: 'short', month: 'short', day: 'numeric' });
    els.forEach(el => el.textContent = `Estimated delivery: ${fmt(d1)} - ${fmt(d2)}`);
  });
})();
