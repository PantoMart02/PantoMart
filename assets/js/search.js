/* ===== SEARCH & FILTER ===== */
(function () {
  'use strict';

  // ======================
  // 🔍 SEARCH FUNCTION
  // ======================
  function initSearch() {
    if (!window.$) return;

    const input = window.$('#global-search');
    const dropdown = window.$('#search-dropdown');

    if (!input || !dropdown) return;

    // 🔥 Dynamic product storage
    let allItems = [];

    // 📦 Fetch products from API (REAL DATA)
    async function loadSearchData() {
      const products = await fetchProducts();

      if (!products) return;

      allItems = products.map(p => ({
        name: p.name || "Product",
        url: `product.html?id=${p._id}`, // ✅ correct routing
        cat: p.category || "General"
      }));
    }

    // Load data once
    loadSearchData();

    // 🔎 INPUT SEARCH
    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();

      if (q.length < 2) {
        dropdown.classList.remove('active');
        return;
      }

      const matches = allItems
        .filter(item =>
          item.name.toLowerCase().includes(q) ||
          item.cat.toLowerCase().includes(q)
        )
        .slice(0, 6);

      if (!matches.length) {
        dropdown.classList.remove('active');
        return;
      }

      dropdown.innerHTML = matches.map(m => `
        <a class="search-item" href="${m.url}">
          ${m.name}
          <span style="color:var(--muted);font-size:0.8rem;margin-left:8px;">
            ${m.cat}
          </span>
        </a>
      `).join('');

      dropdown.classList.add('active');
    });

    // ⏎ ENTER NAVIGATION
    input.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        const q = input.value.trim().toLowerCase();
        const match = allItems.find(i =>
          i.name.toLowerCase().includes(q)
        );
        if (match) window.location.href = match.url;
      }
    });

    // 🖱️ CLOSE DROPDOWN
    document.addEventListener('click', e => {
      if (!input.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove('active');
      }
    });
  }

  // ======================
  // 🎯 FILTER FUNCTION
  // ======================
  function initFilters() {
    if (!window.$) return;

    const priceFilter = window.$('#price-filter');
    const grid = window.$('.masonry');
    const cards = window.$$('.masonry .card');

    if (!grid || cards.length === 0) return;

    function applyFilters() {
      let visibleCards = [...cards];

      // 💰 PRICE SORT
      if (priceFilter) {
        visibleCards.sort((a, b) => {
          const pA = parseFloat(
            a.querySelector('.card-price').textContent.replace('₹', '').replace(/,/g, '')
          );
          const pB = parseFloat(
            b.querySelector('.card-price').textContent.replace('₹', '').replace(/,/g, '')
          );

          if (priceFilter.value === 'low') return pA - pB;
          if (priceFilter.value === 'high') return pB - pA;

          return 0;
        });
      }

      // 🔄 Re-render
      grid.innerHTML = '';
      visibleCards.forEach(card => {
        card.style.display = 'flex';
        grid.appendChild(card);
      });
    }

    if (priceFilter) {
      priceFilter.addEventListener('change', applyFilters);
    }
  }

  // ======================
  // 🚀 INIT
  // ======================
  document.addEventListener('DOMContentLoaded', () => {
    initSearch();
    initFilters();
  });

})();