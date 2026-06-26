async function initProduct() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');

    const container = document.getElementById('product-container');

    if (!id) {
        container.innerHTML = "❌ No product ID";
        return;
    }

    const product = await fetchProductById(id);

    if (!product) {
        container.innerHTML = "❌ Product not found";
        return;
    }

    const stars = "★".repeat(Math.round(product.rating || 4)) +
                  "☆".repeat(5 - Math.round(product.rating || 4));

    container.innerHTML = `
        <div style="display:flex; gap:40px; flex-wrap:wrap;">

            <!-- IMAGE -->
            <div style="flex:1; min-width:300px;">
                <img src="${product.mainImage}" 
                     style="width:100%; border-radius:10px;">
            </div>

            <!-- INFO -->
            <div style="flex:1; min-width:300px;">

                <h1>${product.name}</h1>

                <div style="margin:10px 0; font-size:18px;">
                    ${stars} (${product.reviewsCount || 0} reviews)
                </div>

                <h2 style="margin:10px 0;">₹${product.price}</h2>

                <p style="margin:15px 0;">
                    ${product.description || ''}
                </p>

                <ul>
                    ${(product.benefits || [])
                        .map(b => `<li>${b}</li>`)
                        .join('')}
                </ul>

                <button class="btn btn-primary"
                    data-id="${product._id}"
                    data-name="${product.name}"
                    data-price="${product.price}"
                    data-img="${product.mainImage}">
                    Add to Cart
                </button>

            </div>

        </div>

        <!-- 🔥 RELATED PRODUCTS -->
        <div style="margin-top:60px;">
            <h2>Related Products</h2>
            <div id="related-products" style="display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); gap:20px; margin-top:20px;"></div>
        </div>
    `;

    // 👉 Load related products
    loadRelated(product.category, product._id);
}


// 🔥 RELATED PRODUCTS FUNCTION
async function loadRelated(category, currentId) {
    const container = document.getElementById('related-products');
    if (!container) return;

    const products = await fetchProductsByCategory(category);

    if (!products) return;

    let html = '';

    products.forEach(p => {
        if (p._id === currentId) return;

        html += `
            <div class="card">
                <a href="product.html?id=${p._id}">
                    <img src="${p.mainImage}" style="width:100%">
                    <h4>${p.name}</h4>
                    <p>₹${p.price}</p>
                </a>
            </div>
        `;
    });

    container.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', initProduct);