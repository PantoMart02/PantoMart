// ======================
// 🏷️ CATEGORY ENGINE
// ======================
async function initCategory() {
 const params = new URLSearchParams(window.location.search);
 let category = params.get('cat')?.toLowerCase();
 const container = document.getElementById('category-container');

 // Only run on the category page
 console.log('initCategory check:', { container, category });
 if (!container) {
 console.log('initCategory aborting — no container!');
 return;
 }

 // Default to 'care' if no category specified
 if (!category) {
 category = 'care';
 console.log('No ?cat= param — defaulting to "care"');
 // Update URL so bookmarks / sharing work correctly
 const url = new URL(window.location);
 url.searchParams.set('cat', category);
 window.history.replaceState({}, '', url);
 // Update page title & active nav
 const titles = { care: 'Care', fit: 'Fit', style: 'Style', space: 'Space', pet: 'Pet' };
 const title = titles[category] || 'PantoMart';
 document.title = title + ' | PantoMart';
 const navBrand = document.querySelector('.nav-brand');
 if (navBrand) navBrand.textContent = 'Panto' + title;
 
 document.querySelectorAll('.nav-links a, [data-cat]').forEach(a => {
 if (a.dataset && a.dataset.cat === category) a.classList.add('active');
 });
 }

 const products = await fetchProductsByCategory(category);
 const safeProducts = Array.isArray(products) ? products : [];

 // Hide loading spinner, show container
 const loader = document.getElementById('loading-state');
 if (loader) loader.style.display = 'none';
 container.style.display = 'block';

 // Reset body styles for different themes
 document.body.style.backgroundColor = '';

 if (category === 'care') {
 renderCareCategory(safeProducts, container);
 } else if (category === 'style') {
 renderStyleCategory(safeProducts, container);
 } else if (category === 'fit') {
 renderFitCategory(safeProducts, container);
 } else if (category === 'space') {
 renderSpaceCategory(safeProducts, container);
 } else if (category === 'pet') {
 renderPetCategory(safeProducts, container);
 } else {
 renderDefaultCategory(safeProducts, container);
 }

 // Kick off animations
 requestAnimationFrame(() => {
 if (typeof initScrollReveal === 'function') initScrollReveal();
 });
}

// Style: Collection Listing (Stitch — The Style Edit Magazine)
// ======================
function renderStyleCategory(products, container) {
 const itemsHTML = products.map((p, i) => {
 const name = p.name || 'Architectural Piece';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Ready-to-Wear';
 const offsetClass = i % 2 === 1 ? 'md:mt-24' : '';
 return `
 <article class="group cursor-pointer ${offsetClass}" onclick="window.location.href='product.html?id=${p._id}'">
 <div class="border border-white/20 relative overflow-hidden mb-6 aspect-[3/4] bg-[#1a1a1a]">
 <img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-[2px]">
 <button class="bg-white text-black text-[12px] font-bold tracking-widest uppercase py-4 px-8 hover:bg-[#e9c349] transition-colors" style="font-family:'Manrope',sans-serif;">View Details</button>
 </div>
 </div>
 <div class="flex justify-between items-start">
 <div>
 <span class="text-[12px] font-bold tracking-[0.15em] text-[#a0a0a0] mb-2 block uppercase" style="font-family:'Manrope',sans-serif;">${sub}</span>
 <h3 class="text-[24px] leading-[32px] font-semibold text-white mb-1" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[16px] text-white font-bold" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</p>
 </div>
 <button class="w-10 h-10 border border-white/20 flex items-center justify-center text-white hover:text-[#e9c349] hover:border-[#e9c349] transition-colors" onclick="event.stopPropagation()">
 <span class="material-symbols-outlined" style="font-size:18px;">favorite_border</span>
 </button>
 </div>
 </article>
 `;
 }).join('');

 container.innerHTML = `
 <div class="style-editorial-layout" style="background:#0a0a0a;">

 <!-- 1. MAGAZINE HEADER BANNER -->
 <header class="w-full max-w-[1440px] mx-auto px-16 mt-16 mb-32">
 <div class="border border-white/20 relative h-[614px] flex flex-col justify-end p-8 bg-black overflow-hidden group">
 <img
 class="absolute inset-0 w-full h-full object-cover object-top opacity-90 transition-transform duration-1000 group-hover:scale-105"
 src="https://lh3.googleusercontent.com/aida-public/AB6AXuALaVLDfr1SniP7BZukYiM-m3_efJ6aEKpy0rmb2766TFujHs3UmCsjsUvr1ySv6DcHKRe05UoU_k6-wLt3EkCoEt9CW94vMaXTwbRuE7dU4iGvIXCQMrpW_RJeQK-VPcvPwyWWelI-O8P0RuC0k8z6g8EvrVSzEOmlZf2DIzWH-vE51kCeOmxJjTXoiQ6CVNWgsHBjvOQ5ArGnTmfJDYTT4QlCJwf1vHiHBGaQX1bD8MxaBH-RRcscpL1shqxkSirZot3AtOFmERNm"
 alt="Style Hero Banner"
 />
 <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
 <div class="relative z-10 flex justify-between items-end w-full">
 <div class="max-w-2xl">
 <span class="text-[12px] font-bold tracking-[0.2em] text-[#e9c349] mb-4 block uppercase border-b border-[#e9c349] w-max pb-1" style="font-family:'Manrope',sans-serif;">Collection 01</span>
 <h1 class="text-[80px] leading-[90px] tracking-tight font-bold text-white mb-4" style="font-family:'Noto Serif',serif;">The Style <br/>Edit.</h1>
 <p class="text-[18px] text-white/90 max-w-md" style="font-family:'Manrope',sans-serif;">Curated silhouettes defining the modern atelier. Uncompromising structures built for the discerning eye.</p>
 </div>
 <div class="flex gap-4">
 <button class="w-12 h-12 border border-[#e9c349] flex items-center justify-center text-[#e9c349] hover:bg-[#e9c349] hover:text-black transition-colors bg-black/20 backdrop-blur-sm">
 <span class="material-symbols-outlined">arrow_left</span>
 </button>
 <button class="w-12 h-12 border border-[#e9c349] flex items-center justify-center text-[#e9c349] hover:bg-[#e9c349] hover:text-black transition-colors bg-black/20 backdrop-blur-sm">
 <span class="material-symbols-outlined">arrow_right</span>
 </button>
 </div>
 </div>
 </div>
 </header>

 <!-- 2. PRODUCT GRID SECTION -->
 <section class="max-w-[1440px] mx-auto px-16 mb-32">
 <div class="flex justify-between items-end mb-16 border-b border-white/20 pb-8">
 <h2 class="text-[48px] font-semibold text-white" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">New Arrivals</h2>
 <a class="text-[12px] font-bold tracking-widest uppercase text-white hover:text-[#e9c349] transition-colors flex items-center gap-2" href="#" style="font-family:'Manrope',sans-serif;">
 View Full Collection <span class="material-symbols-outlined" style="font-size:16px;">east</span>
 </a>
 </div>
 <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
 ${itemsHTML}
 </div>
 </section>

 <!-- 3. STYLE FOOTER -->
 <footer class="bg-black w-full border-t-2 border-[#e9c349]">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-8 px-16 py-32 max-w-[1440px] mx-auto text-white">
 <div class="col-span-1">
 <span class="text-[48px] font-semibold text-[#e9c349] block mb-8" style="font-family:'Noto Serif',serif;">PantoMart</span>
 <p class="text-[16px] text-[#c6c6c6] max-w-xs mb-8" style="font-family:'Manrope',sans-serif;">Elevating the everyday through curated precision and uncompromising structure.</p>
 </div>
 <div class="col-span-1 flex flex-col gap-4">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#e9c349] mb-2 border-b border-white/20 pb-2 w-max" style="font-family:'Manrope',sans-serif;">Navigate</span>
 <a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="about/index.html" style="font-family:'Manrope',sans-serif;">The Atelier</a>
 <a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="#" style="font-family:'Manrope',sans-serif;">Sustainability</a>
 </div>
 <div class="col-span-1 flex flex-col gap-4">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#e9c349] mb-2 border-b border-white/20 pb-2 w-max" style="font-family:'Manrope',sans-serif;">Support</span>
 <a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="#" style="font-family:'Manrope',sans-serif;">Shipping &amp; Returns</a>
 <a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="contact/index.html" style="font-family:'Manrope',sans-serif;">Contact</a>
 <a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="privacy-policy/index.html" style="font-family:'Manrope',sans-serif;">Privacy Policy</a>
 </div>
 <div class="col-span-1 flex flex-col gap-4">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#e9c349] mb-2 border-b border-white/20 pb-2 w-max" style="font-family:'Manrope',sans-serif;">Newsletter</span>
 <div class="relative w-full border-b border-white/40 pb-2 mt-4">
 <input class="w-full bg-transparent border-none p-0 focus:outline-none text-[12px] tracking-widest uppercase text-white placeholder-white/30" placeholder="ENTER EMAIL" type="email" style="font-family:'Manrope',sans-serif;"/>
 <button class="absolute right-0 bottom-2 text-[#e9c349] hover:text-white transition-colors">
 <span class="material-symbols-outlined" style="font-size:18px;">arrow_forward</span>
 </button>
 </div>
 </div>
 <div class="col-span-1 md:col-span-4 mt-16 pt-8 border-t border-white/20 flex justify-between items-center">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#c6c6c6]" style="font-family:'Manrope',sans-serif;">&copy; 2024 PantoMart. All rights reserved.</span>
 </div>
 </div>
 </footer>
 </div>
 `;

 document.body.style.background = '#0a0a0a';
}

// Pet: Collection Listing (Stitch — The New Standard)
// ======================
function renderPetCategory(products, container) {
 const p0 = products[0] || {};
 const p1 = products[1] || {};
 const rest = products.slice(2);

 const getImg = (p) => getImageUrl(p.mainImage || p.image);
 const getName = (p, fallback) => p.name || fallback;
 const getPrice = (p) => Number(p.price) || 0;
 const getSub = (p, fallback) => p.subcategory || fallback;
 const getId = (p) => p._id || '#';

 const restCardsHTML = rest.map(p => {
 const name = getName(p, 'Companion Essential');
 const price = getPrice(p);
 const image = getImg(p);
 const sub = getSub(p, 'Premium Care');
 return `
 <article class="group cursor-pointer" onclick="window.location.href='product.html?id=${getId(p)}'">
 <div class="border border-white/20 relative overflow-hidden aspect-[3/4] bg-[#1a1a1a]">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:-0 transition-all duration-700 group-hover:scale-105" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
 <span class="bg-white text-black text-[12px] font-bold tracking-widest uppercase px-8 py-3 hover:bg-[#e9c349] transition-colors" style="font-family:'Manrope',sans-serif;">View Details</span>
 </div>
 </div>
 <div class="mt-4 pt-4 border-t border-white/20 flex justify-between items-start">
 <div>
 <p class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0] mb-1" style="font-family:'Manrope',sans-serif;">${sub}</p>
 <h3 class="text-[24px] font-semibold text-white leading-tight" style="font-family:'Noto Serif',serif;">${name}</h3>
 </div>
 <span class="text-[18px] font-bold text-[#e9c349]" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 </div>
 </article>
 `;
 }).join('');

 container.innerHTML = `
 <div class="pet-editorial-layout" style="background:#0a0a0a;background-image:url('data:image/svg+xml,%3Csvg width=\\'100\\' height=\\'100\\' viewBox=\\'0 0 100 100\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cfilter id=\\'noise\\'%3E%3CfeTurbulence type=\\'fractalNoise\\' baseFrequency=\\'0.8\\' numOctaves=\\'4\\' stitchTiles=\\'stitch\\'/%3E%3C/filter%3E%3Crect width=\\'100\\' height=\\'100\\' filter=\\'url(%23noise)\\' opacity=\\'0.02\\' fill=\\'%23ffffff\\'/%3E%3C/svg%3E');">

 <!-- 1. HERO SECTION -->
 <section class="max-w-[1440px] mx-auto px-16 mt-8 relative">
 <div class="w-full h-[716px] border border-white/20 relative overflow-hidden flex flex-col justify-end p-8 group">
 <img
 class="absolute inset-0 w-full h-full object-cover opacity-60"
 style="filter:(40%);mix-blend-mode:luminosity;"
 src="https://lh3.googleusercontent.com/aida-public/AB6AXuC36GHxT6wIN5dPXYLxn_Pz3pm8nsuxGo-ts5L_mS_kzx5guORbA5rhg7cgK6X7pVJ6DYYhWoWdQBe1oeSuG7JsTu0MVCnZftFI4ve5GF4TbIeipJTSeLoHPrGTNabWpwu0_FmoAh44IbJDxRxl40jRmBA3OnlW8RyQpOW_6V3bPe_6CqYQJugV-tGk2ViFOiSNIIGkSuQ39bH4n-FEZGttunj3uar1H5OHuND_OB4HUNUYIchEKKun3Ltx5KqTzVrZ81sLu8FW0g4G"
 alt="Pet Hero"
 />
 <!-- Gold corner accent -->
 <div class="absolute top-0 right-0 w-[120px] h-[120px] opacity-80" style="background:#e9c349;mix-blend-mode:color;"></div>
 <!-- Content overlay -->
 <div class="relative z-10 max-w-[600px] bg-black/80 p-8 border border-white/20 backdrop-blur-sm">
 <h1 class="text-[80px] leading-[90px] tracking-tight font-bold text-white mb-4 uppercase" style="font-family:'Noto Serif',serif;letter-spacing:-0.02em;">The New Standard</h1>
 <p class="text-[18px] text-white/90 mb-8" style="font-family:'Manrope',sans-serif;">Curated essentials for the discerning companion. Elevate the everyday with uncompromising craftsmanship.</p>
 <button class="bg-white text-black text-[12px] font-bold tracking-widest uppercase px-8 py-4 hover:bg-[#e9c349] transition-colors border border-white" style="font-family:'Manrope',sans-serif;"
 onclick="document.getElementById('pet-collection').scrollIntoView({behavior:'smooth'})">
 Explore Collection
 </button>
 </div>
 <!-- Carousel Controls -->
 <div class="absolute bottom-8 right-8 flex border border-white/20 bg-black z-10">
 <button class="w-16 h-16 flex items-center justify-center border-r border-white/20 hover:bg-[#e9c349] hover:text-black transition-colors text-white">
 <span class="material-symbols-outlined text-[32px]">arrow_left_alt</span>
 </button>
 <button class="w-16 h-16 flex items-center justify-center hover:bg-[#e9c349] hover:text-black transition-colors text-white">
 <span class="material-symbols-outlined text-[32px]">arrow_right_alt</span>
 </button>
 </div>
 </div>
 </section>

 <!-- 2. CHAPTER I: NOURISH & ALIGN -->
 <section class="max-w-[1440px] mx-auto px-16 mt-32">
 <div class="w-full border-t border-white/20 mb-8 pt-4 flex justify-between items-start">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">Chapter I</span>
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">Nourish &amp; Align</span>
 </div>
 <div class="grid grid-cols-12 gap-8 items-center cursor-pointer" onclick="window.location.href='product.html?id=${getId(p0)}'">
 <!-- Left Image -->
 <div class="col-span-12 md:col-span-7 relative border border-white/20 p-4 bg-[#1a1a1a] group">
 <img class="w-full aspect-[4/3] object-cover opacity-90 group-hover:opacity-100 group-hover:-0 transition-all duration-700" src="${getImg(p0)}" onerror="this.src='./assets/images/placeholder.jpg'" alt="${getName(p0, 'Care Product')}"/>
 <div class="absolute -bottom-6 -right-6 w-[200px] h-[200px] border border-[#e9c349] pointer-events-none"></div>
 </div>
 <!-- Right Text -->
 <div class="col-span-12 md:col-span-4 md:col-start-9 flex flex-col justify-center">
 <h2 class="text-[48px] font-semibold text-white mb-6 uppercase" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">Care</h2>
 <p class="text-[16px] text-[#a0a0a0] mb-4" style="font-family:'Manrope',sans-serif;">${getName(p0, 'Premium Pet Care')}</p>
 <p class="text-[16px] text-[#a0a0a0] mb-8 leading-relaxed" style="font-family:'Manrope',sans-serif;">A rigorous approach to well-being. Our formulations are stripped of the superfluous, leaving only the essential raw materials required for optimal vitality.</p>
 <p class="text-[24px] font-bold text-[#e9c349] mb-6" style="font-family:'Manrope',sans-serif;">&#8377;${getPrice(p0).toLocaleString('en-IN')}</p>
 <a class="flex items-center gap-2 text-[12px] font-bold tracking-widest uppercase text-white border-b border-white w-max pb-1 hover:text-[#e9c349] hover:border-[#e9c349] transition-colors" href="product.html?id=${getId(p0)}" style="font-family:'Manrope',sans-serif;" onclick="event.stopPropagation()">
 Discover Care <span class="material-symbols-outlined" style="font-size:16px;">arrow_forward</span>
 </a>
 </div>
 </div>
 </section>

 <!-- 3. CHAPTER II: STYLE -->
 <section class="max-w-[1440px] mx-auto px-16 mt-32">
 <div class="w-full border-t border-white/20 mb-8 pt-4">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">Chapter II</span>
 </div>
 <div class="grid grid-cols-12 gap-8 cursor-pointer" onclick="window.location.href='product.html?id=${getId(p1)}'">
 <!-- Left Text -->
 <div class="col-span-12 md:col-span-3 flex flex-col pt-[10%]">
 <h2 class="text-[48px] font-semibold text-white mb-6 uppercase" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">Style</h2>
 <p class="text-[16px] text-[#a0a0a0] mb-4" style="font-family:'Manrope',sans-serif;">${getName(p1, 'Premium Style')}</p>
 <p class="text-[16px] text-[#a0a0a0] mb-8 leading-relaxed" style="font-family:'Manrope',sans-serif;">Architecture for the animate. Structured silhouettes, premium hides, and hardware cast in solid brass. An intersection of function and high fashion.</p>
 <p class="text-[24px] font-bold text-[#e9c349] mb-6" style="font-family:'Manrope',sans-serif;">&#8377;${getPrice(p1).toLocaleString('en-IN')}</p>
 <a class="flex items-center gap-2 text-[12px] font-bold tracking-widest uppercase text-white border-b border-white w-max pb-1 hover:text-[#e9c349] hover:border-[#e9c349] transition-colors" href="product.html?id=${getId(p1)}" style="font-family:'Manrope',sans-serif;" onclick="event.stopPropagation()">
 View Lookbook <span class="material-symbols-outlined" style="font-size:16px;">arrow_forward</span>
 </a>
 </div>
 <!-- Right Large Image -->
 <div class="col-span-12 md:col-span-8 md:col-start-5 border border-white/20 relative group overflow-hidden bg-[#1a1a1a]">
 <div class="absolute inset-0 z-10 pointer-events-none" style="background:rgba(233,195,73,0.05);mix-blend-mode:screen;"></div>
 <img class="w-full aspect-square md:aspect-[16/9] object-cover opacity-90 group-hover:opacity-100 group-hover:-0 group-hover:scale-105 transition-all duration-700" src="${getImg(p1)}" onerror="this.src='./assets/images/placeholder.jpg'" alt="${getName(p1, 'Style Product')}"/>
 </div>
 </div>
 </section>

 <!-- 4. REMAINING PRODUCTS GRID -->
 ${rest.length > 0 ? `
 <section class="max-w-[1440px] mx-auto px-16 mt-32" id="pet-collection">
 <div class="border-t border-white/20 pt-4 mb-16 flex justify-between items-end">
 <h2 class="text-[48px] font-semibold text-white" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">The Collection</h2>
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">Pet / Essentials</span>
 </div>
 <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
 ${restCardsHTML}
 </div>
 </section>
 ` : `<div id="pet-collection"></div>`}

 <!-- 5. PET FOOTER -->
 <footer class="w-full mt-32 bg-black border-t-2 border-[#e9c349]">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-8 px-16 py-32 max-w-[1440px] mx-auto">
 <div class="col-span-1 md:col-span-2 flex flex-col justify-between">
 <div class="text-[48px] font-semibold text-[#e9c349] uppercase tracking-tight" style="font-family:'Noto Serif',serif;">PantoMart</div>
 <div class="text-white text-[16px] opacity-60 mt-8" style="font-family:'Manrope',sans-serif;">&copy; 2024 PantoMart. All rights reserved.</div>
 </div>
 <div class="col-span-1 flex flex-col gap-4" style="font-family:'Manrope',sans-serif;">
 <a class="text-[#c6c6c6] text-[16px] hover:text-[#e9c349] transition-colors" href="about/index.html">The Atelier</a>
 <a class="text-[#c6c6c6] text-[16px] hover:text-[#e9c349] transition-colors" href="#">Sustainability</a>
 <a class="text-[#c6c6c6] text-[16px] hover:text-[#e9c349] transition-colors" href="#">Shipping &amp; Returns</a>
 </div>
 <div class="col-span-1 flex flex-col gap-4" style="font-family:'Manrope',sans-serif;">
 <a class="text-[#c6c6c6] text-[16px] hover:text-[#e9c349] transition-colors" href="contact/index.html">Contact</a>
 <a class="text-[#c6c6c6] text-[16px] hover:text-[#e9c349] transition-colors" href="privacy-policy/index.html">Privacy Policy</a>
 </div>
 </div>
 </footer>
 </div>
 `;

 document.body.style.background = '#0a0a0a';
}

// Space: Collection Listing (Stitch — The Space Atelier)
// ======================
function renderSpaceCategory(products, container) {
 // Map products to the 4-slot asymmetric bento
 const p0 = products[0] || {};
 const p1 = products[1] || {};
 const p2 = products[2] || {};
 const p3 = products[3] || {};

 const cardLarge = (p) => {
 const name = p.name || 'Lunar Sphere Lamp';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Ambient Illumination Object';
 const id = p._id || '#';
 return `
 <div class="col-span-12 md:col-span-8 group cursor-pointer" onclick="window.location.href='product.html?id=${id}'">
 <div class="w-full aspect-[4/3] bg-[#1a1a1a] relative overflow-hidden border border-white/20">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-transform duration-700 ease-in-out" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 </div>
 <div class="flex justify-between items-start mt-6 border-t border-white/20 pt-4">
 <div>
 <h3 class="text-[32px] font-semibold text-white" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[16px] text-[#a0a0a0] mt-2" style="font-family:'Manrope',sans-serif;">${sub}</p>
 </div>
 <div class="text-right flex flex-col items-end">
 <span class="text-[18px] text-[#e9c349] font-bold tracking-wide block" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 <button class="mt-4 text-[12px] font-bold tracking-widest uppercase bg-white text-black px-8 py-3 hover:bg-[#e9c349] transition-colors" style="font-family:'Manrope',sans-serif;">Acquire</button>
 </div>
 </div>
 </div>
 `;
 };

 const cardVertical = (p) => {
 const name = p.name || 'Obsidian Monolith';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Sculptural Vessel';
 const id = p._id || '#';
 return `
 <div class="col-span-12 md:col-span-4 group flex flex-col mt-16 md:mt-0 cursor-pointer" onclick="window.location.href='product.html?id=${id}'">
 <div class="w-full aspect-[3/4] bg-[#1a1a1a] relative overflow-hidden border border-white/20">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-transform duration-700 ease-in-out" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 </div>
 <div class="flex justify-between items-start mt-6 border-t border-white/20 pt-4 flex-grow">
 <div>
 <h3 class="text-[24px] font-semibold text-white" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[16px] text-[#a0a0a0] mt-1" style="font-family:'Manrope',sans-serif;">${sub}</p>
 </div>
 <span class="text-[18px] text-[#e9c349] font-bold tracking-wide" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 </div>
 </div>
 `;
 };

 const cardMidSquare = (p) => {
 const name = p.name || 'Astral Mobile';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Suspended Kinetic Art';
 const id = p._id || '#';
 return `
 <div class="col-span-12 md:col-span-6 group mt-32 cursor-pointer" onclick="window.location.href='product.html?id=${id}'">
 <div class="w-full aspect-square bg-[#1a1a1a] relative overflow-hidden border border-white/20">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-transform duration-700 ease-in-out" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 </div>
 <div class="flex justify-between items-start mt-6 border-t border-white/20 pt-4 w-11/12">
 <div>
 <h3 class="text-[30px] font-semibold text-white" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[16px] text-[#a0a0a0] mt-1" style="font-family:'Manrope',sans-serif;">${sub}</p>
 </div>
 <span class="text-[18px] text-[#e9c349] font-bold tracking-wide block" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 </div>
 </div>
 `;
 };

 const cardMidOffset = (p) => {
 const name = p.name || 'Void Seating';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Architectural Furniture';
 const id = p._id || '#';
 return `
 <div class="col-span-12 md:col-span-6 group mt-32 cursor-pointer" onclick="window.location.href='product.html?id=${id}'">
 <div class="w-full aspect-[4/5] bg-[#1a1a1a] relative overflow-hidden border border-white/20 md:ml-auto md:w-5/6">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-transform duration-700 ease-in-out" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 </div>
 <div class="flex justify-between items-start mt-6 border-t border-white/20 pt-4 md:ml-auto md:w-5/6">
 <div>
 <h3 class="text-[30px] font-semibold text-white" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[16px] text-[#a0a0a0] mt-1" style="font-family:'Manrope',sans-serif;">${sub}</p>
 </div>
 <span class="text-[18px] text-[#e9c349] font-bold tracking-wide block" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 </div>
 </div>
 `;
 };

 container.innerHTML = `
 <div class="space-editorial-layout" style="background:#0a0a0a;">

 <!-- 1. HERO BLACK BANNER -->
 <section class="max-w-[1440px] mx-auto px-16 pb-8 mt-16">
 <div class="bg-black text-white flex justify-between items-center px-8 py-12 md:py-24 w-full border border-white/20 relative overflow-hidden">
 <div class="absolute inset-0 opacity-5 mix-blend-overlay" style="background-image:repeating-linear-gradient(45deg,#fff 25%,transparent 25%,transparent 75%,#fff 75%,#fff),repeating-linear-gradient(45deg,#fff 25%,transparent 25%,transparent 75%,#fff 75%,#fff);background-position:0 0,10px 10px;background-size:20px 20px;"></div>
 <span class="material-symbols-outlined text-4xl md:text-5xl cursor-pointer text-[#a0a0a0] hover:text-[#e9c349] transition-colors relative z-10">arrow_left_alt</span>
 <h1 class="text-[80px] leading-[90px] tracking-[0.1em] font-bold text-center uppercase text-white relative z-10" style="font-family:'Noto Serif',serif;letter-spacing:-0.02em;">Space</h1>
 <span class="material-symbols-outlined text-4xl md:text-5xl cursor-pointer text-[#a0a0a0] hover:text-[#e9c349] transition-colors relative z-10">arrow_right_alt</span>
 </div>
 </section>

 <!-- 2. ARTIFACTS GRID -->
 <section class="max-w-[1440px] mx-auto px-16 pb-32">
 <div class="border-b border-white/20 mb-16 pb-4 flex flex-col md:flex-row justify-between items-start md:items-end gap-8">
 <h2 class="text-[48px] font-semibold text-white" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">Artifacts</h2>
 <div class="flex gap-8 text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">
 <span class="cursor-pointer text-white border-b-2 border-white pb-1">All Objects</span>
 <span class="cursor-pointer hover:text-white transition-colors">Illumination</span>
 <span class="cursor-pointer hover:text-white transition-colors">Structures</span>
 </div>
 </div>
 <div class="grid grid-cols-12 gap-8">
 ${cardLarge(p0)}
 ${cardVertical(p1)}
 ${cardMidSquare(p2)}
 ${cardMidOffset(p3)}
 </div>
 </section>

 <!-- 3. EDITORIAL QUOTE STRIP -->
 <section class="max-w-[1440px] mx-auto px-16 py-32 border-y border-white/20">
 <div class="w-full max-w-4xl mx-auto text-center">
 <p class="text-[48px] leading-[56px] font-semibold text-white italic" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">
 &ldquo;The absence of clutter is the presence of intention. Our space collection is curated for the quiet moments.&rdquo;
 </p>
 <div class="w-16 h-[2px] bg-[#e9c349] mx-auto mt-12"></div>
 </div>
 </section>

 <!-- 4. SPACE FOOTER -->
 <footer class="bg-black w-full border-t-2 border-[#e9c349]">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-8 px-16 py-32 max-w-[1440px] mx-auto">
 <div class="col-span-1 flex flex-col justify-between">
 <div class="text-[48px] font-semibold text-[#e9c349]" style="font-family:'Noto Serif',serif;">PantoMart</div>
 <div class="text-[16px] text-white mt-8 md:mt-0" style="font-family:'Manrope',sans-serif;">&copy; 2024 PantoMart. All rights reserved.</div>
 </div>
 <div class="col-span-1 md:col-span-3 grid grid-cols-2 md:grid-cols-3 gap-8 text-[#c6c6c6] text-[16px]" style="font-family:'Manrope',sans-serif;">
 <div class="flex flex-col gap-4">
 <a class="hover:text-[#e9c349] transition-colors" href="about/index.html">The Atelier</a>
 <a class="hover:text-[#e9c349] transition-colors" href="#">Sustainability</a>
 </div>
 <div class="flex flex-col gap-4">
 <a class="hover:text-[#e9c349] transition-colors" href="#">Shipping &amp; Returns</a>
 <a class="hover:text-[#e9c349] transition-colors" href="contact/index.html">Contact</a>
 </div>
 <div class="flex flex-col gap-4">
 <a class="hover:text-[#e9c349] transition-colors" href="privacy-policy/index.html">Privacy Policy</a>
 </div>
 </div>
 </div>
 </footer>
 </div>
 `;

 document.body.style.background = '#0a0a0a';
}

// Care: Collection Listing (Stitch Editorial — L'Art du Soin)
// ======================
function renderCareCategory(products, container) {
 const itemsHTML = products.map((p, i) => {
 const name = p.name || 'Restorative Formula';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Cellular regeneration complex';
 const offsetClass = i === 1 ? 'md:mt-16' : '';
 return `
 <article class="group border border-transparent hover:border-white/20 transition-colors duration-300 pb-8 cursor-pointer ${offsetClass}" onclick="window.location.href='product.html?id=${p._id}'">
 <div class="relative aspect-[3/4] mb-4 bg-[#1a1a1a] overflow-hidden border border-white/20">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-transform duration-700" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 <div class="absolute inset-0 bg-white/0 group-hover:bg-white/5 transition-colors duration-300"></div>
 </div>
 <h3 class="text-[28px] font-semibold text-white mb-2 leading-tight" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[15px] text-[#a0a0a0] mb-4" style="font-family:'Manrope',sans-serif;">${sub}</p>
 <div class="flex justify-between items-center border-t border-white/20 pt-2">
 <span class="text-[12px] font-bold tracking-widest uppercase text-white" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 <button class="text-[12px] font-bold tracking-widest uppercase text-[#e9c349] hover:text-white transition-colors" style="font-family:'Manrope',sans-serif;">ADD TO CART</button>
 </div>
 </article>
 `;
 }).join('');

 container.innerHTML = `
 <div class="care-editorial-layout" style="background:#0a0a0a;">

 <!-- 1. IMMERSIVE EDITORIAL HERO BANNER -->
 <section class="relative w-full h-[614px] border border-white/20 flex items-center justify-center overflow-hidden">
 <div class="absolute inset-0 bg-black/40 z-10"></div>
 <img
 class="absolute inset-0 w-full h-full object-cover opacity-70"
 src="https://lh3.googleusercontent.com/aida-public/AB6AXuC76Q8sOj8HX8EIduBflvG7-M10IzQSI5fjXrwT_l6eyogiLzDrMfmTpmPPzW-Ts74bmGQSzxc4ikvXVMIFRT8LCYjdOGrstuMGFkQFYFMEKH6O6fXgg49nOMDCU2UCm1ge0kZmXB0NxAMeCf0uUxcc2OpgGDFThdS7PVe6zf9QiTBtl6NIZm_sLTdeFHnXfyywKSoKTqmSgvNTgeYWlwnb1Q5gjjjB_MgvBpBiGwLHwta8KUSIfUsSBEuiQ5gQF-VX7knx8HvetPwf"
 alt="Care Hero Banner"
 />
 <div class="relative z-20 text-center max-w-2xl px-8">
 <h1 class="text-[56px] font-bold leading-tight text-white bg-black/80 p-4 border border-white/20 inline-block backdrop-blur-sm" style="font-family:'Noto Serif',serif;">PantoCare</h1>
 <p class="text-[18px] text-white/90 mt-6 bg-black/80 p-4 border border-white/20 backdrop-blur-sm" style="font-family:'Manrope',sans-serif;">Curated regimens for the discerning patron. A dedication to purity, efficacy, and tactile perfection.</p>
 </div>
 <button class="absolute bottom-8 left-1/2 -translate-x-1/2 z-20 p-4 bg-black border border-white/20 hover:bg-[#e9c349] hover:text-black transition-colors">
 <span class="material-symbols-outlined text-white">arrow_downward</span>
 </button>
 </section>

 <!-- 2. CURATED COLLECTION GRID -->
 <section class="mt-32 px-16">
 <div class="flex items-end justify-between border-b border-white/20 pb-4 mb-8">
 <h2 class="text-[48px] font-semibold text-white" style="font-family:'Noto Serif',serif;">The Collection</h2>
 <div class="text-[12px] font-bold tracking-[0.15em] uppercase text-[#e9c349]" style="font-family:'Manrope',sans-serif;">01 / CARE</div>
 </div>
 <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
 ${itemsHTML}
 </div>
 </section>

 <!-- 3. PHILOSOPHY BANNER -->
 <section class="mt-32 mx-16 relative h-[512px] border border-white/20 flex items-center justify-center overflow-hidden">
 <img
 class="absolute inset-0 w-full h-full object-cover opacity-60"
 src="https://lh3.googleusercontent.com/aida-public/AB6AXuBaG-rv0amq8-JxmFk6GFdw8Mg8ljfQTC-Muy8mjHglPFNXaqmzZ7jnmtpt93rBNH5pBdKMQjjpbdzcwtr2qJl_BCn9rOqyLTAfvD2YlTLz89ywdlf-kTM5VgQM0Q_orGvFQFgahQrwxj70XkiyWRNOliQJtEl6Qj7ejctvbrMGQ89Kf0nubFdTQcKCNltABZnpNLDJxOvhudqUN-YWdf2SXhH-ham5ENLKAa7AXeGlhaQE2DW8KQr3VM2ZFuBEFDeBqQ5u6tegvSPa"
 alt="Philosophy Banner"
 />
 <div class="absolute inset-0 bg-black/60 backdrop-blur-sm z-10"></div>
 <div class="relative z-20 text-center max-w-xl px-8">
 <h2 class="text-[48px] font-semibold text-white mb-6" style="font-family:'Noto Serif',serif;">The Philosophy</h2>
 <p class="text-[18px] text-white/90 mb-8" style="font-family:'Manrope',sans-serif;">We believe that true care is a discipline of reduction. Stripping away the superfluous to reveal the essential.</p>
 <a href="about/index.html" class="inline-block px-8 py-4 bg-white text-black text-[12px] font-bold tracking-widest uppercase hover:bg-[#e9c349] hover:text-black transition-colors" style="font-family:'Manrope',sans-serif;">DISCOVER MORE</a>
 </div>
 </section>

 <!-- 4. CARE FOOTER -->
 <footer class="mt-32 bg-black border-t-2 border-[#e9c349]">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-8 px-16 py-32 max-w-[1440px] mx-auto">
 <div class="col-span-1 md:col-span-2">
 <h2 class="text-[48px] font-semibold text-[#e9c349] mb-4" style="font-family:'Noto Serif',serif;">PantoMart</h2>
 <p class="text-[16px] text-white max-w-xs mb-8" style="font-family:'Manrope',sans-serif;">Curated essentials for the avant-garde.</p>
 <p class="text-[16px] text-white" style="font-family:'Manrope',sans-serif;">&copy; 2024 PantoMart. All rights reserved.</p>
 </div>
 <div class="col-span-1">
 <ul class="space-y-4 text-[16px] text-[#c6c6c6]" style="font-family:'Manrope',sans-serif;">
 <li><a class="hover:text-[#e9c349] transition-colors" href="about/index.html">The Atelier</a></li>
 <li><a class="hover:text-[#e9c349] transition-colors" href="#">Sustainability</a></li>
 <li><a class="hover:text-[#e9c349] transition-colors" href="#">Shipping &amp; Returns</a></li>
 </ul>
 </div>
 <div class="col-span-1">
 <ul class="space-y-4 text-[16px] text-[#c6c6c6]" style="font-family:'Manrope',sans-serif;">
 <li><a class="hover:text-[#e9c349] transition-colors" href="contact/index.html">Contact</a></li>
 <li><a class="hover:text-[#e9c349] transition-colors" href="privacy-policy/index.html">Privacy Policy</a></li>
 </ul>
 </div>
 </div>
 </footer>
 </div>
 `;

 document.body.style.background = '#0a0a0a';
}

// Fit: Collection Listing (Stitch — Architecture of Motion)
// ======================
function renderFitCategory(products, container) {
 // Build bento grid: first product = large feature (left), rest = stacked right
 const featured = products[0] || {};
 const stacked = products.slice(1, 3);

 const featuredHTML = (() => {
 const name = featured.name || 'Aero-Silk Compression Sheath';
 const price = Number(featured.price) || 0;
 const image = getImageUrl(featured.mainImage || featured.image);
 const sub = featured.subcategory || 'Phase 01 / Core';
 const id = featured._id || '#';
 return `
 <div class="col-span-12 md:col-span-7 group cursor-pointer relative flex flex-col" onclick="window.location.href='product.html?id=${id}'">
 <div class="h-[800px] w-full border border-white/20 p-2 mb-6 relative overflow-hidden bg-[#1a1a1a]">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-all duration-1000" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 <div class="absolute inset-0 bg-black/40 backdrop-blur-sm opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-center justify-center">
 <span class="bg-white text-black text-[12px] font-bold tracking-widest uppercase px-8 py-4 border border-[#e9c349] hover:bg-[#e9c349] transition-colors" style="font-family:'Manrope',sans-serif;">Acquire</span>
 </div>
 </div>
 <div class="flex justify-between items-start pt-2">
 <div>
 <h3 class="text-[32px] font-semibold text-white leading-none mb-2" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">${sub}</p>
 </div>
 <span class="text-[18px] text-[#e9c349] font-bold" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 </div>
 </div>
 `;
 })();

 const stackedHTML = stacked.map(p => {
 const name = p.name || 'Performance Gear';
 const price = Number(p.price) || 0;
 const image = getImageUrl(p.mainImage || p.image);
 const sub = p.subcategory || 'Phase 01 / Core';
 return `
 <div class="group cursor-pointer relative flex flex-col flex-1" onclick="window.location.href='product.html?id=${p._id}'">
 <div class="flex-1 w-full border border-white/20 p-2 mb-6 relative overflow-hidden bg-[#1a1a1a] min-h-[350px]">
 <img class="w-full h-full object-cover opacity-90 group-hover:opacity-100 group-hover:scale-105 transition-all duration-1000 object-top" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 <div class="absolute inset-0 bg-black/40 backdrop-blur-sm opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-center justify-center">
 <span class="bg-white text-black text-[12px] font-bold tracking-widest uppercase px-6 py-3 border border-[#e9c349] hover:bg-[#e9c349] transition-colors" style="font-family:'Manrope',sans-serif;">Acquire</span>
 </div>
 </div>
 <div class="flex justify-between items-start pt-2 border-t border-white/20">
 <div>
 <h3 class="text-[24px] font-semibold text-white leading-none mb-1" style="font-family:'Noto Serif',serif;">${name}</h3>
 <p class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0]" style="font-family:'Manrope',sans-serif;">${sub}</p>
 </div>
 <span class="text-[18px] text-[#e9c349] font-bold" style="font-family:'Manrope',sans-serif;">&#8377;${price.toLocaleString('en-IN')}</span>
 </div>
 </div>
 `;
 }).join('');

 container.innerHTML = `
 <div class="fit-editorial-layout" style="background:#0a0a0a;">

 <!-- 1. HERO EDITORIAL SPREAD -->
 <section class="px-16 max-w-[1440px] mx-auto pt-16 mb-32">
 <div class="grid grid-cols-12 gap-8 items-center">
 <!-- Typography Left -->
 <div class="col-span-12 md:col-span-5 flex flex-col gap-8 pr-12 z-10">
 <div class="flex items-center gap-4">
 <div class="h-px w-12 bg-[#e9c349]"></div>
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#e9c349]" style="font-family:'Manrope',sans-serif;">The Fit Collection</span>
 </div>
 <h1 class="text-[80px] leading-[90px] tracking-tight font-bold text-white" style="font-family:'Noto Serif',serif;">Architecture<br/>of Motion.</h1>
 <p class="text-[18px] text-[#a0a0a0] max-w-md" style="font-family:'Manrope',sans-serif;">Engineered for the elite. Merging highly technical performance fabrics with the uncompromising precision of haute couture.</p>
 <div class="pt-8 border-t border-white/20 mt-4">
 <a class="inline-block bg-[#e9c349] text-black text-[12px] font-bold tracking-widest uppercase px-8 py-4 hover:bg-white hover:text-black transition-colors duration-300" href="#fit-collection" style="font-family:'Manrope',sans-serif;">
 Explore the Archive
 </a>
 </div>
 </div>
 <!-- Hero Image Right -->
 <div class="col-span-12 md:col-span-7 relative h-[716px] border border-white/20 p-4 group">
 <div class="absolute -bottom-6 -left-6 w-32 h-px bg-[#e9c349]"></div>
 <div class="absolute -top-6 -right-6 w-px h-32 bg-[#e9c349]"></div>
 <div class="w-full h-full relative overflow-hidden bg-[#1a1a1a]">
 <img
 class="w-full h-full object-cover opacity-80 transition-all duration-700 group-hover:scale-105 group-hover:opacity-100"
 src="https://lh3.googleusercontent.com/aida-public/AB6AXuDwP6f9HZIKO9ymSIAY8msQwrlPOOgteuPw1CpNFiTHylCtsdEhb2NGrq1wMliXUK54rVV9SLR6zmAl-B9N1wC240rxM1bkzM_x-5t72wl1CQvgSnWpPSy04ZgkJdCJqlVZe3xCjvxjp8gm79LTS2xEV_BDY1G4hSBnZRQXObkFjyqYIXfo49XH7jeW1WGsIFODAqG1vtAw1XvmBCmu7HNIfeMYeW-z-incE7hnkn6RD_wqhCgTdsPxmbJ0GdXcHkpu9mqRdYbg5Yu1"
 alt="Fit Hero"
 />
 </div>
 </div>
 </div>
 </section>

 <!-- 2. CATEGORY TAXONOMY CHIPS -->
 <section class="px-16 max-w-[1440px] mx-auto border-y border-white/20 py-6 mb-32">
 <div class="flex items-center justify-between">
 <h2 class="text-[32px] font-semibold text-white hidden md:block w-1/4" style="font-family:'Noto Serif',serif;">Divisions</h2>
 <div class="flex gap-12 overflow-x-auto w-full md:w-3/4 justify-start md:justify-end">
 <a class="text-[12px] font-bold tracking-widest uppercase text-black bg-white border border-white px-6 py-2 shrink-0 hover:bg-[#e9c349] hover:border-[#e9c349] transition-colors" href="#" style="font-family:'Manrope',sans-serif;">Compression</a>
 <a class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0] border border-transparent px-6 py-2 shrink-0 hover:border-white transition-colors" href="#" style="font-family:'Manrope',sans-serif;">Outerwear</a>
 <a class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0] border border-transparent px-6 py-2 shrink-0 hover:border-white transition-colors" href="#" style="font-family:'Manrope',sans-serif;">Base Layers</a>
 <a class="text-[12px] font-bold tracking-widest uppercase text-[#a0a0a0] border border-transparent px-6 py-2 shrink-0 hover:border-white transition-colors" href="#" style="font-family:'Manrope',sans-serif;">Recovery</a>
 </div>
 </div>
 </section>

 <!-- 3. BENTO PRODUCT GRID -->
 <section class="px-16 max-w-[1440px] mx-auto mb-32" id="fit-collection">
 <div class="flex justify-between items-end mb-16 border-b border-white/20 pb-4">
 <h2 class="text-[48px] font-semibold text-white" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">Core Index.</h2>
 <a class="text-[12px] font-bold tracking-widest uppercase text-white flex items-center gap-2 hover:text-[#e9c349] transition-colors" href="#" style="font-family:'Manrope',sans-serif;">
 View Complete Roster <span class="material-symbols-outlined" style="font-size:16px;">arrow_forward</span>
 </a>
 </div>
 <div class="grid grid-cols-12 gap-8">
 ${featuredHTML}
 <div class="col-span-12 md:col-span-5 flex flex-col gap-8">
 ${stackedHTML}
 </div>
 </div>
 </section>

 <!-- 4. EDITORIAL PHILOSOPHY STRIP -->
 <section class="border-y border-white/20 bg-black text-white overflow-hidden relative">
 <div class="absolute inset-0 opacity-10" style="background:radial-gradient(circle at center, #e9c349 0%, transparent 70%);"></div>
 <div class="px-16 max-w-[1440px] mx-auto py-32 grid grid-cols-12 gap-8 items-center relative z-10">
 <div class="col-span-12 md:col-span-5 md:col-start-2 flex flex-col gap-8">
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#e9c349]" style="font-family:'Manrope',sans-serif;">Design Philosophy</span>
 <blockquote class="text-[48px] leading-[56px] font-semibold text-white" style="font-family:'Noto Serif',serif;letter-spacing:-0.01em;">
 &ldquo;The architecture of the garment dictates the geometry of performance. We remove the superfluous to elevate the essential.&rdquo;
 </blockquote>
 <div class="flex items-center gap-4 mt-8">
 <div class="h-px w-16 bg-white"></div>
 <span class="text-[12px] font-bold tracking-widest uppercase text-[#c6c6c6]" style="font-family:'Manrope',sans-serif;">The Atelier</span>
 </div>
 </div>
 <div class="col-span-12 md:col-span-4 md:col-start-8 mt-16 md:mt-0 relative">
 <div class="aspect-[3/4] border border-[#e9c349] p-4 relative z-10 bg-black">
 <img
 class="w-full h-full object-cover opacity-80"
 src="https://lh3.googleusercontent.com/aida-public/AB6AXuAeARHcffXSn1l9vGfauVeZO1oJonbuKVE_Yg260Dk1b4nkJ8qW7wYmKHsdUtE86fQwiXmC64Nb1w9xrSVuGKhk2Ac8_nYrAR8ZZu_cWOituYJnhLZfFqEVXasJRtfQ4_2sUo1bjfHj6yhnvxazQnvj-kny_J4bWpn-b7II9MPr_twlk5iH8vMD_tPmxtbCOlMaCXhfzAS95bl7MSGjyDMKuIWgrLycfN_S3EISqyeRwW70zczocTZu8CQertH6BL95zx1bIQ6t7peG"
 alt="Detail"
 />
 </div>
 <div class="absolute top-8 -right-8 bottom-8 left-8 border border-white/30 z-0 pointer-events-none hidden md:block"></div>
 </div>
 </div>
 </section>

 <!-- 5. NEWSLETTER -->
 <section class="px-16 max-w-[1440px] mx-auto py-32 flex flex-col items-center text-center border-b border-white/20">
 <span class="material-symbols-outlined text-[#e9c349] text-4xl mb-6">workspace_premium</span>
 <h2 class="text-[32px] font-semibold text-white mb-4" style="font-family:'Noto Serif',serif;">Join the Inner Circle.</h2>
 <p class="text-[16px] text-[#a0a0a0] mb-12 max-w-lg" style="font-family:'Manrope',sans-serif;">Exclusive access to limited capsules, private events, and technical innovations.</p>
 <div class="w-full max-w-md flex flex-col gap-6">
 <div class="relative w-full">
 <input class="w-full bg-transparent border-0 border-b border-white/40 focus:outline-none focus:border-[#e9c349] px-0 py-2 text-[18px] text-white placeholder-[#dadada] transition-colors" placeholder="Enter your email" type="email" style="font-family:'Manrope',sans-serif;"/>
 </div>
 <button class="self-start mt-4 bg-white text-black text-[12px] font-bold tracking-widest uppercase px-8 py-3 hover:bg-[#e9c349] transition-colors duration-300" style="font-family:'Manrope',sans-serif;">
 Subscribe
 </button>
 </div>
 </section>

 <!-- 6. FIT FOOTER -->
 <footer class="bg-black w-full border-t-2 border-[#e9c349]">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-8 px-16 py-32 max-w-[1440px] mx-auto text-white">
 <div class="col-span-1 flex flex-col gap-6">
 <span class="text-[48px] font-semibold text-[#e9c349]" style="font-family:'Noto Serif',serif;">PantoMart</span>
 <p class="text-[16px] text-[#c6c6c6] max-w-xs" style="font-family:'Manrope',sans-serif;">Defining the intersection of avant-garde design and elite performance utility.</p>
 </div>
 <div class="col-span-1 md:col-span-2 flex justify-start">
 <ul class="flex flex-col gap-4" style="font-family:'Manrope',sans-serif;">
 <li><a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="about/index.html">The Atelier</a></li>
 <li><a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="#">Sustainability</a></li>
 <li><a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="#">Shipping &amp; Returns</a></li>
 <li><a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="contact/index.html">Contact</a></li>
 <li><a class="text-[16px] text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="privacy-policy/index.html">Privacy Policy</a></li>
 </ul>
 </div>
 <div class="col-span-1 flex flex-col justify-end items-start md:items-end gap-4" style="font-family:'Manrope',sans-serif;">
 <div class="flex gap-4">
 <a class="text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="#"><span class="material-symbols-outlined">public</span></a>
 <a class="text-[#c6c6c6] hover:text-[#e9c349] transition-colors" href="#"><span class="material-symbols-outlined">mail</span></a>
 </div>
 <span class="text-[14px] text-[#c6c6c6]">&copy; 2024 PantoMart. All rights reserved.</span>
 </div>
 </div>
 </footer>
 </div>
 `;

 document.body.style.background = '#0a0a0a';
}

function renderDefaultCategory(products, container) {
 container.innerHTML = `<div class="py-20 text-center" style="font-family:'Manrope',sans-serif;font-size:14px;color:#4c4546;letter-spacing:0.1em;">No products found for this category.</div>`;
}
// Note: initCategory() is called by api.js DOMContentLoaded handler — no duplicate listener needed here.