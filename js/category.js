document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const categoryName = urlParams.get('cat') || 'All';
    const container = document.getElementById('category-container');

    // Update headers
    const titleEl = document.getElementById('category-title');
    const subtitleEl = document.getElementById('category-subtitle');
    
    if (titleEl) titleEl.textContent = categoryName.charAt(0).toUpperCase() + categoryName.slice(1);
    if (subtitleEl) subtitleEl.textContent = `Panto${categoryName.charAt(0).toUpperCase() + categoryName.slice(1)} Essential Luxury Collection`;
    document.title = `${categoryName.charAt(0).toUpperCase() + categoryName.slice(1)} | PantoMart Luxury`;

    if (!container) return;

    if (!categoryName || categoryName === 'All') {
        container.innerHTML = '<div class="text-center text-muted" style="grid-column: 1 / -1; padding: 80px 0;">Please specify a category.</div>';
        return;
    }

    const products = await fetchProductsByCategory(categoryName);

    if (!products || products.length === 0) {
        container.innerHTML = '<div class="text-center text-muted" style="grid-column: 1 / -1; padding: 80px 0;">No products found in this category.</div>';
        return;
    }

    container.innerHTML = '';

    products.forEach((product) => {
        const name = product.name || 'Premium Product';
        const price = product.price || '';
        const img = product.image || './assets/images/placeholder.jpg';
        const productId = product.id;
        const productUrl = `product.html?id=${productId}`;
        const sub = product.subcategory || 'Exclusive Addition';

        const cardHtml = `
        <div class="card aos" data-search-name="${name}" data-search-url="${productUrl}" data-search-cat="${categoryName}">
          <button class="wish-btn" data-id="${productId}" data-name="${name}" data-img="${img}" data-url="${productUrl}">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          </button>
          <a href="${productUrl}">
            <div class="card-img-wrap"><img src="${img}" alt="${name}" onerror="this.src='./assets/images/placeholder.jpg'"></div>
            <div class="card-body">
              <h3 class="card-title">${name}</h3>
              <p class="card-sub">${sub}</p>
              <div class="card-price">${price}</div>
            </div>
          </a>
        </div>
        `;
        container.insertAdjacentHTML('beforeend', cardHtml);
    });
});
