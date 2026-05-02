/* ===== GLOBAL JS ENGINE ===== */
(function () {
  'use strict';

  /* ---------- HELPERS ---------- */
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];
  const getCart = () => JSON.parse(localStorage.getItem('pantoCart') || '[]');
  const getWish = () => JSON.parse(localStorage.getItem('pantoWishlist') || '[]');
  const getRecent = () => JSON.parse(localStorage.getItem('pantoRecent') || '[]');
  const setCart = v => localStorage.setItem('pantoCart', JSON.stringify(v));
  const setWish = v => localStorage.setItem('pantoWishlist', JSON.stringify(v));
  const setRecent = v => localStorage.setItem('pantoRecent', JSON.stringify(v));

  /* ---------- BADGE UPDATE ---------- */
  function updateBadges() {
    const cart = getCart();
    const wish = getWish();
    $$('#cart-badge').forEach(el => el.textContent = cart.length);
    $$('#wish-badge').forEach(el => el.textContent = wish.length);
  }

  /* ---------- CART ---------- */
  function addToCart(product) {
    const cart = getCart();
    if (!cart.find(p => p.id === product.id)) {
      cart.push(product);
      setCart(cart);
    }
    updateBadges();
  }

  /* ---------- WISHLIST ---------- */
  function toggleWishlist(product) {
    let wish = getWish();
    const idx = wish.findIndex(p => p.id === product.id);
    if (idx === -1) {
      wish.push(product);
    } else {
      wish.splice(idx, 1);
    }
    setWish(wish);
    updateBadges();
    return idx === -1; // true = added
  }

  /* ---------- RECENTLY VIEWED ---------- */
  function trackRecent(product) {
    if (!product.id) return;
    let recent = getRecent();
    recent = recent.filter(p => p.id !== product.id);
    recent.unshift(product);
    if (recent.length > 8) recent = recent.slice(0, 8);
    setRecent(recent);
  }

  /* ---------- DELIVERY DATE ---------- */
  function setDeliveryDates() {
    const els = $$('.dynamic-delivery');
    if (!els.length) return;
    const today = new Date();
    const d1 = new Date(today); d1.setDate(today.getDate() + 3);
    const d2 = new Date(today); d2.setDate(today.getDate() + 6);
    const fmt = d => d.toLocaleDateString('en-IN', { weekday: 'short', month: 'short', day: 'numeric' });
    els.forEach(el => el.textContent = `Estimated delivery: ${fmt(d1)} – ${fmt(d2)}`);
  }

  /* ---------- GALLERY ---------- */
  function initGallery() {
    const main = $('#main-product-image');
    if (!main) return;
    $$('.thumb').forEach(th => {
      th.addEventListener('click', () => {
        $$('.thumb').forEach(t => t.classList.remove('active'));
        th.classList.add('active');
        main.src = th.dataset.src || th.querySelector('img')?.src || th.src;
      });
    });
  }

  /* ---------- SEARCH ---------- */
  function initSearch() {
    const input = $('#global-search');
    const dropdown = $('#search-dropdown');
    const icon = $('.search-icon-pos');
    if (!input || !dropdown) return;

    // We can pull search data from current page OR a global store if needed. 
    // For this static version, we'll search whatever is available in the DOM.
    let allItems = $$('[data-search-name]').map(el => ({
      name: el.dataset.searchName,
      url: el.dataset.searchUrl,
      cat: el.dataset.searchCat
    }));

    // If on homepage, we might want to fake a global index. For now we use DOM.
    function executeSearch() {
      const q = input.value.trim().toLowerCase();
      if (q.length < 2) return;
      const match = allItems.find(i => i.name.toLowerCase().includes(q) || (i.cat && i.cat.toLowerCase().includes(q)));
      if (match) window.location.href = match.url;
      else alert('No products found matching: ' + q);
    }

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      if (q.length < 2) { dropdown.classList.remove('active'); return; }

      const matches = allItems.filter(i =>
        i.name.toLowerCase().includes(q) || (i.cat && i.cat.toLowerCase().includes(q))
      ).slice(0, 6);

      if (!matches.length) { dropdown.classList.remove('active'); return; }

      dropdown.innerHTML = matches.map(m =>
        `<a class="search-item" href="${m.url}">${m.name} <span style="color:var(--muted);font-size:0.8rem;margin-left:8px;">${m.cat}</span></a>`
      ).join('');
      dropdown.classList.add('active');
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') executeSearch();
    });

    if(icon) icon.addEventListener('click', executeSearch);

    document.addEventListener('click', e => {
      if (!input.contains(e.target) && !dropdown.contains(e.target))
        dropdown.classList.remove('active');
    });
  }

  /* ---------- FILTER SYSTEM ---------- */
  function initFilters() {
    const typeFilter = $('#type-filter');
    const priceFilter = $('#price-filter');
    const cards = $$('.masonry .card');
    const grid = $('.masonry');
    
    if (!typeFilter && !priceFilter || !grid || cards.length === 0) return;

    function applyFilters() {
      let visibleCards = [...cards];
      
      // Type filter (Mock logic since we only have 'Premium'/'Standard' implicitly)
      if (typeFilter && typeFilter.value !== 'All Types') {
        // Since we don't have explicit data-type, we mock it based on even/odd or name for demo
        visibleCards = visibleCards.filter((card, idx) => {
          if (typeFilter.value === 'Premium') return idx % 2 === 0;
          return idx % 2 !== 0;
        });
      }

      // Sort by price
      if (priceFilter) {
        visibleCards.sort((a, b) => {
          const pA = parseFloat(a.querySelector('.card-price').textContent.replace('$', ''));
          const pB = parseFloat(b.querySelector('.card-price').textContent.replace('$', ''));
          if (priceFilter.value === 'Price: Low to High') return pA - pB;
          if (priceFilter.value === 'Price: High to Low') return pB - pA;
          return 0;
        });
      }

      // Re-append to grid
      grid.innerHTML = '';
      visibleCards.forEach(card => {
        card.style.display = 'flex';
        grid.appendChild(card);
      });
      
      // Hide others
      cards.forEach(card => {
        if (!visibleCards.includes(card)) card.style.display = 'none';
      });
    }

    if(typeFilter) typeFilter.addEventListener('change', applyFilters);
    if(priceFilter) priceFilter.addEventListener('change', applyFilters);
  }

  /* ---------- BUY BUTTONS ---------- */
  function initBuyButtons() {
    $$('.buy-btn').forEach(btn => {
      btn.addEventListener('click', e => {
        e.preventDefault();
        const product = {
          id: btn.dataset.id || 'unknown',
          name: btn.dataset.name || 'PantoMart Product',
          price: btn.dataset.price || '$0',
          img: btn.dataset.img || '',
          url: window.location.pathname
        };
        addToCart(product);
        const orig = btn.textContent;
        btn.textContent = '✓ Added to Cart';
        btn.style.background = '#2ecc71';
        setTimeout(() => {
          btn.textContent = orig;
          btn.style.background = '';
        }, 2000);
      });
    });
  }

  /* ---------- WISHLIST BUTTONS ---------- */
  function initWishButtons() {
    $$('.wish-btn').forEach(btn => {
      const pid = btn.dataset.id;
      if (getWish().find(p => p.id === pid)) btn.classList.add('active');

      btn.addEventListener('click', e => {
        e.preventDefault();
        e.stopPropagation();
        const product = {
          id: pid,
          name: btn.dataset.name || '',
          price: btn.dataset.price || '',
          img: btn.dataset.img || '',
          url: btn.dataset.url || window.location.pathname
        };
        const added = toggleWishlist(product);
        btn.classList.toggle('active', added);
      });
    });
  }

  /* ---------- ANIMATE ON SCROLL ---------- */
  function initAOS() {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0.1 });
    $$('.aos').forEach(el => obs.observe(el));
  }

  /* ---------- STICKY BUY BAR ---------- */
  function initStickyBuy() {
    const bar = $('#sticky-buy-bar');
    const productInfo = $('.product-info');
    if (!bar || !productInfo) return;
    const obs = new IntersectionObserver(entries => {
      bar.style.display = entries[0].isIntersecting ? 'none' : 'flex';
    }, { threshold: 0 });
    obs.observe(productInfo);
  }

  /* ---------- TRACK RECENTLY VIEWED ON PRODUCT PAGES ---------- */
  function trackCurrentProduct() {
    const titleEl = $('h1.product-title');
    const priceEl = $('.product-price-val');
    const imgEl = $('#main-product-image');
    if (!titleEl) return;
    const pid = document.body.dataset.productId;
    if (!pid) return;
    trackRecent({
      id: pid,
      name: titleEl.textContent,
      price: priceEl?.textContent || '',
      img: imgEl?.src || '',
      url: window.location.pathname
    });
  }

  /* ---------- INIT ---------- */
  document.addEventListener('DOMContentLoaded', () => {
    updateBadges();
    setDeliveryDates();
    initGallery();
    initSearch();
    initFilters();
    initBuyButtons();
    initWishButtons();
    initAOS();
    initStickyBuy();
    trackCurrentProduct();
  });

})();
