// js/cart.js

const CART_KEY = 'pantoCart';

function getCart() {
    try {
        const cart = JSON.parse(localStorage.getItem(CART_KEY));
        return Array.isArray(cart) ? cart : [];
    } catch {
        return [];
    }
}

function setCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartBadges();
}

function addToCart(product) {
    const cart = getCart();
    // Check if already in cart
    if (!cart.find(item => item.id === product.id)) {
        cart.push(product);
        setCart(cart);
    }
}

function removeFromCart(id) {
    let cart = getCart();
    cart = cart.filter(item => item.id !== id);
    setCart(cart);
    renderCartPage(); // Re-render if on cart page
}

function updateCartBadges() {
    const cart = getCart();
    const badges = document.querySelectorAll('#cart-badge');
    badges.forEach(badge => badge.textContent = cart.length);
}

function renderCartPage() {
    const container = document.getElementById('cart-container');
    if (!container) return; // Not on the cart page

    const cart = getCart();
    
    if (cart.length === 0) {
        container.innerHTML = '<div class="text-center text-muted" style="padding: 40px 0;">Your cart is empty. <br><a href="index.html" class="btn btn-primary mt-4">Continue Shopping</a></div>';
        return;
    }

    let html = '<div class="cart-items-list" style="max-width: 800px; margin: 0 auto;">';
    let total = 0;

    cart.forEach(item => {
        let priceNum = 0;
        if (typeof item.price === 'string') {
            priceNum = parseFloat(item.price.replace(/[^0-9.-]+/g, ""));
        } else if (typeof item.price === 'number') {
            priceNum = item.price;
        }
        total += priceNum;

        html += `
        <div class="cart-item flex-between" style="padding: 16px; border-bottom: 1px solid var(--border-color); align-items: center;">
            <div class="flex" style="align-items: center; gap: 16px;">
                <img src="${item.image || item.img || './assets/images/placeholder.jpg'}" alt="${item.name}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px;">
                <div>
                    <h4 style="margin: 0 0 8px 0;">${item.name}</h4>
                    <div style="color: var(--accent); font-weight: 600;">${item.price}</div>
                </div>
            </div>
            <button class="btn btn-outline text-muted remove-from-cart-btn" data-id="${item.id}" style="padding: 6px 12px; font-size: 0.8rem;">Remove</button>
        </div>
        `;
    });

    html += `
        <div class="cart-total flex-between" style="padding: 24px 16px; margin-top: 24px; font-size: 1.2rem; font-weight: 600; border-top: 2px solid var(--border-color);">
            <span>Total:</span>
            <span style="color: var(--accent);">₹${total.toLocaleString('en-IN')}</span>
        </div>
        <div class="text-center mt-4">
            <button class="btn btn-primary btn-full" style="max-width: 400px;" onclick="alert('Checkout integration pending')">Proceed to Checkout</button>
        </div>
    </div>`;

    container.innerHTML = html;
}

// Global Event Delegation for Add to Cart and Remove from Cart
document.addEventListener('click', (e) => {
    // Add to cart buttons (dynamic or static)
    const buyBtn = e.target.closest('.buy-btn');
    if (buyBtn) {
        e.preventDefault();
        const product = {
            id: buyBtn.dataset.id,
            name: buyBtn.dataset.name,
            price: buyBtn.dataset.price,
            image: buyBtn.dataset.img
        };
        addToCart(product);
        
        // Visual feedback
        const origText = buyBtn.textContent;
        buyBtn.textContent = '✓ Added';
        buyBtn.style.background = '#2ecc71';
        setTimeout(() => { 
            buyBtn.textContent = origText; 
            buyBtn.style.background = ''; 
        }, 2000);
    }

    // Remove from cart buttons
    const removeBtn = e.target.closest('.remove-from-cart-btn');
    if (removeBtn) {
        e.preventDefault();
        removeFromCart(removeBtn.dataset.id);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    updateCartBadges();
    renderCartPage();
});
