const CART_KEY = 'pantoCart';

// ðŸ“¦ GET CART
function getCart() {
    try {
        const cart = JSON.parse(localStorage.getItem(CART_KEY));
        return Array.isArray(cart) ? cart : [];
    } catch {
        return [];
    }
}

// ðŸ’¾ SET CART
function setCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartBadges();
}

// âž• ADD TO CART
function addToCart(product) {
    if (!product || !product._id) return;

    const cart = getCart();
    const existing = cart.find(item => item._id === product._id);

    if (existing) {
        existing.qty = (existing.qty || 1) + 1;
    } else {
        cart.push({
            _id: product._id,
            name: product.name || "Product",
            price: Number(product.price) || 0,
            image: product.image || './assets/images/placeholder.jpg',
            qty: 1
        });
    }

    setCart(cart);
}

// âž– REMOVE ITEM
function removeFromCart(id) {
    let cart = getCart();
    cart = cart.filter(item => item._id !== id);
    setCart(cart);
    renderCartPage();
}

// ðŸ”„ UPDATE QTY (NEW)
function updateQuantity(id, change) {
    const cart = getCart();

    const item = cart.find(i => i._id === id);
    if (!item) return;

    item.qty = (item.qty || 1) + change;

    if (item.qty <= 0) {
        removeFromCart(id);
        return;
    }

    setCart(cart);
    renderCartPage();
}

// ðŸ”¢ CART BADGE
function updateCartBadges() {
    const cart = getCart();

    const count = cart.reduce(
        (sum, item) => sum + (item.qty || 1),
        0
    );

    document.querySelectorAll('#cart-badge')
        .forEach(el => (el.textContent = count));
}

// ðŸ›’ RENDER CART PAGE
function renderCartPage() {
    const container = document.getElementById('cart-container');
    if (!container) return;

    const cart = getCart();

    // âŒ Empty
    if (!cart || cart.length === 0) {
        container.innerHTML = `
      <div class="text-center text-muted" style="padding:40px 0;">
        Your cart is empty.<br>
        <a href="index.html" class="btn btn-primary mt-4">
          Continue Shopping
        </a>
      </div>
    `;
        return;
    }

    let total = 0;
    let htmlBuffer = `<div class="cart-items-list" style="max-width:800px;margin:0 auto;">`;

    cart.forEach(item => {
        if (!item || !item._id) return;

        const price = Number(item.price) || 0;
        const qty = item.qty || 1;
        const image = item.image || './assets/images/placeholder.jpg';

        total += price * qty;

        htmlBuffer += `
      <div class="cart-item flex-between"
        style="padding:16px;border-bottom:1px solid var(--border-color);align-items:center;">
        
        <div class="flex" style="align-items:center;gap:16px;">
          <img loading="lazy"
            src="${image}"
            alt="${item.name}"
            style="width:80px;height:80px;object-fit:cover;border-radius:8px;">
          
          <div>
            <h4 style="margin:0 0 8px 0;">${item.name}</h4>
            <div style="color:var(--accent);font-weight:600;">â‚¹${price}</div>

            <div style="display:flex;gap:8px;align-items:center;margin-top:6px;">
              <button class="qty-btn" data-id="${item._id}" data-change="-1">âˆ’</button>
              <span>${qty}</span>
              <button class="qty-btn" data-id="${item._id}" data-change="1">+</button>
            </div>
          </div>
        </div>

        <button class="btn btn-outline text-muted remove-btn"
          data-id="${item._id}">
          Remove
        </button>
      </div>
    `;
    });

    htmlBuffer += `
    <div class="cart-total flex-between"
      style="padding:24px 16px;margin-top:24px;font-size:1.2rem;font-weight:600;border-top:2px solid var(--border-color);">
      
      <span>Total:</span>
      <span style="color:var(--accent);">â‚¹${total.toLocaleString('en-IN')}</span>
    </div>

    <div class="text-center mt-4">
      <button class="btn btn-primary btn-full"
        style="max-width:400px;"
        onclick="alert('Checkout integration pending')">
        Proceed to Checkout
      </button>
    </div>
  </div>`;

    container.innerHTML = htmlBuffer;
}

// ðŸ§  GLOBAL EVENTS (CLEAN DELEGATION)
document.addEventListener('click', (e) => {

    // âž• Add to cart
    const buyBtn = e.target.closest('.buy-btn');
    if (buyBtn) {
        e.preventDefault();

        const product = {
            _id: buyBtn.dataset.id,
            name: buyBtn.dataset.name,
            price: buyBtn.dataset.price,
            image: buyBtn.dataset.img
        };

        addToCart(product);

        // âœ… Feedback
        const original = buyBtn.textContent;
        buyBtn.textContent = 'âœ“ Added';
        buyBtn.disabled = true;

        setTimeout(() => {
            buyBtn.textContent = original;
            buyBtn.disabled = false;
        }, 1200);
    }

    // âž– Remove
    const removeBtn = e.target.closest('.remove-btn');
    if (removeBtn) {
        e.preventDefault();
        removeFromCart(removeBtn.dataset.id);
    }

    // ðŸ”„ Quantity
    const qtyBtn = e.target.closest('.qty-btn');
    if (qtyBtn) {
        e.preventDefault();

        const id = qtyBtn.dataset.id;
        const change = Number(qtyBtn.dataset.change);

        updateQuantity(id, change);
    }
});

// ðŸš€ INIT
function initCart() {
    updateCartBadges();
    renderCartPage();
}
