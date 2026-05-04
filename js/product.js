document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const productId = urlParams.get('id');
    const container = document.getElementById('product-container');

    if (!container) return;

    if (!productId) {
        container.innerHTML = '<div class="text-center text-muted" style="padding: 80px 0;">Product not found.</div>';
        return;
    }

    const product = await fetchProductById(productId);

    if (!product) {
        container.innerHTML = '<div class="text-center text-muted" style="padding: 80px 0;">Product not found.</div>';
        return;
    }

    // Default values if API omits some fields
    const name = product.name || 'Premium Product';
    const price = product.price || '';
    const img = product.image || './assets/images/placeholder.jpg';
    const desc = product.description || 'A timeless, luxuriously crafted piece designed to effortlessly match your high-end lifestyle.';
    
    // Build the dynamic HTML
    const html = `
    <div class="product-layout">
      <!-- HERO GALLERY -->
      <div class="product-gallery">
        <div class="main-img position-relative">
          <button class="wish-btn wish-btn-main" data-id="${productId}" data-name="${name}" data-img="${img}" title="Add to Wishlist">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          </button>
          <button class="share-btn" onclick="shareProduct()" title="Share Product">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
          </button>
          <img src="${img}" id="main-product-image" alt="${name}">
        </div>
      </div>

      <!-- PRODUCT INFO -->
      <div class="product-info">
        <div class="rating-row">
          <div class="stars">★★★★☆</div>
          <div class="rating-count">4.7/5 (Reviews)</div>
        </div>
        <h1 class="product-title">${name}</h1>
        <div class="product-price"><span class="product-price-val" style="color: var(--accent);">${price}</span></div>
        <p class="product-hook">"${desc}"</p>
        
        <div class="labels-row">
          <span class="label-tag accent">Exclusive Edition</span>
          <span class="label-tag">Premium Crafted</span>
        </div>

        <button class="btn btn-primary btn-full buy-btn mt-3 mb-4" data-id="${productId}" data-name="${name}" data-price="${price}" data-img="${img}">Add to Cart</button>

        <div class="divider"></div>

        <div class="mb-4">
          <h4 class="mb-2">About This Product</h4>
          <p class="text-muted">${desc}</p>
        </div>

        <div class="delivery-box">
          <strong>White Glove Shipping</strong>
          <span class="dynamic-delivery text-muted">Calculating VIP delivery...</span>
        </div>
      </div>
    </div>
    
    <section class="editorial-banner" style="background-image: url('${img}');">
      <div class="editorial-overlay"></div>
      <div class="editorial-content">
        <h2>${name}</h2>
        <p>Experience the ultimate luxury.</p>
      </div>
    </section>

    <div id="sticky-buy-bar" class="sticky-buy-bar">
      <div style="flex:1;">
        <div style="font-weight:600;font-size:0.9rem;color:var(--white);">${name}</div>
        <div style="color:var(--accent);font-weight:700;">${price}</div>
      </div>
      <button class="btn btn-primary buy-btn" data-id="${productId}" data-name="${name}" data-price="${price}" data-img="${img}">Add to Cart</button>
    </div>
    `;

    container.innerHTML = html;
    
    // Update document title
    document.title = `${name} | PantoMart Luxury`;
});
