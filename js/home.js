document.addEventListener('DOMContentLoaded', async () => {
    const productsContainer = document.getElementById('products-container');
    if (!productsContainer) return;

    productsContainer.innerHTML = '<div class="text-center text-muted" style="padding: 40px 0;">Loading premium essentials...</div>';

    const products = await fetchProducts();
    
    if (!products || products.length === 0) {
        productsContainer.innerHTML = '<div class="text-center text-muted" style="padding: 40px 0;">No products found at this moment.</div>';
        return;
    }

    productsContainer.innerHTML = '';

    products.forEach((product, index) => {
        const isRtl = index % 2 !== 0;
        const alignStyle = isRtl ? 'align-items: center; direction: rtl;' : 'align-items: center;';
        const innerStyle = isRtl ? 'style="direction: ltr;"' : '';
        
        // Handle potentially missing fields gracefully
        const labelText = product.category || 'Premium Essential';
        const priceText = product.price ? product.price : '';
        const descText = product.description || 'Elevate your daily routine with this curated premium essential.';

        const layoutHtml = `
        <div class="product-layout aos mb-5" style="${alignStyle}">
          <div class="product-gallery" ${innerStyle}>
            <div class="main-img position-relative">
              <img src="${product.image}" alt="${product.name}" onerror="this.src='./assets/images/placeholder.jpg'">
            </div>
          </div>
          <div class="product-info" ${innerStyle}>
            <div class="labels-row"><span class="label-tag accent">${labelText}</span></div>
            <h2 class="mb-2">${product.name}</h2>
            <h4 class="mb-3" style="color: var(--accent);">${priceText}</h4>
            <p class="text-muted mb-4">${descText}</p>
            <a href="product.html?id=${product.id}" class="btn btn-primary">View Product</a>
          </div>
        </div>
        `;
        productsContainer.insertAdjacentHTML('beforeend', layoutHtml);
    });
});
