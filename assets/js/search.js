/* ===== SEARCH & FILTER ===== */
(function () {
  'use strict';
  function initSearch() {
    if(!window.$) return;
    const input = window.$('#global-search');
    const dropdown = window.$('#search-dropdown');
    if (!input || !dropdown) return;

    let allItems = window.$$('[data-search-name]').map(el => ({
      name: el.dataset.searchName, url: el.dataset.searchUrl, cat: el.dataset.searchCat
    }));

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      if (q.length < 2) { dropdown.classList.remove('active'); return; }
      const matches = allItems.filter(i => i.name.toLowerCase().includes(q) || (i.cat && i.cat.toLowerCase().includes(q))).slice(0, 6);
      if (!matches.length) { dropdown.classList.remove('active'); return; }
      dropdown.innerHTML = matches.map(m => `<a class="search-item" href="${m.url}">${m.name} <span style="color:var(--muted);font-size:0.8rem;margin-left:8px;">${m.cat}</span></a>`).join('');
      dropdown.classList.add('active');
    });

    input.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        const q = input.value.trim().toLowerCase();
        const match = allItems.find(i => i.name.toLowerCase().includes(q));
        if (match) window.location.href = match.url;
      }
    });

    document.addEventListener('click', e => {
      if (!input.contains(e.target) && !dropdown.contains(e.target)) dropdown.classList.remove('active');
    });
  }

  function initFilters() {
    if(!window.$) return;
    const typeFilter = window.$('#type-filter');
    const priceFilter = window.$('#price-filter');
    const cards = window.$$('.masonry .card');
    const grid = window.$('.masonry');
    if (!grid || cards.length === 0) return;

    function applyFilters() {
      let visibleCards = [...cards];
      if (priceFilter) {
        visibleCards.sort((a, b) => {
          const pA = parseFloat(a.querySelector('.card-price').textContent.replace('₹', '').replace(/,/g, ''));
          const pB = parseFloat(b.querySelector('.card-price').textContent.replace('₹', '').replace(/,/g, ''));
          if (priceFilter.value === 'Price: Low to High') return pA - pB;
          if (priceFilter.value === 'Price: High to Low') return pB - pA;
          return 0;
        });
      }
      grid.innerHTML = '';
      visibleCards.forEach(card => { card.style.display = 'flex'; grid.appendChild(card); });
    }
    if(typeFilter) typeFilter.addEventListener('change', applyFilters);
    if(priceFilter) priceFilter.addEventListener('change', applyFilters);
  }

  document.addEventListener('DOMContentLoaded', () => {
    initSearch();
    initFilters();
  });
})();
