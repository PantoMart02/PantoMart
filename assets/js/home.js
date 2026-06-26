async function initHome() {
 const container = document.getElementById('products-container');
 if (!container) return;

 const products = await fetchProducts();

 if (!products || products.length === 0) {
 container.innerHTML = `
 <div class="col-span-full py-20 text-center text-secondary opacity-50">
 No products available right now.
 </div>`;
 return;
 }

 // Group by category → pick highest rated product per category
 // Or just pick the top 3-6 products for the homepage
 const categoryMap = new Map();
 products.forEach(p => {
 if (!p || !p._id) return;
 const cat = (p.category || 'uncategorized').toLowerCase();
 const rating = Number(p.rating) || 0;
 if (!categoryMap.has(cat) || rating > Number((categoryMap.get(cat).rating) || 0)) {
 categoryMap.set(cat, p);
 }
 });

 const featured = Array.from(categoryMap.values()).slice(0, 6); // Show top 6
 
 let html = '';

 featured.forEach((product) => {
 const name = product.name || 'Premium Product';
 const price = Number(product.price) || 0;
 const image = getImageUrl(product.mainImage || product.image);
 const cat = (product.category || 'Essential').toLowerCase();
 const label = cat.charAt(0).toUpperCase() + cat.slice(1);
 const tagline = product.tagline || product.description || 'Crafted for the discerning few.';

 html += `
 <a href="product.html?id=${product._id}" class="flex flex-col group animate-fade-in">
 <div class="aspect-[4/5] overflow-hidden bg-surface mb-6 border border-outline-variant/20 relative">
 <img class="w-full h-full object-cover -[20%] group-hover:-0 group-hover:scale-105 transition-all duration-700" 
 src="${image}" 
 alt="${name}"
 onerror="this.src='./assets/images/placeholder.jpg'">
 <div class="absolute top-4 left-4 bg-surface/90 backdrop-blur-sm px-3 py-1 text-[10px] uppercase tracking-widest font-bold border border-outline-variant/20 text-primary">
 ${label}
 </div>
 </div>
 <h4 class="font-headline-md text-lg mb-1 text-primary group-hover:opacity-70 transition-opacity">${name}</h4>
 <p class="font-body-md text-secondary text-sm mb-4 line-clamp-1 opacity-80">${tagline}</p>
 <span class="font-body-lg text-primary font-medium">₹${price.toLocaleString('en-IN')}</span>
 </a>`;
 });

 container.innerHTML = html;
}
