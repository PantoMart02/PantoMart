/* ===== CART & WISHLIST ENGINE ===== */
(function () {
  'use strict';
  const getCart = () => JSON.parse(localStorage.getItem('pantoCart') || '[]');
  const getWish = () => JSON.parse(localStorage.getItem('pantoWishlist') || '[]');
  const setCart = v => localStorage.setItem('pantoCart', JSON.stringify(v));
  const setWish = v => localStorage.setItem('pantoWishlist', JSON.stringify(v));
  const trackRecent = (product) => {
    let rawP = String(product.price).replace(/[$₹, ]/g, '');
    let numP = parseFloat(rawP) || 0;
    if (String(product.price).includes('$')) numP = Math.round(numP * 83);
    if (numP > 0) product.price = '₹' + numP.toLocaleString('en-IN', {maximumFractionDigits:0});

    const rootPath = window.location.pathname.includes('/PantoMart/') ? '/PantoMart/' : '/';
    product.img = rootPath + String(product.img).replace(/^(\.\.\/|\.\/)+/, '');
    product.url = rootPath + String(product.url).replace(/^(\.\.\/|\.\/)+/, '').replace(/^\//, '');

    let recent = JSON.parse(localStorage.getItem('pantoRecent') || '[]');
    recent = recent.filter(p => p.id !== product.id && p.name !== product.name);
    recent.unshift(product);
    if (recent.length > 8) recent = recent.slice(0, 8);
    localStorage.setItem('pantoRecent', JSON.stringify(recent));
  };

  function updateBadges() {
    window.$$ && window.$$('#cart-badge').forEach(el => el.textContent = getCart().length);
    window.$$ && window.$$('#wish-badge').forEach(el => el.textContent = getWish().length);
  }

  function initBuyButtons() {
    if(!window.$$) return;
    window.$$('.buy-btn').forEach(btn => {
      btn.addEventListener('click', e => {
        e.preventDefault();
        const userStr = localStorage.getItem('pantoUser');
        if(!userStr || userStr === 'undefined' || userStr === 'null') {
          alert('You must be logged in to buy products.');
          const rootPath = window.location.pathname.includes('/PantoMart/') ? '/PantoMart/' : '/';
          window.location.href = rootPath + 'login/';
          return;
        }

        const rootPath = window.location.pathname.includes('/PantoMart/') ? '/PantoMart/' : '/';
        const p = { 
          id: btn.dataset.id, 
          name: btn.dataset.name, 
          price: btn.dataset.price, 
          img: rootPath + String(btn.dataset.img).replace(/^(\.\.\/|\.\/)+/, ''), 
          url: rootPath + String(window.location.pathname).replace(/^(\.\.\/|\.\/)+/, '').replace(/^\//, '') 
        };
        if (!cart.find(x => x.id === p.id)) { cart.push(p); setCart(cart); }
        updateBadges();
        const orig = btn.textContent;
        btn.textContent = '✓ Added';
        btn.style.background = '#2ecc71';
        setTimeout(() => { btn.textContent = orig; btn.style.background = ''; }, 2000);
      });
    });
  }

  function initWishButtons() {
    if(!window.$$) return;
    window.$$('.wish-btn').forEach(btn => {
      const pid = btn.dataset.id;
      if (getWish().find(p => p.id === pid)) btn.classList.add('active');
      btn.addEventListener('click', e => {
        e.preventDefault(); e.stopPropagation();
        
        const userStr = localStorage.getItem('pantoUser');
        if(!userStr || userStr === 'undefined' || userStr === 'null') {
          alert('You must be logged in to save to your wishlist.');
          const rootPath = window.location.pathname.includes('/PantoMart/') ? '/PantoMart/' : '/';
          window.location.href = rootPath + 'login/';
          return;
        }

        let wish = getWish();
        const rootPath = window.location.pathname.includes('/PantoMart/') ? '/PantoMart/' : '/';
        const pUrl = btn.dataset.url ? rootPath + String(btn.dataset.url).replace(/^(\.\.\/|\.\/)+/, '').replace(/^\//, '') : rootPath + String(window.location.pathname).replace(/^(\.\.\/|\.\/)+/, '').replace(/^\//, '');
        const pImg = rootPath + String(btn.dataset.img).replace(/^(\.\.\/|\.\/)+/, '');

        const idx = wish.findIndex(p => p.id === pid);
        if (idx === -1) {
          wish.push({ id: pid, name: btn.dataset.name, price: btn.dataset.price, img: pImg, url: pUrl });
          btn.classList.add('active');
        } else {
          wish.splice(idx, 1);
          btn.classList.remove('active');
        }
        setWish(wish);
        updateBadges();
      });
    });
  }

  function trackCurrentProduct() {
    if(!window.$) return;
    const titleEl = window.$('h1.product-title');
    const pid = document.body.dataset.productId;
    if (titleEl && pid) {
      trackRecent({ id: pid, name: titleEl.textContent, price: window.$('.product-price-val')?.textContent || '', img: window.$('#main-product-image')?.src || '', url: window.location.pathname });
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    updateBadges();
    initBuyButtons();
    initWishButtons();
    trackCurrentProduct();
  });
})();
