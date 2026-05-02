/* ===== SEARCH & FILTER ===== */
(function () {
  'use strict';
  function initSearch() {
    if(!window.$) return;
    const input = window.$('#global-search');
    const dropdown = window.$('#search-dropdown');
    if (!input || !dropdown) return;

    const getRootPath = () => window.location.pathname.includes('/PantoMart/') ? '/PantoMart' : '';
    const catalogData = [];
    const getRootPath = () => window.location.pathname.includes('/PantoMart/') ? '/PantoMart' : '';
    const catalogData = [{"name": "Aura Botanical Oil", "url": "/care/aura-botanical-oil/", "cat": "Care"}, {"name": "Celestial Eye Cream", "url": "/care/celestial-eye-cream/", "cat": "Care"}, {"name": "Golden Elixir Cream", "url": "/care/golden-elixir-cream/", "cat": "Care"}, {"name": "Luminous Pearl Cleanser", "url": "/care/luminous-pearl-cleanser/", "cat": "Care"}, {"name": "Midnight Hydration Mask", "url": "/care/midnight-hydration-mask/", "cat": "Care"}, {"name": "Obsidian Facial Roller", "url": "/care/obsidian-facial-roller/", "cat": "Care"}, {"name": "Pure Rosewater Mist", "url": "/care/pure-rosewater-mist/", "cat": "Care"}, {"name": "Radiant Glow Serum", "url": "/care/radiant-glow-serum/", "cat": "Care"}, {"name": "Silk Barrier Cream", "url": "/care/silk-barrier-cream/", "cat": "Care"}, {"name": "Velvet Renewal Polish", "url": "/care/velvet-renewal-polish/", "cat": "Care"}, {"name": "Alabaster Knit Sweater", "url": "/style/alabaster-knit-sweater/", "cat": "Style"}, {"name": "Bespoke Cufflinks", "url": "/style/bespoke-cufflinks/", "cat": "Style"}, {"name": "Cashmere Blend Wrap", "url": "/style/cashmere-blend-wrap/", "cat": "Style"}, {"name": "Cashmere Overcoat", "url": "/style/cashmere-overcoat/", "cat": "Style"}, {"name": "Golden Thread Blazer", "url": "/style/golden-thread-blazer/", "cat": "Style"}, {"name": "Leather Trim Briefcase", "url": "/style/leather-trim-briefcase/", "cat": "Style"}, {"name": "Midnight Suede Loafers", "url": "/style/midnight-suede-loafers/", "cat": "Style"}, {"name": "Minimalist Cotton Tee", "url": "/style/minimalist-cotton-tee/", "cat": "Style"}, {"name": "Obsidian Silk Tie", "url": "/style/obsidian-silk-tie/", "cat": "Style"}, {"name": "Onyx Statement Belt", "url": "/style/onyx-statement-belt/", "cat": "Style"}, {"name": "Silk Evening Scarf", "url": "/style/silk-evening-scarf/", "cat": "Style"}, {"name": "Tailored Wool Trousers", "url": "/style/tailored-wool-trousers/", "cat": "Style"}, {"name": "AeroCore Resistance Band", "url": "/fit/aerocore-resistance-band/", "cat": "Fit"}, {"name": "Aura Fitness Tracker", "url": "/fit/aura-fitness-tracker/", "cat": "Fit"}, {"name": "Balance Stability Sphere", "url": "/fit/balance-stability-sphere/", "cat": "Fit"}, {"name": "Carbon Fiber Kettlebell", "url": "/fit/carbon-fiber-kettlebell/", "cat": "Fit"}, {"name": "Elevate Push-up Grips", "url": "/fit/elevate-push-up-grips/", "cat": "Fit"}, {"name": "Obsidian Yoga Mat", "url": "/fit/obsidian-yoga-mat/", "cat": "Fit"}, {"name": "Titanium Grip Dumbbell", "url": "/fit/titanium-grip-dumbbell/", "cat": "Fit"}, {"name": "Velocity Jump Rope", "url": "/fit/velocity-jump-rope/", "cat": "Fit"}, {"name": "Zenith Recovery Foam Roller", "url": "/fit/zenith-recovery-foam-roller/", "cat": "Fit"}, {"name": "Alabaster Centerpiece Vase", "url": "/space/alabaster-centerpiece-vase/", "cat": "Space"}, {"name": "Aura Diffuser Core", "url": "/space/aura-diffuser-core/", "cat": "Space"}, {"name": "Brass Geometric Bookends", "url": "/space/brass-geometric-bookends/", "cat": "Space"}, {"name": "Eternity Hourglass", "url": "/space/eternity-hourglass/", "cat": "Space"}, {"name": "Golden Ratio Planter", "url": "/space/golden-ratio-planter/", "cat": "Space"}, {"name": "Lumi\u00e8re Crystal Lamp", "url": "/space/lumi\u00e8re-crystal-lamp/", "cat": "Space"}, {"name": "Midnight Silk Throw", "url": "/space/midnight-silk-throw/", "cat": "Space"}, {"name": "Nordic Minimalist Clock", "url": "/space/nordic-minimalist-clock/", "cat": "Space"}, {"name": "Obsidian Abstract Sculpture", "url": "/space/obsidian-abstract-sculpture/", "cat": "Space"}, {"name": "Velvet Accent Cushion", "url": "/space/velvet-accent-cushion/", "cat": "Space"}, {"name": "Alabaster Paw Cleanser", "url": "/pet/alabaster-paw-cleanser/", "cat": "Pet"}, {"name": "Aura Pet Wellness Roller", "url": "/pet/aura-pet-wellness-roller/", "cat": "Pet"}, {"name": "Golden Fleece DeShedder", "url": "/pet/golden-fleece-deshedder/", "cat": "Pet"}, {"name": "Midnight Coat Polisher", "url": "/pet/midnight-coat-polisher/", "cat": "Pet"}, {"name": "Obsidian Grooming Comb", "url": "/pet/obsidian-grooming-comb/", "cat": "Pet"}, {"name": "Royal Velvet Pet Brush", "url": "/pet/royal-velvet-pet-brush/", "cat": "Pet"}, {"name": "Silk Touch Pet Massager", "url": "/pet/silk-touch-pet-massager/", "cat": "Pet"}];
    let allItems = catalogData.map(i => ({ name: i.name, url: getRootPath() + i.url, cat: i.cat }));


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
