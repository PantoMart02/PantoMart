// ======================
// ✅ LOAD PRODUCT PAGE
// ======================
async function initProduct() {
 const params = new URLSearchParams(window.location.search);
 const productId = params.get("id");

 const container = document.getElementById("product-container");
 if (!container) return;

 // No ID
 if (!productId) {
 container.innerHTML = `
 <div style="text-align:center; padding:80px;">
 <h2>Product not found</h2>
 </div>`;
 return;
 }

 // Loading
 container.innerHTML = `
 <div style="text-align:center; padding:80px;">
 Loading product...
 </div>`;

 const product = await fetchProductById(productId);

 // Error
 if (!product || !product._id) {
 container.innerHTML = `
 <div style="text-align:center; padding:80px;">
 <h2>Product not found</h2>
 </div>`;
 return;
 }

 // Add category class to body for the premium styling system
 const wasDark = document.body.classList.contains('dark');
 document.body.className = ''; // reset
 document.body.classList.add('product-page', 'category-' + (product.category || 'default'));
 if (wasDark) document.body.classList.add('dark');

 // 🚀 Category-specific rendering
 const cat = (product.category || "").toLowerCase();
 
 const breadcrumb = document.getElementById('breadcrumb-container');
 if (breadcrumb && cat) {
   breadcrumb.classList.remove('hidden');
   document.getElementById('back-to-category').href = 'category.html?cat=' + cat;
   document.getElementById('category-name-display').innerText = cat;
 }

 if (cat === 'care') {
 renderCareProduct(product, container);
 } else if (cat === 'style') {
 renderStyleProduct(product, container);
 } else if (cat === 'fit') {
 renderFitProduct(product, container);
 } else if (cat === 'space') {
 renderSpaceProduct(product, container);
 } else if (cat === 'pet') {
 renderPetProduct(product, container);
 } else {
 renderDefaultProduct(product, container);
 }

 // Page title
 const brand = (product.category === 'care') ? 'PantoCure' : 'PantoMart';
 document.title = (product.name || "Product") + " | " + brand + " Luxury";
}

// ======================
// ✨ PANTOCURE (CARE) RENDERER
// ======================
function renderCareProduct(product, container) {
 const name = product.name || "Eternal Glow Serum";
 const price = Number(product.price) || 0;
 const image = getImageUrl(product.mainImage || product.image);
 const tagline = product.tagline || "Transformative luminosity and clear, hydrated skin through botanical precision.";
 const description = product.description || "A transformative elixir crafted with botanical precision.";
 const oldPrice = Math.round(price * 1.25);

 const benefits = product.benefits || [
 {title: "Glow", desc: "Instant luminosity that brightens dark spots and evens skin tone for a glass-like finish.", icon: "auto_awesome"},
 {title: "Hydration", desc: "72-hour moisture lock using multi-weight Hyaluronic molecules for deep cellular hydration.", icon: "water_drop"},
 {title: "Smoothness", desc: "Refines pore appearance and smooths fine lines with gentle botanical resurfacing agents.", icon: "blur_on"},
 {title: "Repair", desc: "Reinforces the skin barrier against environmental stressors and urban pollutants.", icon: "health_and_safety"}
 ];

 const ingredients = product.ingredients || [
 {name: "Hyaluronic Acid", desc: "Binds moisture to the skin, holding 1,000 times its weight in water for plump, bouncy texture.", icon: "opacity", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuB9v0qEIXUctfEv_E4_SzS0pg9xjpxvNW4GjETv4M9kisGY1sENKHIJyxky1dk2RQ5ULOd-4MvbUv2UHkOduB5dibHbR299FkGDkWolk9yG572EMs1Srlzj8DSGIl0CU4ycHewyh8oEWqULwI4kCa96Q7i6Q6Byr1uG8QUeYtVJ7w7NuJSyWPUpzP0pZrDXxM5H1MjDoX4sdqsF-5CrqRK7iXRWBCYqQwrIULT18g5JRwoA5hGxrVvWeAgjMXtizoq-n-e-BZOOYKQ5"},
 {name: "Stabilized Vitamin C", desc: "A potent antioxidant that combats free radicals while visibly brightening hyperpigmentation.", icon: "biotech", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuAJwgvdidsUp4-0MrsL7u-V6XKLM1CAXqRmQAbFk5K5329AfCGWKZVM6ATcgpaJcJUVXcX_YHlsWnQkKFyHijiKhnEy7ot9eDoWPdI5M7slW-PGO1SzZvf5m3HNozh3e9_LIYVg3ETM2RcNureurJdd12XmwCVHeDf3GuIiKxHb5yBeF9rNAO5-lA_C89vSM5Y5VJvKqVSyvlXb05ixjVjrmaelmHeDi8jpMGgrCpjW9rHSCQbR75zQT82ueQeYY6oJ8KaptsVqZskd"}
 ];

 const ritualSteps = product.ritual || [
 {step: "Cleanse", desc: "Prepare with a gentle, pH-balanced cleanser.", icon: "cleaning_services"},
 {step: "Apply", desc: "Press 3-4 drops gently into the damp skin.", icon: "opacity"},
 {step: "Massage", desc: "Use upward circular motions for absorption.", icon: "self_improvement"},
 {step: "Repeat", desc: "Morning and night for optimal luminosity.", icon: "refresh"}
 ];

 const reviews = (product.reviews && product.reviews.length > 0) ? product.reviews : [
 {name: "Elena R.", quote: "The 'glow' isn't just a marketing claim—it's visible within days. My skin feels like silk.", role: "Verified Collector", stars: 5},
 {name: "James T.", quote: "Heavenly texture. It absorbs instantly without any residue, making it perfect under makeup.", role: "MUA", stars: 5},
 {name: "Sarah L.", quote: "Finally a serum that actually addresses dullness without irritation. It's my daily staple.", role: "Beauty Editor", stars: 5}
 ];

 const faqs = product.faqs || [
 {q: "Is this serum suitable for sensitive skin?", a: "Yes, our formula is dermatologist-tested and specifically designed with soothing botanical extracts like chamomile to minimize irritation while delivering potent results."},
 {q: "When will I see visible results?", a: "While immediate hydration is felt after the first use, 98% of users report a visible increase in radiance and more even skin tone within 21 days of consistent twice-daily application."},
 {q: "Can I use this serum with other products?", a: "Absolutely. Eternal Glow Serum is designed to be the core of your routine. It layers perfectly under heavier creams, sunscreen, and foundation without pilling."},
 {q: "Is the packaging recyclable?", a: "Yes, our glass vessels are 100% recyclable. We encourage you to rinse the bottle after use and dispose of it in your local glass recycling bin."}
 ];

 // Remove previous body styles to prevent bleeding from other categories
 document.body.style.backgroundImage = "";
 document.body.style.backgroundAttachment = "";
 document.body.style.backgroundPosition = "";
 document.body.style.backgroundSize = "";

 container.innerHTML = `
 

 <!-- Sticky Mobile CTA -->
 <div class="md:hidden mobile-cta-sticky">
 <button class="buy-btn flex-1 px-4 py-3 bg-white border border-primary text-primary text-label-sm uppercase tracking-widest font-bold"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Add to Cart</button>
 <button class="flex-1 px-4 py-3 bg-primary text-white text-label-sm uppercase tracking-widest font-bold">Buy Now</button>
 </div>

 <main class="mt-24 flex flex-col max-w-container-max mx-auto px-margin-page">
 <!-- 1. HERO SECTION -->
 <section class="section-box">
 <div class="section-header">
 <span>The Product</span>
 <span class="material-symbols-outlined text-sm">auto_awesome</span>
 </div>
 <div class="flex flex-col md:flex-row items-center p-8 md:p-16 gap-16 w-full bg-gradient-to-br from-surface/50 to-tertiary-fixed/20">
 <div class="relative w-full md:w-1/2 aspect-[4/5] overflow-hidden rounded-lg shadow-sm">
 <img alt="${name}" class="w-full h-full object-cover shadow-2xl" src="${image}"/>
 </div>
 <div class="flex flex-col gap-8 w-full md:w-1/2">
 <div class="space-y-4">
 <span class="text-label-sm font-label-sm uppercase tracking-widest text-on-surface-variant">Care / Face Serum</span>
 <h1 class="text-display-xl font-display-xl text-primary leading-tight">${name}</h1>
 <h2 class="text-headline-md font-headline-md text-on-surface-variant italic">${tagline}</h2>
 </div>
 <div class="flex items-baseline gap-4">
 <span class="text-display-xl font-display-xl">₹${price.toLocaleString('en-IN')}</span>
 <span class="text-body-lg font-body-lg text-on-surface-variant line-through">₹${oldPrice.toLocaleString('en-IN')}</span>
 </div>
 <div class="flex items-center gap-2 text-on-surface-variant">
 <span class="material-symbols-outlined text-sm" data-icon="verified">verified</span>
 <p class="text-body-md">98% report visible radiance and clear skin within 21 days.</p>
 </div>
 <div class="hidden md:flex gap-4">
 <button class="buy-btn flex-1 py-5 border border-primary text-primary font-label-sm uppercase tracking-widest hover:bg-primary-fixed transition-all duration-300"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Add to Cart</button>
 <button class="flex-1 py-5 bg-primary text-on-primary font-label-sm uppercase tracking-widest hover:bg-on-surface-variant transition-all duration-300 shadow-lg">Buy Now</button>
 </div>
 </div>
 </div>
 </section>

 <!-- 2. IMAGE GALLERY -->
 <section class="section-box">
 <div class="section-header">
 <span>The Visual Journey</span>
 <span class="material-symbols-outlined text-sm">visibility</span>
 </div>
 <div class="bg-surface/60 py-12 px-8">
 <h3 class="text-label-sm uppercase tracking-widest text-center mb-12">Detailed Perspectives</h3>
 <div class="flex overflow-x-auto gap-gutter pb-8 snap-x-mandatory scrollbar-hide md:grid md:grid-cols-4 md:overflow-visible">
 <div class="min-w-[80%] md:min-w-0 snap-center rounded-lg overflow-hidden border border-outline-variant/30 bg-surface-container-lowest">
 <img alt="Texture" class="w-full aspect-square object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCsp2jAgRUiL0FDSs5yu7Ftrnhr28pCHUymZiriabz9VAhdVDVJZ5j5t_0WSVsSbCG5uJOXFRUGuMt-BR-uiHD_tiGGBu0MMO67O0whwGKdJWodwJkSPizGNSlHBZk0C2jTwV2GLXgwwgbML3G0jtmJ5XvavEgiSHzE5sj7j7aDeIFN1VJZAQ2BEpxgWwvbK46V6OCfIvYJ7DPBP8MS1HuLwKFpNGmqZ9pohgp0TspXTYfnbbT8dL3qJt3yTo2NL_vp2yI-wKsBd_2Z"/>
 <p class="p-4 text-label-sm uppercase text-on-surface-variant text-center">Silky Texture</p>
 </div>
 <div class="min-w-[80%] md:min-w-0 snap-center rounded-lg overflow-hidden border border-outline-variant/30 bg-surface-container-lowest">
 <img alt="Packaging" class="w-full aspect-square object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBzKE5jUB5QabElnyeBmnMmtX-FfTY41BOqp8tuwP5IRZM3_6yTTs3w0pvtjzx6ZfTTRfhPoz-MXMAUKqN8eUfsO9z4A_aWJhJEMJsMa11gZp9ztIFfE_gwcbbf_sk8VDwM-g2_wl_JBTacNCmKvMMcWow3mEVfZ6ngtxheDr8s-r9G48A4CQHBRTXdHCkOeMJTCM96JzBvvWlYmLenzJB8G6rCyIMmA5bcKJ4Na1AOiCIrSXBXfsz44Bv_IlgPpMHG1ofMH3AqtOO9"/>
 <p class="p-4 text-label-sm uppercase text-on-surface-variant text-center">Elegant Vessel</p>
 </div>
 <div class="min-w-[80%] md:min-w-0 snap-center rounded-lg overflow-hidden border border-outline-variant/30 bg-surface-container-lowest">
 <img alt="Ingredients" class="w-full aspect-square object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDylJ7WBfhuG1JMlFnNiu7O2I1cURd4EsGPbWSccMwUf9c0rzGF1-J-nR7W-buxp3_0_O4qfOhyrlE6eQLAnKaZjuiIIVVm_Qx3lp2-sEmRqPEthLS65tjOrNL0PfJ7RxMp49ELW2HkxVo-0dhj4EecrvwHSpfLSfE1_-JjjUYzvIEW-Uv2sWJK_uyOAjxY3YoNOsB6WNQG4Ummp4d8CxB35cisMBGFjLY4WOrDOqQ1iutm-wBqSMTbyw8yedjj7uP6kZ4IB8PgDFXJ"/>
 <p class="p-4 text-label-sm uppercase text-on-surface-variant text-center">Pure Potency</p>
 </div>
 <div class="min-w-[80%] md:min-w-0 snap-center rounded-lg overflow-hidden border border-outline-variant/30 bg-surface-container-lowest">
 <img alt="Results" class="w-full aspect-square object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDB-HkyPkP2fP4jYNA_qGEIdS3uCXntw0FU-6pGe1UMP7U8IO0Mns4mTZ5mkaH9DwQe2T58eC1SZTGvfTxrg4jFG-EDmjJYS-P-DL7oIwzjGbWSERUK9ydzV_fM7rnMGbQ42qKa8N0xtBMrmbTszwWZ_7Ubgkr0oBD09NGejLJnBa44XevAFreBG-u-hI6ocJzn1PONMZ-c_yQJgBZiyhWz-2sOC3Rk8H9dwtiTU6aSDhk7ThHqecg5174hi-gISuifmfkDouQLRjt5"/>
 <p class="p-4 text-label-sm uppercase text-on-surface-variant text-center">21-Day Glow</p>
 </div>
 </div>
 </div>
 </section>

 <!-- 3. PROBLEM -> RESULT -->
 <section class="section-box">
 <div class="section-header">
 <span>The Luminosity Transformation</span>
 <span class="material-symbols-outlined text-sm">compare</span>
 </div>
 <div class="bg-background/40 py-16 px-8">
 <h3 class="text-headline-lg font-headline-lg text-center mb-16">Clinical Observations</h3>
 <div class="flex flex-col md:flex-row items-center justify-center gap-8 md:gap-20">
 <div class="w-full md:w-[400px] text-center">
 <div class="relative mb-6 rounded-xl overflow-hidden shadow-sm aspect-square border border-outline-variant/30">
 <img alt="Before" class="w-full h-full object-cover " src="https://lh3.googleusercontent.com/aida-public/AB6AXuA7hnAm1aGl5aSYW_b_mwUbrXJKQXtq8eCygVSTIGy9-ycBEQetH__PlOW1QcYIIGbV1CKnWKV_6QDmsPUq-b-4aDai8YFvNHilwpn5yJle5H9fgbwmJ0eGLs7IQGmp3N1EWzT0nIKbecIB9lVDAPAB-uEYwRwAKqGjWw9tm9x_JrTa5JoZXulf8RWBIWvyAyzmnupcW3fo7fshX1I8mNM_Kwme3DQkq1IAmECyLMbKrJYXNGrMBF3igym5oVRV5Rc1m1YxL-sJYJJo"/>
 <span class="absolute top-4 left-4 bg-white/90 px-3 py-1 text-label-sm">DAY 01</span>
 </div>
 <h4 class="text-headline-md font-headline-md">Dull & Dehydrated</h4>
 <p class="text-body-md text-on-surface-variant mt-2">Compromised barrier and uneven tone.</p>
 </div>
 <div class="flex">
 <span class="material-symbols-outlined text-4xl text-outline-variant hidden md:block" data-icon="east">east</span>
 <span class="material-symbols-outlined text-4xl text-outline-variant md:hidden" data-icon="south">south</span>
 </div>
 <div class="w-full md:w-[400px] text-center">
 <div class="relative mb-6 rounded-xl overflow-hidden shadow-lg border-2 border-primary aspect-square">
 <img alt="After" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDB-HkyPkP2fP4jYNA_qGEIdS3uCXntw0FU-6pGe1UMP7U8IO0Mns4mTZ5mkaH9DwQe2T58eC1SZTGvfTxrg4jFG-EDmjJYS-P-DL7oIwzjGbWSERUK9ydzV_fM7rnMGbQ42qKa8N0xtBMrmbTszwWZ_7Ubgkr0oBD09NGejLJnBa44XevAFreBG-u-hI6ocJzn1PONMZ-c_yQJgBZiyhWz-2sOC3Rk8H9dwtiTU6aSDhk7ThHqecg5174hi-gISuifmfkDouQLRjt5"/>
 <span class="absolute top-4 left-4 bg-primary text-white px-3 py-1 text-label-sm">DAY 21</span>
 </div>
 <h4 class="text-headline-md font-headline-md">The Eternal Glow</h4>
 <p class="text-body-md text-on-surface-variant mt-2">Deeply hydrated, radiant complexion.</p>
 </div>
 </div>
 </div>
 </section>

 <!-- 4. BENEFITS -->
 <section class="section-box">
 <div class="section-header">
 <span>Core Benefits</span>
 <span class="material-symbols-outlined text-sm">verified_user</span>
 </div>
 <div class="bg-surface-container/60 py-16 px-8">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-gutter">
 ${benefits.map((b) => `
 <div class="p-8 bg-white/80 backdrop-blur-sm rounded-xl flex flex-col gap-4 border border-outline-variant/30 hover:border-primary transition-all shadow-sm">
 <span class="material-symbols-outlined text-3xl text-primary" data-icon="${b.icon}">${b.icon}</span>
 <h4 class="text-headline-md font-headline-md">${b.title}</h4>
 <p class="text-body-md text-on-surface-variant">${b.desc}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 5. INGREDIENTS -->
 <section class="section-box">
 <div class="section-header">
 <span>Purely Formulated</span>
 <span class="material-symbols-outlined text-sm">science</span>
 </div>
 <div class="bg-background/40 py-16 px-8">
 <h3 class="text-headline-lg font-headline-lg text-center mb-16">Key Actives</h3>
 <div class="grid md:grid-cols-2 gap-gutter">
 ${ingredients.map((ing) => `
 <div class="flex items-center gap-8 p-8 bg-white/70 backdrop-blur-sm rounded-2xl border border-outline-variant/20 group transition-colors hover:bg-white hover:border-outline-variant/40">
 <div class="w-32 h-32 flex-shrink-0 rounded-full overflow-hidden shadow-inner border-2 border-white">
 <img alt="${ing.name}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" src="${ing.img || image}"/>
 </div>
 <div>
 <h5 class="text-headline-md font-headline-md mb-2">${ing.name}</h5>
 <p class="text-body-md text-on-surface-variant">${ing.desc}</p>
 </div>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 6. HOW TO USE -->
 <section class="section-box">
 <div class="section-header">
 <span>The Ritual</span>
 <span class="material-symbols-outlined text-sm">self_improvement</span>
 </div>
 <div class="bg-surface/60 py-16 px-8">
 <h3 class="text-display-xl font-display-xl text-center mb-4">Application Method</h3>
 <p class="text-center text-body-lg text-on-surface-variant mb-16">Four steps to absolute radiance.</p>
 <div class="grid grid-cols-1 md:grid-cols-4 gap-12">
 ${ritualSteps.map((r, i) => `
 <div class="flex flex-col items-center text-center">
 <div class="w-16 h-16 rounded-full border border-primary flex items-center justify-center text-headline-md font-headline-md mb-6 relative bg-white">
 0${i + 1}
 <span class="material-symbols-outlined absolute -top-2 -right-2 bg-background p-1 text-base text-primary" data-icon="${r.icon}">${r.icon}</span>
 </div>
 <h6 class="text-headline-md font-headline-md mb-2">${r.step}</h6>
 <p class="text-body-md text-on-surface-variant">${r.desc}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 7. SOCIAL PROOF -->
 <section class="section-box">
 <div class="section-header">
 <span>Voices of Radiance</span>
 <span class="material-symbols-outlined text-sm">chat_bubble</span>
 </div>
 <div class="bg-background/40 py-16 px-8">
 <h3 class="text-headline-lg font-headline-lg text-center mb-16">Customer Testimonials</h3>
 <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
 ${reviews.map((r) => `
 <div class="bg-white/90 backdrop-blur-sm p-10 border border-outline-variant/30 shadow-sm flex flex-col gap-6 rounded-lg hover:border-primary transition-colors">
 <div class="flex gap-1">
 ${Array(5).fill(0).map((_, idx) => `<span class="material-symbols-outlined text-primary" data-icon="star" style="font-variation-settings: 'FILL' ${idx < (r.stars || 5) ? 1 : 0};">star</span>`).join('')}
 </div>
 <p class="italic text-body-lg font-body-lg">"${r.quote || r.q}"</p>
 <div class="flex items-center gap-4 mt-auto">
 <div class="w-12 h-12 rounded-full bg-secondary-fixed"></div>
 <div>
 <p class="font-bold text-on-surface">${r.name}</p>
 <p class="text-label-sm font-label-sm text-on-surface-variant">${r.role || 'Verified Radiant User'}</p>
 </div>
 </div>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 8. SAFETY/TRUST STRIP (Purity Promise) -->
 <section class="section-box">
 <div class="section-header">
 <span>Purity Promise</span>
 <span class="material-symbols-outlined text-sm">eco</span>
 </div>
 <div class="bg-surface-container/60 py-8 px-8 flex flex-wrap justify-center md:justify-between items-center gap-8">
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-xl" data-icon="done_all">done_all</span>
 <span class="text-label-sm uppercase tracking-widest">All Skin Types</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-xl" data-icon="eco">eco</span>
 <span class="text-label-sm uppercase tracking-widest">No Harmful Chemicals</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-xl" data-icon="cruelty_free">cruelty_free</span>
 <span class="text-label-sm uppercase tracking-widest">Cruelty Free & Vegan</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-xl" data-icon="science">science</span>
 <span class="text-label-sm uppercase tracking-widest">Dermatologist Inspired</span>
 </div>
 </div>
 </section>

 <!-- FAQ SECTION -->
 <section class="section-box">
 <div class="section-header">
 <span>Frequently Asked Questions</span>
 <span class="material-symbols-outlined text-sm">help_outline</span>
 </div>
 <div class="bg-white/70 py-16 px-8">
 <div class="max-w-3xl mx-auto space-y-6">
 ${faqs.map((faq, index) => `
 <div class="${index === faqs.length - 1 ? 'pb-6' : 'border-b border-outline-variant/30 pb-6'}">
 <h4 class="text-headline-md font-headline-md mb-3 flex items-center justify-between cursor-pointer group">
 ${faq.q}
 <span class="material-symbols-outlined text-primary group-hover:translate-x-1 transition-transform" data-icon="add">add</span>
 </h4>
 <p class="text-body-md text-on-surface-variant">${faq.a}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 9. FINAL CTA -->
 <section class="section-box">
 <div class="section-header">
 <span>Final CTA</span>
 <span class="material-symbols-outlined text-sm">shopping_bag</span>
 </div>
 <div class="bg-background/60 py-16 px-8 text-center">
 <h3 class="text-display-xl font-display-xl mb-6">Get Your Glow</h3>
 <p class="text-body-lg text-on-surface-variant mb-12 max-w-2xl mx-auto">Reveal clear skin today. Experience the culmination of skincare science and luxury. Your most radiant skin is just a bottle away.</p>
 <div class="flex flex-col md:flex-row justify-center gap-4">
 <button class="buy-btn px-16 py-5 bg-primary text-white font-label-sm uppercase tracking-widest hover:bg-on-surface-variant transition-all duration-300"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Order Now</button>
 <button class="px-16 py-5 border border-primary text-primary font-label-sm uppercase tracking-widest hover:bg-primary-fixed transition-all duration-300">Discover More</button>
 </div>
 <p class="mt-8 text-label-sm text-on-surface-variant uppercase tracking-tighter">Free global shipping on orders over ₹2,500</p>
 </div>
 </section>
 </main>
 `;

 setupProductButtons(product, name, price, image);
}

// ======================
// 👔 FASHION (STYLE) RENDERER
// ======================
function renderStyleProduct(product, container) {
 const name = product.name || "Architectural Blazer";
 const price = Number(product.price) || 1250;
 const description = product.description || "An ode to timeless craftsmanship. Our signature tailored piece draped to perfection.";
 const image = getImageUrl(product.mainImage || product.image);
 const tagline = product.tagline || "The Silence of Quality";
 
 // Data extraction with fallbacks
 const benefits = product.benefits || [
 {title: "The Look", desc: "Sharp, geometric lines that redefine the modern silhouette for maximum visual impact.", icon: "visibility"},
 {title: "Comfort", desc: "Lined with 100% Italian silk, providing a breathable, second-skin feeling all day long.", icon: "cloud"},
 {title: "The Fit", desc: "Bespoke-level tailoring that contours to the body while maintaining its rigid, iconic shape.", icon: "straighten"},
 {title: "Versatility", desc: "Seamlessly transitions from high-stakes boardroom meetings to exclusive evening events.", icon: "all_inclusive"}
 ];
 
 const material = product.materialText || "Every fiber is chosen for its ability to hold form while providing an unmatched tactile experience. We don't just use fabric; we use heritage.";
 
 const styling = product.howToStyle || [
 {label: "The Casual Edge", desc: "Paired with raw denim and a crisp white tee for weekend sophistication. Effortless luxury.", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuDNGVFN7ts5FsaAi1ruwhDLg8j8TcvV7wvF64dllE_Kp3-MdsM3KNXyDabV0YdN6HwNEpiuflWH1JHsFnn0aq8QHtejYnezKhJp-VUWr1WyJEE1xZd4XbUKPOOR5NjPDubEvyg1cHCzjKn057N0xWA3wts8CaROwxPLv7aFF4wWVuYaVU4psL2qMKDpt4z78Ec9CIeL_GuJzbKpZ0c2sfih_H48VTWtMB1uSJlcCfKhPzHKlIXnFD464TVNkBxoSPEEu0_5F97AM_wi"},
 {label: "The Formal Standard", desc: "Full monochrome with matching tailored trousers and leather oxfords. The ultimate power suit.", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuBJzUYo6G3H3DZpT_LJnUjjjbk9ZiRPU8Q40FRfHwWqzJ4fytLd_762wRzRe5yRSMkfSIxo1zNHnrJ8ffqNCjmbDrk8pPhv6TnDIeFdaPY_M9H0PM1fpG_rZkmdXi6-5C0x-izomjjr4oYf4Fzs8K8NXgzWa9s3yp_DTVLC3EBq3FVD9TFe-qkFuXqlyVkgaKntzxlm_m-725uR31wtdL8ymfDFvYjy-UemHqTMHdVf183TFHaJG7EmEtEiB_Tgy4QIaLV3tFXNl_RB"},
 {label: "The Premium Gala", desc: "Draped over a silk slip dress for an evening of understated opulence. Captivating and refined.", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuBrXBPgBtzz3BLknaYn3Qc0EVCNnyGTGAhdFLzYpdjPbfn6z7IMK0aWMCTLD8jnGB1N7Loe5mgTA4p6Wa_DiQ0QuR6QgYJYC-RsiCIcbxSXo9h9mEu5CRx3YnKm-HC8Odz6_4Ixsmt8l1Y8wm63jsiTJkrLQKSpdECJ3tKqoGIy9Jy996-4uT1IpPUGbtq80dm1zXomA_78-urmxzDYzLKiq8wfhsKmcOyRtM9-rV725xXBLR7KlUhPcY_Pf2Vm-m7Xk4l5PYY7VIly"}
 ];

 const reviews = product.reviews && product.reviews.length > 0 ? product.reviews : [
 {name: "Eleanor V.", quote: "I have never worn a piece that commands such immediate respect. The tailoring on the shoulders is architectural perfection. I received more compliments in one night than I have in an entire year. It builds instant confidence.", role: "Verified Collector", stars: 5},
 {name: "Julian M.", quote: "The weight of the fabric is substantial yet comfortable. It feels like wearing armor. It changed the way I walk and the way I carry myself in the boardroom. A true masterpiece of modern authority.", role: "Executive Partner", stars: 5}
 ];

 const faqs = product.faqs || [
 {q: "How do I determine my correct size?", a: "Our Architectural Blazer is true-to-size with a structured silhouette. We recommend taking your standard tailoring size. If you prefer a more relaxed fit through the shoulders, consider sizing up one increment. Our concierge is available for detailed measurements."},
 {q: "What is the recommended care for this piece?", a: "To maintain the sharp lines and integrity of the wool-silk blend, professional dry clean only. We recommend seasonal cleaning and hanging on the provided contoured wide-shoulder hanger to preserve its internal structure."},
 {q: "Can the blazer be tailored further?", a: "Yes. We have left generous seam allowances at the waist and sleeves to accommodate custom tailoring. However, we do not recommend altering the shoulder construction as it is integral to the architectural design."},
 {q: "What is your return policy for limited editions?", a: "We offer a 14-day return window for all items. The blazer must be returned in its original condition with all security tags intact and in the original premium packaging. Returns are complimentary for our domestic collectors."}
 ];

 // Apply specific tailwind config for Style Boutique if possible
 

 // Remove Care background styling to ensure cleanliness
 document.body.style.backgroundImage = "";
 document.body.style.backgroundAttachment = "";
 document.body.style.backgroundPosition = "";
 document.body.style.backgroundSize = "";

 container.innerHTML = `
 

 <div class="fixed-bg"></div>
 
 <main class="pt-[64px] space-y-12 px-4 md:px-margin-page pb-12 relative z-10 bg-background text-on-surface font-body-md overflow-x-hidden">
 <!-- 1. HERO SECTION -->
 <section class="relative border border-primary/20 bg-surface/90 mt-12 backdrop-blur-sm">
 <div class="section-label">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">01 / The Presentation</span>
 </div>
 <div class="min-h-screen flex flex-col md:flex-row">
 <div class="w-full md:w-1/2 h-[614px] md:h-screen sticky top-[64px] overflow-hidden border-r border-outline-variant/20">
 <img alt="${name}" class="w-full h-full object-cover" src="${image}"/>
 </div>
 <div class="w-full md:w-1/2 flex flex-col justify-center px-12 py-section-padding space-y-gutter">
 <div class="space-y-unit-base">
 <span class="text-label-sm font-label-sm uppercase tracking-widest text-on-surface-variant">Style / Outerwear</span>
 <h1 class="text-display-xl font-display-xl text-primary">${name}</h1>
 <p class="text-headline-md font-headline-md italic text-on-surface-variant">"${tagline}"</p>
 </div>
 <div class="text-headline-lg font-headline-lg text-primary">₹${price.toLocaleString('en-IN')}</div>
 <div class="space-y-4">
 <label class="text-label-sm font-label-sm uppercase">Select Size</label>
 <div class="flex gap-4">
 <button class="w-12 h-12 flex items-center justify-center border border-outline hover:border-primary transition-colors text-body-md">XS</button>
 <button class="w-12 h-12 flex items-center justify-center border border-primary bg-primary text-on-primary text-body-md">S</button>
 <button class="w-12 h-12 flex items-center justify-center border border-outline hover:border-primary transition-colors text-body-md">M</button>
 <button class="w-12 h-12 flex items-center justify-center border border-outline hover:border-primary transition-colors text-body-md">L</button>
 </div>
 </div>
 <div class="flex flex-col gap-4 pt-4">
 <button class="buy-btn w-full py-4 border border-primary text-primary font-headline-md hover:bg-primary hover:text-on-primary transition-all duration-300"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Add to Cart</button>
 <button class="w-full py-4 bg-primary text-on-primary font-headline-md hover:opacity-90 transition-opacity">Buy Now</button>
 </div>
 <div class="grid grid-cols-2 gap-gutter pt-8 border-t border-outline-variant/30">
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-secondary" data-icon="verified" style="font-variation-settings: 'FILL' 1;">verified</span>
 <span class="text-label-sm font-label-sm uppercase">Premium Quality</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-secondary" data-icon="release_alert" style="font-variation-settings: 'FILL' 1;">release_alert</span>
 <span class="text-label-sm font-label-sm uppercase">Limited Release</span>
 </div>
 </div>
 </div>
 </div>
 </section>

 <!-- 2. IMAGE GALLERY -->
 <section class="relative border border-primary/20 bg-surface-container-low/80 py-section-padding backdrop-blur-sm">
 <div class="section-label">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">02 / Detail Gallery</span>
 </div>
 <div class="px-12 mb-gutter">
 <h2 class="text-headline-md font-headline-md uppercase tracking-tighter">Perspective Studies</h2>
 </div>
 <div class="flex overflow-x-auto gap-gutter px-12 pb-8 custom-scrollbar snap-x snap-mandatory">
 <div class="min-w-[350px] aspect-[3/4] snap-center border border-outline-variant/30 overflow-hidden bg-surface">
 <img alt="Lifestyle shot" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDeM_sWSzL5Sx-UiT9Ag-XNfT3wl-D5K22K2xRREqEFzalsjssL8lQmiTzLZovPLsRP8TBYn8c6xV-pyiAagmxJ0Lox7KEVYLLgh65Tnubxy-jaPQfLlbw_oNmmF7P9pPUg_VRILZDDFnR9xllELYFK-wTB7lbG702EYJo9b8gw2CmPvG9UNQqrt1MO0JFbgMaIkkbrCU0atLrdJBDlbNRnnAnaS8LPG5yXOm_Evv6m7bxQ7pCyL8q4FB3sWPWu59Bd2cbvbjm40Tt1"/>
 </div>
 <div class="min-w-[350px] aspect-[3/4] snap-center border border-outline-variant/30 overflow-hidden bg-surface">
 <img alt="Fabric close-up" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDL9u7Ns9nMwsJ4LsO9sk5_nr01M3iH4VFs3IrZFB9S-Nc8LvJ5N5S2swtHrRmYeomnSl1r0ll4e4T72069yL0vize-NZC5bajT2QuRpcLGBqOYL7YsMHJ4uSd0QgSmHhHBZ2N7zdDheSKgSDuHNexUyaX2Epn9hjBi0MXSptvugJzsmus3r3cUKySE0OndFE2VHNs3hPsBmwlHC0JJHVRBCQ8FXfLR4D8TkLVYJ8ZrUtE440bl6LSdhJv4Bvz0dc4kvXrgYN18WUI4"/>
 </div>
 <div class="min-w-[350px] aspect-[3/4] snap-center border border-outline-variant/30 overflow-hidden bg-surface">
 <img alt="Side profile" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA0yapiM1KD--ZdFPmZhJKS7rrTyicyjv1fcCudCyK4QjT8XtdttlGUCbcsPFAkb-i3kS8Z5JcAIsUAs8_Cp6YwSS_bJDBbfY3tYWscpppYfzq263PUhnIuAiF56gX0AUwfLH0vhsxW8PqQw3_xzNr46yHy2KJ0w_vVYgY6fDCbPpk8hIOmPBYHKn3N8CIfDoUGxjvUuJldECFASZoPFdg5xcUX3rAfidmx-KVCEdtMFE0_irx-83ob2nfbEG9HV8zLGBO5U-HR7KNF"/>
 </div>
 <div class="min-w-[350px] aspect-[3/4] snap-center border border-outline-variant/30 overflow-hidden bg-surface">
 <img alt="Back detail" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCzswHDSS6U96hLoaRiqcPBaNiwf_5gcK2qo_zsfwR1a6NQpkKMgTnR89kC8n79VGbF33lpfKwrnL6C-IFiZLc6EVi58V5u9F3uwQOLhKaVx4FXdp0RC2_B_1pXDvqtKoEu6dYeadXG9eiOfmOsDgQZ6nJp4MRuouxfNB6gd2iZO4H8MEj8Ux6zreFnF_pD-CIy4miH0Lx2Ld-JA6a6j4kEBJ25kgDxTUB1vg0eSxBsKFASQL5TWmgPVWyDZoWsgkr5_vzVdWvc70ZO"/>
 </div>
 </div>
 </section>

 <!-- 3. BRAND ETHOS SECTION -->
 <section class="relative border border-primary bg-primary text-on-primary py-section-padding">
 <div class="section-label bg-primary">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-on-primary">03 / Brand Ethos</span>
 </div>
 <div class="max-w-container-max mx-auto px-12 text-center">
 <h2 class="text-display-xl font-display-xl max-w-4xl mx-auto leading-tight">True Presence is felt long before a single word is spoken. Confidence, Attraction, Authority.</h2>
 </div>
 </section>

 <!-- 4. KEY BENEFITS SECTION -->
 <section class="relative border border-primary/20 bg-surface/90 py-section-padding backdrop-blur-sm">
 <div class="section-label">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">04 / Key Benefits</span>
 </div>
 <div class="max-w-container-max mx-auto px-12">
 <div class="grid grid-cols-1 md:grid-cols-4 gap-gutter">
 ${benefits.map((b) => `
 <div class="p-8 border border-outline-variant/30 flex flex-col gap-4 bg-surface-container-lowest/90 hover:border-primary transition-colors">
 <span class="material-symbols-outlined text-primary text-4xl" data-icon="${b.icon}">${b.icon}</span>
 <h3 class="text-headline-md font-headline-md">${b.title}</h3>
 <p class="text-on-surface-variant">${b.desc}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 5. MATERIAL EXCELLENCE SECTION -->
 <section class="relative border border-primary/20 bg-surface-container-highest/90 py-section-padding backdrop-blur-sm">
 <div class="section-label bg-surface-container-highest">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">05 / Material Excellence</span>
 </div>
 <div class="max-w-container-max mx-auto px-12">
 <div class="grid grid-cols-1 md:grid-cols-2 items-center gap-section-padding">
 <div class="relative group">
 <div class="p-4 border border-outline-variant/30 bg-surface inline-block">
 <img alt="Material texture" class="w-full aspect-[4/3] object-cover rounded shadow-2xl" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAva5fTqMjlZHBcRLyh3RUEP03YkvahEVRXFlzTQDLrqMi1G-J0CKrC_Cn4ChAmyPlIeCRBRxrtArsBO7m9Q3L2ADkyyaZuDgPVqckdzFS8cOhoR-brlKfOYy7qNil0y5Wg4bulhyM5iwYPNUkhthuaED1YT7f5_B8GeuoWMnUIXJeoaOHTlaCD1NbWrlbS6FppqIQ9bWKBAQ5Yd5Sh7ylJzmXV99As9thJkYqV-1gmth9jT7hyvHSKzSh5V-GDs5AxokRp9Y4MHArr"/>
 </div>
 <div class="absolute -bottom-6 -right-6 bg-primary text-on-primary p-8 hidden md:block border border-accent-gold/20 shadow-xl">
 <p class="text-display-xl font-display-xl">100%</p>
 <p class="text-label-sm uppercase tracking-widest">Italian Craftsmanship</p>
 </div>
 </div>
 <div class="space-y-gutter">
 <div class="inline-block px-4 py-1 border border-accent-gold text-accent-gold text-label-sm uppercase tracking-widest mb-4">Integrity Matters</div>
 <h2 class="text-display-xl font-display-xl">Crafted from Integrity</h2>
 <p class="text-body-lg text-on-surface-variant mb-8">${material}</p>
 <div class="space-y-8">
 <div class="flex items-start gap-4">
 <span class="material-symbols-outlined text-primary" data-icon="inventory_2">inventory_2</span>
 <div>
 <h4 class="font-bold text-body-lg">Wool-Silk Blend</h4>
 <p class="text-on-surface-variant">A proprietary 70/30 blend ensuring durability and a gentle sheen that catches the light with movement.</p>
 </div>
 </div>
 <div class="flex items-start gap-4">
 <span class="material-symbols-outlined text-primary" data-icon="temp_preferences_custom">temp_preferences_custom</span>
 <div>
 <h4 class="font-bold text-body-lg">Temperature Regulating</h4>
 <p class="text-on-surface-variant">Naturally breathable fibers that adapt to your body heat, keeping you composed in any climate.</p>
 </div>
 </div>
 <div class="flex items-start gap-4">
 <span class="material-symbols-outlined text-primary" data-icon="verified_user">verified_user</span>
 <div>
 <h4 class="font-bold text-body-lg">Indestructible Form</h4>
 <p class="text-on-surface-variant">Internal structural elements designed to never sag, maintaining the architectural silhouette for a lifetime.</p>
 </div>
 </div>
 </div>
 </div>
 </div>
 </div>
 </section>

 <!-- 6. STYLE GUIDE SECTION -->
 <section class="relative border border-primary/20 bg-surface/90 py-section-padding backdrop-blur-sm">
 <div class="section-label">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">06 / The Style Guide</span>
 </div>
 <div class="max-w-container-max mx-auto px-12">
 <div class="text-center mb-16">
 <span class="text-label-sm uppercase tracking-widest text-on-surface-variant">Curation</span>
 <h2 class="text-display-xl font-display-xl mt-2">Elevated Pairings</h2>
 </div>
 <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
 ${styling.map((s) => `
 <div class="group cursor-pointer p-6 border border-transparent hover:border-outline-variant/30 transition-all duration-500">
 <div class="overflow-hidden mb-6 aspect-[4/5] bg-surface-container border border-outline-variant/10">
 <img alt="${s.label}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="${s.img || image}"/>
 </div>
 <h3 class="text-headline-md font-headline-md mb-2">${s.label}</h3>
 <p class="text-on-surface-variant">${s.desc}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 7. TESTIMONIALS SECTION -->
 <section class="relative border border-primary/20 bg-surface-container-low/80 py-section-padding backdrop-blur-sm">
 <div class="section-label bg-surface-container-low">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">07 / The Voice of Quality</span>
 </div>
 <div class="max-w-container-max mx-auto px-12">
 <h2 class="text-display-xl font-display-xl text-center mb-16">Acclaimed Presence</h2>
 <div class="grid grid-cols-1 md:grid-cols-2 gap-gutter">
 ${reviews.map((r) => `
 <div class="p-10 bg-surface/90 border border-outline-variant/20 flex flex-col gap-6 shadow-sm">
 <div class="flex text-accent-gold">
 ${Array(5).fill(0).map((_, idx) => `<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' ${idx < (r.stars || 5) ? 1 : 0};">star</span>`).join('')}
 </div>
 <p class="text-body-lg font-body-lg italic leading-relaxed">"${r.quote}"</p>
 <div class="flex items-center gap-4 pt-4 border-t border-outline-variant/10">
 <div class="w-12 h-12 rounded-full bg-secondary-fixed flex items-center justify-center font-bold text-primary">${r.name.substring(0, 2).toUpperCase()}</div>
 <div>
 <p class="font-bold">${r.name}</p>
 <p class="text-label-sm text-on-surface-variant uppercase tracking-widest">${r.role || 'Verified Collector'}</p>
 </div>
 </div>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 8. COMMON INQUIRIES SECTION -->
 <section class="relative border border-primary/20 bg-surface/90 py-section-padding backdrop-blur-sm">
 <div class="section-label">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">08 / Common Inquiries</span>
 </div>
 <div class="max-w-4xl mx-auto px-12">
 <div class="text-center mb-12">
 <span class="text-label-sm uppercase tracking-widest text-on-surface-variant">Assistance</span>
 <h2 class="text-display-xl font-display-xl mt-2">Collector Support</h2>
 </div>
 <div class="space-y-6">
 ${faqs.map((faq) => `
 <div class="p-8 border border-outline-variant/30 bg-surface-container-lowest/90 group cursor-pointer hover:border-primary transition-colors">
 <h4 class="text-headline-md font-headline-md mb-4 flex justify-between items-center">
 ${faq.q}
 <span class="material-symbols-outlined group-hover:rotate-90 transition-transform duration-300">add</span>
 </h4>
 <p class="text-on-surface-variant text-body-md">${faq.a}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 9. FINAL CTA SECTION -->
 <section class="relative border border-primary/20 bg-surface-container-low/80 py-section-padding text-center backdrop-blur-sm">
 <div class="section-label bg-surface-container-low">
 <span class="text-label-sm font-label-sm uppercase tracking-[0.2em] text-primary">09 / Final Call</span>
 </div>
 <div class="max-w-4xl mx-auto px-12 py-20 border border-outline-variant/30 bg-surface/90 flex flex-col items-center shadow-xl backdrop-blur-sm">
 <span class="text-label-sm uppercase tracking-[0.3em] text-accent-gold mb-6">Limited Edition</span>
 <h2 class="text-display-xl font-display-xl mb-10 leading-tight">Elevate Your Existence</h2>
 <p class="text-body-lg text-on-surface-variant mb-10 max-w-2xl">Invest in a piece that transcends trends and defines your personal legacy. The Architectural Blazer is more than clothing—it's a statement of being.</p>
 <button class="buy-btn px-16 py-6 bg-primary text-on-primary font-headline-md hover:scale-105 transition-transform duration-300 shadow-xl flex items-center gap-4"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
 Upgrade Your Style
 <span class="material-symbols-outlined">trending_flat</span>
 </button>
 </div>
 </section>
 </main>
 `;

 setupProductButtons(product, name, price, image);
}

// ======================
// 💪 FITNESS (FIT) RENDERER
// ======================
// ======================
function renderFitProduct(product, container) {
 const name = product.name || "Apex Performance Collection";
 const price = Number(product.price) || 850;
 const description = product.description || "Engineered for the discerning athlete.";
 const image = getImageUrl(product.mainImage || product.image);
 
 // Data extraction with fallbacks
 const benefits = product.benefits || [
 {title: "Structural Strength", desc: "Precision-balanced weights for maximum muscular recruitment.", icon: "fitness_center"},
 {title: "Endurance Flow", desc: "Ergonomic design allows for higher volume sets safely.", icon: "timer"},
 {title: "Hypertrophy", desc: "Optimized resistance curves designed for maximum growth.", icon: "groups"},
 {title: "Metabolic Core", desc: "High-intensity design facilitates rapid caloric expenditure.", icon: "local_fire_department"}
 ];
 
 const technicalSpecs = product.features || [
 {title: "Aviation-Grade Steel", desc: "Cold-rolled, high-tensile steel core for zero-flex performance under maximum loads."},
 {title: "Precision Grip Technology", desc: "Diamond-cut knurling pattern provides maximum friction without skin abrasion."},
 {title: "Legacy Durability", desc: "Industrial powder coating and rust-resistant plating designed for generational use."},
 {title: "Biometric Comfort", desc: "Optimized contact points to reduce joint stress and focus on target muscle groups."}
 ];

 const protocol = product.ritualSteps || [
 {label: "Spatial Setup", icon: "architecture"},
 {label: "Dynamic Activation", icon: "self_improvement"},
 {label: "Elite Execution", icon: "fitness_center"},
 {label: "Restorative Cycle", icon: "bed"}
 ];

 const reviews = product.reviews && product.reviews.length > 0 ? product.reviews : [
 {name: "Marcus V.", quote: "Transformed my home studio into a world-class training facility.", stars: 5},
 {name: "Sarah J.", quote: "The tactile response is incredible. Peerless quality.", stars: 5},
 {name: "David K.", quote: "The results are measurable. Power output increased.", stars: 5}
 ];

 const faqs = product.faqs || [
 {q: "Is the Apex Performance Set squat-proof?", a: "Our performance gear is engineered with high-density fibers and reinforced stitching, ensuring complete opacity through full range of motion."},
 {q: "Does it provide medical-grade compression?", a: "The Apex collection utilizes targeted graduated compression zones designed to support muscle oscillation and enhance venous return."},
 {q: "What is the weight tolerance?", a: "Our aviation-grade steel barbell has been stress-tested to 200,000 PSI, maintaining zero whip under loads exceeding 1,500 lbs."}
 ];

 // Apply specific tailwind config for Fit Boutique if possible
 

 // Remove Care background styling to ensure cleanliness
 document.body.style.backgroundImage = "";
 document.body.style.backgroundAttachment = "";
 document.body.style.backgroundPosition = "";
 document.body.style.backgroundSize = "";

 container.innerHTML = `
 

 <div class="fixed-bg"></div>

 <main class="mt-[80px] max-w-screen-container relative z-10 bg-[#f7f3f2] text-on-background selection:bg-primary selection:text-white overflow-x-hidden font-body-md">
 <!-- HERO SECTION BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 01 // Hero Presentation</div>
 <section class="flex flex-col md:flex-row items-stretch">
 <div class="w-full md:w-1/2 relative min-h-[400px] md:min-h-[700px]">
 <img alt="${name}" class="absolute inset-0 w-full h-full object-cover" src="${image}"/>
 </div>
 <div class="w-full md:w-1/2 p-margin-page py-section-padding flex flex-col justify-center items-start gap-8 bg-surface/90">
 <span class="text-label-sm font-label-sm text-secondary tracking-[0.2em] uppercase">Fit Category // Elite Gear</span>
 <h1 class="text-display-xl font-display-xl leading-tight">${name}</h1>
 <p class="text-headline-md font-headline-md text-on-surface-variant font-light">${description}</p>
 <div class="flex flex-col gap-6 w-full">
 <div class="flex items-center gap-4 text-headline-lg font-headline-lg text-primary">
 <span>₹${price.toLocaleString('en-IN')}</span>
 </div>
 <ul class="flex flex-col gap-4">
 <li class="flex items-center gap-3 font-body-lg text-on-surface-variant">
 <span class="material-symbols-outlined text-secondary" data-icon="check_circle">check_circle</span> Superior Strength Foundation
 </li>
 <li class="flex items-center gap-3 font-body-lg text-on-surface-variant">
 <span class="material-symbols-outlined text-secondary" data-icon="check_circle">check_circle</span> Advanced Endurance Optimization
 </li>
 </ul>
 </div>
 <div class="flex flex-col sm:flex-row gap-4 w-full mt-6">
 <button class="buy-btn bg-primary text-white font-body-md font-semibold px-12 py-5 uppercase tracking-widest hover:bg-secondary transition-all duration-300 w-full sm:w-auto"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Add to Cart</button>
 <button class="border border-primary text-primary font-body-md font-semibold px-12 py-5 uppercase tracking-widest hover:bg-primary hover:text-white transition-all duration-300 w-full sm:w-auto">Inquiry</button>
 </div>
 </div>
 </section>
 </div>

 <!-- PERFORMANCE VISUALS BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 02 // Precision Engineering</div>
 <section class="py-section-padding bg-background/80 backdrop-blur-sm">
 <div class="px-margin-page mb-10">
 <p class="text-display-xl font-headline-lg max-w-2xl">The beauty of pure mechanics.</p>
 </div>
 <div class="flex gap-gutter overflow-x-auto pb-12 px-margin-page no-scrollbar snap-x snap-mandatory">
 <div class="min-w-[320px] md:min-w-[500px] aspect-video snap-center relative overflow-hidden group border refined-border rounded-lg">
 <img alt="Detail 1" class="w-full h-full object-cover transition-all duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAvW0byFTDMirRcxitlSv4A3pxD6hejdFkY7bhsUvfK-HzwtUVerNg_yqWa4uXiSqMLo7uWJM8FeI4QBH9eMc2vFV1L83T3tCgTpkz3YFZkaPXQOlCOtPQtYSaBz_KMm1MhbMSjLeo_-9PnWgyU4Jz3uVJp1tYDkpW07ae7VhJWLAUY3XSaMVHZd2jxHrx-Y9wnsroxzXxPsf49R7kyR9KU3P6DiOdj0EApU-DZwl_1LLkhzotYsqXqArB5hvId1NnELQNbbeTsRHxc"/>
 </div>
 <div class="min-w-[320px] md:min-w-[500px] aspect-video snap-center relative overflow-hidden group border refined-border rounded-lg">
 <img alt="Detail 2" class="w-full h-full object-cover transition-all duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBM2yFGOneWwKXeD6KjYWujQBqHyiN3yQHyk2m5IggeVreIZ2BAyBOlAj40U7jCOt39mmdF0pXk4K-KiUtIfi1KHWX5nmfmqI5dewJVnCoZpYGCzWNaao_VL-U9zF7qTsSZlr02jUjBLaOhfI3no31CzVZogA1-W6eesGz-h6V7onXmIbyiEnmPmhDdv9Pp79ZxBaINXHPxw6FCzdJKjfFfp0IO2A0dus0rlvGy4SGlA6jozOR09gBU1EOG0rFY6jAJbmGgfnlsnk8Y"/>
 </div>
 <div class="min-w-[320px] md:min-w-[500px] aspect-video snap-center relative overflow-hidden group border refined-border rounded-lg">
 <img alt="Detail 3" class="w-full h-full object-cover transition-all duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCmHfXBerH1vhxfd-awus42yNnWemY2x-2w41vTGKdkyUUVc-hnEBd9hV6rqTZRjjMh0ed_zZIuC6DAHZNa8JJQsy7AXconGfZpsvJIK0GbV1YHMxapg8XjTE5oAigE1iVtEjt8729Ec5mE2Xfa74KtGXOeegeg8jsx8WIMkCUMFmkTAzFXPE1IcAsMHzBP3ZQul7fDOSzbuv5TYRE_mQEYbGGaBdU8zkdWWcpIYYobOyzLW_F4ffamsNUN6o9XHZYkXT3TkkBL_wQk"/>
 </div>
 </div>
 </section>
 </div>

 <!-- PROBLEM & TRANSFORMATION BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 03 // The Performance Gap</div>
 <section class="flex flex-col md:flex-row">
 <div class="w-full md:w-1/2 p-section-padding bg-surface-container-low/90 md:border-r refined-border relative">
 <div class="relative z-10 flex flex-col gap-6">
 <h3 class="text-display-xl font-headline-lg text-primary/30 uppercase">Traditional Limits</h3>
 <p class="text-body-lg font-body-lg text-on-surface-variant max-w-sm">Inefficient equipment creates unnecessary plateaus. Break free from the cycle of stagnant progress.</p>
 </div>
 </div>
 <div class="w-full md:w-1/2 p-section-padding bg-surface/90 relative">
 <div class="relative z-10 flex flex-col gap-6">
 <h3 class="text-display-xl font-headline-lg text-primary uppercase">Elite Evolution</h3>
 <p class="text-body-lg font-body-lg text-on-surface-variant max-w-sm">The Apex Set provides the architectural leverage required to transcend your current physical limits.</p>
 </div>
 </div>
 </section>
 </div>

 <!-- KEY BENEFITS BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 04 // Core Attributes</div>
 <section class="py-section-padding px-margin-page bg-background/80">
 <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter">
 ${benefits.map((b) => `
 <div class="bento-card p-8 flex flex-col gap-6">
 <span class="material-symbols-outlined text-4xl text-primary" data-icon="${b.icon}">${b.icon}</span>
 <h4 class="text-headline-md font-headline-md uppercase text-sm font-bold">${b.title}</h4>
 <p class="text-on-surface-variant font-body-md text-sm">${b.desc}</p>
 </div>
 `).join('')}
 </div>
 </section>
 </div>

 <!-- TECHNICAL DOSSIER BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 05 // The Technical Dossier</div>
 <section class="py-section-padding px-margin-page bg-surface-container-low/90">
 <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
 ${technicalSpecs.map((spec, i) => `
 <div class="bg-white/80 backdrop-blur-sm p-10 border refined-border flex items-start gap-8 rounded-lg">
 <span class="text-secondary font-bold text-headline-md opacity-30">0${i + 1}</span>
 <div>
 <h5 class="text-headline-md uppercase mb-3 text-lg">${spec.title}</h5>
 <p class="text-on-surface-variant leading-relaxed text-sm">${spec.desc}</p>
 </div>
 </div>
 `).join('')}
 </div>
 </section>
 </div>

 <!-- EXECUTION PROTOCOL BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 06 // Execution Protocol</div>
 <section class="py-section-padding px-margin-page bg-background/80">
 <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
 ${protocol.map((step, i) => `
 <div class="flex flex-col gap-6 text-center group">
 <div class="aspect-square bg-surface-variant/80 flex items-center justify-center relative border refined-border rounded-xl transition-all duration-300 group-hover:bg-white group-hover:border-primary">
 <span class="absolute top-6 left-6 text-secondary font-bold text-[10px] tracking-widest uppercase">Phase 0${i + 1}</span>
 <span class="material-symbols-outlined text-6xl text-primary/40 group-hover:text-primary transition-colors" data-icon="${step.icon}">${step.icon}</span>
 </div>
 <h6 class="font-bold uppercase tracking-widest text-xs">${step.label}</h6>
 </div>
 `).join('')}
 </div>
 </section>
 </div>

 <!-- SOCIAL PROOF BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 07 // Peer Review</div>
 <section class="py-section-padding px-margin-page bg-surface-container-lowest/90">
 <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
 ${reviews.map((r) => `
 <div class="flex flex-col gap-8 p-8 border-b md:border-b-0 md:border-r refined-border last:border-0">
 <div class="flex gap-1 text-primary">
 ${Array(5).fill(0).map((_, idx) => `<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' ${idx < (r.stars || 5) ? 1 : 0};">star</span>`).join('')}
 </div>
 <p class="text-headline-md font-headline-md font-light italic text-lg">"${r.quote}"</p>
 <div class="flex items-center gap-4">
 <div class="w-10 h-10 rounded-full bg-surface-variant flex items-center justify-center text-primary text-[10px] font-bold">${r.name.substring(0, 2).toUpperCase()}</div>
 <span class="font-bold uppercase text-[10px] tracking-widest">${r.name}</span>
 </div>
 </div>
 `).join('')}
 </div>
 </section>
 </div>

 <!-- TECHNICAL INQUIRIES BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 08 // Technical Inquiries</div>
 <section class="py-section-padding px-margin-page bg-surface-container/80 backdrop-blur-sm">
 <div class="max-w-4xl mx-auto space-y-6">
 ${faqs.map((faq) => `
 <div class="p-8 bg-white/90 border refined-border rounded-lg">
 <h4 class="text-base font-bold uppercase tracking-wider mb-3">${faq.q}</h4>
 <p class="text-on-surface-variant font-body-md text-sm leading-relaxed">${faq.a}</p>
 </div>
 `).join('')}
 </div>
 </section>
 </div>

 <!-- FINAL CTA BOX -->
 <div class="section-box soft-shadow">
 <div class="section-label">Section 09 // Acquisition</div>
 <section class="py-[120px] px-margin-page bg-background/80 text-center flex flex-col items-center gap-10">
 <h2 class="text-display-xl font-headline-lg uppercase">Curate Your Performance</h2>
 <p class="text-body-lg font-body-lg text-on-surface-variant max-w-2xl mx-auto leading-relaxed">Invest in a legacy of strength. Join the select few who choose the Apex Performance Set.</p>
 <button class="buy-btn bg-primary text-white font-body-md font-bold px-16 py-6 uppercase tracking-[0.3em] hover:scale-105 transition-all duration-500"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Acquire Now</button>
 </section>
 </div>

 <!-- MOBILE STICKY CTA -->
 <div class="fixed bottom-0 left-0 w-full p-4 md:hidden bg-white/90 backdrop-blur-lg border-t refined-border z-50">
 <button class="buy-btn w-full bg-primary text-white font-bold py-5 uppercase tracking-widest"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Acquire - ₹${price.toLocaleString('en-IN')}</button>
 </div>
 </main>
 `;

 setupProductButtons(product, name, price, image);
}

// ======================
// 🏛️ HOME DECOR (SPACE) RENDERER — LUXURY CENTERPIECE EDITION
// ======================
function renderSpaceProduct(product, container) {
 const name = product.name || "Lunar Sphere Lamp";
 const price = Number(product.price) || 340;
 const description = product.description || "Illuminating the Art of Living";
 const image = getImageUrl(product.mainImage || product.image);
 const tagline = product.tagline || description;

 const designPillars = product.benefits || [
 {title: "Craftsmanship", desc: "Every lamp is hand-assembled by artisans with decades of experience in high-end metalwork.", icon: "draw"},
 {title: "Material Quality", desc: "Utilizing hand-blown crystalline glass to create a sphere of perfect clarity and unique internal character.", icon: "temp_preferences_custom"},
 {title: "Design Philosophy", desc: "A minimalist aesthetic that prioritizes the purity of light and the integrity of natural materials.", icon: "diamond"},
 {title: "Durability", desc: "Forged from solid brass and high-tempered glass, designed to be a centerpiece for generations.", icon: "verified"}
 ];

 const placements = product.placements || [
 {room: "Living Room", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuD8tHFpPCcs-8_Viziygvu5BawZU8mRFYmH31flxB1oUDMx0o_g4FoOjGWIHzQ4PwWf_xS0dlExlL1ahh4ml43CtqJtzXXtefoHscB9dwPiPMDdBBX7LbXCAw6bh4S2WB40zToXZsOPJbFvfuCTzJiqaB9ayyaiCB1hLviAuC7KJLln05ZTzc6HfG1sZWEnlbl3-YJ8Rl5jvEFCru6XM0-BvZFBzxgoW8Ht_3TPmAiaEMwwgGScIlV_96l9jCQW21rPR1WVMOW9P4hZ"},
 {room: "Bedroom", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuC2z7I9kJ3g8wzbrEHec5BJMPnK_zdR-NiDB-9lmpRMleh3MfsZhqaru5scGxZluB65OiAGS7aVwPyK8UDsTqjCOWJ5aHFisWdTpa9kV0EDOvzCzLzWfJdjFNkiiQbsd_Oa6lTkcSrH1RL4rfGXrrmjMA880WfPKTz9udn1X6TKcq7g-QfaH9cs8l8YngXxr1h9I76vVnNBjrtdzCLMqADcKDnlXxPca9HyHkAwD12YMTEzRb9JVm8tAZUvURFWwasK3lyre9TuyR8w"},
 {room: "Office", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuDCNR71SNZOfo1tJOXBa8pGutzvb_F_kD3JuPWYO6ibwydBzdcTJwhlas3c8oO8Pb0wi7Zb91bqWrtsCrku1BR6Z5agRq8vMTXVfXeAoTR195vtJqOItEFU2WsYieic_pTglTQkHoGcHZYkHIVu0r88zb3TmPr6wmf2_l2IBAQcM90Db9bn-hz7fex3fgRqoTrPcdeB9P3K1O6k6VHh33GLXvA9DSDCMmu55AWKhgv5qzV-Oy7lsrs0wxYBdpTRUw2WIUHyAaOQ5FmG"}
 ];

 const reviews = product.reviews && product.reviews.length > 0 ? product.reviews : [
 {name: "Eleanor V.", role: "Interior Designer", quote: "The way the light plays through the glass is simply mesmerizing. It's the first thing everyone notices when they walk into my study.", stars: 5},
 {name: "Marcus T.", role: "Architect", quote: "Most complimented piece in my home. I spent months looking for the perfect bedside lamp, and this is far beyond anything I expected.", stars: 5},
 {name: "Sarah J.", role: "Collector", quote: "Quiet luxury at its best. No branding, no noise—just beautiful materials and perfect illumination. It's transformed our evening routine.", stars: 5}
 ];

 const technicalSpecs = product.features || [
 {title: "Materials", desc: "The Lunar Sphere is constructed from a heavy-gauge, hand-blown crystalline glass orb and a solid 100% brass base with a hand-brushed matte finish. Each component is sustainably sourced and individually inspected."},
 {title: "Dimensions", desc: "Sphere Diameter: 12 inches (30.5 cm). Total Height: 14.5 inches (36.8 cm). Base Diameter: 6 inches (15.2 cm). Cord Length: 8 feet (2.4 m) with a premium braided fabric casing."},
 {title: "Care & Maintenance", desc: "To maintain the luster of the brass, dust with a soft, dry microfiber cloth. Avoid chemical cleaners. The glass sphere can be cleaned with a damp cloth and mild glass-safe solution."}
 ];

 const faqs = product.faqs || [
 {q: "Is the bulb replaceable?", a: "Yes, the Lunar Sphere uses a standard G9 base LED bulb which can be easily replaced by unscrewing the brass locking nut at the base of the glass sphere."},
 {q: "What is the voltage range?", a: "The lamp is designed for global use, supporting 110V - 240V. We provide the appropriate regional plug based on your shipping address."},
 {q: "Does it have a dimming feature?", a: "Yes, it features a discreet, touch-sensitive dimmer located on the brass base, allowing for three distinct levels of brightness to suit your mood."},
 {q: "How fragile is the glass sphere?", a: "While it is made of glass, it is hand-blown to a significant thickness (approx 5mm) for durability. It is far more robust than standard decorative glass lamps."}
 ];

 

 document.body.style.backgroundImage = "";
 document.body.style.backgroundAttachment = "";
 document.body.style.backgroundPosition = "";
 document.body.style.backgroundSize = "";

 container.innerHTML = `
 

 <div class="fixed-bg"></div>

 <main class="mt-[80px] max-w-container-max mx-auto relative z-10 bg-background text-on-surface font-body-md selection:bg-secondary-container">
 <!-- 1. HERO SECTION -->
 <section class="section-box overflow-hidden !bg-white/95">
 <span class="section-label">Featured Product</span>
 <div class="relative min-h-[700px] flex items-center justify-center rounded-lg overflow-hidden border border-outline-variant/20">
 <div class="absolute inset-0 z-0">
 <img class="w-full h-full object-cover" data-alt="${name}" src="${image}"/>
 <div class="absolute inset-0 bg-black/10"></div>
 </div>
 <div class="relative z-10 text-center px-margin-page max-w-4xl mx-auto">
 <span class="text-label-sm font-label-sm uppercase tracking-widest text-white/80 mb-4 block">New Arrival</span>
 <h1 class="text-display-xl font-display-xl text-white mb-2">${name}</h1>
 <p class="text-headline-md font-headline-md text-white/90 mb-8 italic">${tagline}</p>
 <div class="text-headline-md font-headline-md text-white mb-12">₹${price.toLocaleString('en-IN')}</div>
 <div class="flex flex-col sm:flex-row gap-gutter justify-center items-center">
 <button class="buy-btn bg-white text-primary px-12 py-4 border border-white hover:bg-accent-gold hover:border-accent-gold hover:text-white transition-all duration-300 font-headline-md"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
 Buy Now
 </button>
 <button class="border border-white text-white px-12 py-4 hover:bg-white hover:text-primary transition-all duration-300 font-headline-md">
 Add to Cart
 </button>
 </div>
 </div>
 </div>
 </section>

 <!-- 2. IMMERSIVE VISUALS -->
 <section class="section-box">
 <span class="section-label">Immersive Details</span>
 <div class="grid grid-cols-1 lg:grid-cols-12 gap-gutter h-auto">
 <div class="lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-gutter">
 <div class="aspect-square md:col-span-2 relative group overflow-hidden rounded-lg">
 <img class="w-full h-full object-cover border border-outline-variant/30 transition-transform duration-1000 group-hover:scale-110" data-alt="Detail Shot" src="https://lh3.googleusercontent.com/aida-public/AB6AXuADSDN-BgJUKUt3mwJZdkT0t507vfX4npXUwN7bnuiKFSzDmlTQ13SrPlDg4tFoG5stmAn_kH8SAJE_sAM78Mg_KU0Jfb4njtDJAfTRtfmQayznCzPra0HckjpkZzZKD98tHLefNoH852sCSNyULNQgf5GyE5N8RnBKiGAZh-FUx88u5q_PWkjfAVgKRhvRpFErtz15RVpTv-u4MXclhGPzrVSWyO1rnm1JxzdiIbwpjmjvGFNXTBrtDNP3-neitvK_NnHhVEbJ2Xsn"/>
 <div class="absolute bottom-4 right-4 bg-surface/90 backdrop-blur px-3 py-1 rounded text-label-sm uppercase tracking-tighter border border-accent-gold/20">Zoom Detail</div>
 </div>
 <div class="aspect-[4/5] relative group overflow-hidden rounded-lg">
 <img class="w-full h-full object-cover border border-outline-variant/30 transition-transform duration-1000 group-hover:scale-110" data-alt="Base detail" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAX1sNxMwMH6FCFZic7k4mF4EkE43X9C-DQYXlEEzHqofvCSO9jusbxeXBSYgEMqxBvYssN__9ED-0B4EP_REztrrPdEvwgluOlZTuqZgz9zp7x1jIuArz_XAyuqEVD68kKQkxc7bI1GYu1DwT-QvAwfcwX3fkU1llZ7eKnpIbhKhuxjKQzoOjY6ZeQ552Q2AuXHn4TM9cgtjJSNevxoObsVPLIONBlfPcTas4CrLUIL2TRH4LCxAEc5GxptJLoyrPgYOfr-cewowRn"/>
 <div class="absolute bottom-4 right-4 bg-surface/90 backdrop-blur px-3 py-1 rounded text-label-sm uppercase tracking-tighter border border-accent-gold/20">Artisan Finish</div>
 </div>
 <div class="aspect-[4/5] relative group overflow-hidden rounded-lg">
 <img class="w-full h-full object-cover border border-outline-variant/30 transition-transform duration-1000 group-hover:scale-110" data-alt="Lifestyle shot" src="https://lh3.googleusercontent.com/aida-public/AB6AXuB8o_Up021QlfrmvIzefIasjad-aG-kIlBmCLu6srWf65uRlys4pWCWl0uq8QIYfSsUW-x4AmKhlGgJr1HX8Mopge8riGaa3QpExsZxUO1pdf1_n4V-9tptAEX-kcHK-T4YB7zT5N2Ngk-VgudhwKP620Kf_iP2V7GplN_kyhrbKpW5xESvrDMLdz1gjIeI7D3rSaylIT51HeZW6SW41CRjH_KnX8CROYPovmxByJpv89YdgmJFIYBTGgVDxyV0aYBNvaqMg-veW_kT"/>
 <div class="absolute bottom-4 right-4 bg-surface/90 backdrop-blur px-3 py-1 rounded text-label-sm uppercase tracking-tighter border border-accent-gold/20">Atmosphere</div>
 </div>
 </div>
 <div class="lg:col-span-4 flex flex-col">
 <div class="relative bg-surface-container h-[400px] lg:h-full rounded-lg overflow-hidden border border-outline-variant/30 flex items-center justify-center group cursor-pointer">
 <div class="absolute inset-0 bg-black/30 group-hover:bg-black/40 transition-colors z-10"></div>
 <img alt="Video Placeholder" class="absolute inset-0 w-full h-full object-cover brightness-50" src="${image}"/>
 <div class="relative z-20 text-center text-white">
 <span class="material-symbols-outlined text-6xl mb-4 text-accent-gold" style="font-variation-settings: 'FILL' 1;">play_circle</span>
 <h3 class="text-headline-md font-headline-md">Watch the Glow</h3>
 <p class="text-label-sm uppercase tracking-widest opacity-80 mt-2">See it in real space</p>
 </div>
 </div>
 </div>
 </div>
 </section>

 <!-- 3. PROBLEM → TRANSFORMATION -->
 <section class="section-box bg-surface-container-low/90">
 <span class="section-label">The Transformation</span>
 <div class="text-center mb-16">
 <h2 class="text-headline-lg font-headline-lg text-primary mb-4">Redefine Your Environment</h2>
 <p class="text-body-lg font-body-lg text-on-surface-variant">The subtle difference of intentional design.</p>
 </div>
 <div class="grid grid-cols-1 md:grid-cols-2 gap-0 overflow-hidden rounded-xl border border-outline-variant/50 shadow-sm bg-surface">
 <div class="relative group">
 <img class="w-full h-[500px] object-cover opacity-60" data-alt="Dull uninspired room" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDgVQou4Hxe7sl87eGf5hR5I4LwFfDncXsN35C9F5xjG0ouHMkCp7YZDNCMR6c8Q8p9n9srOYggiKAUlXA9bAoaCiWoC9ZusraehZV6JPdM2lQToAZYwmUuVeq86b8RyLmpkm9joKiKSAxpgGYLm9XPKLovNn3LQiNf-IFrqD1fWVcbwuTqcsPRbYnSWuOK0IHdA3n2tPTl_iEASzXV8YL6-qiUg3BWJmzaHjAgjcfEEQio3z1xoXSEV-SC996jvAghCCXv4DN10ah3"/>
 <div class="absolute top-8 left-8 bg-black/60 backdrop-blur px-6 py-2 text-white font-label-sm uppercase tracking-widest border-l-2 border-accent-gold">Your Space Now</div>
 </div>
 <div class="relative group">
 <img class="w-full h-[500px] object-cover" data-alt="Transformed room with product" src="${image}"/>
 <div class="absolute top-8 right-8 bg-accent-gold/90 backdrop-blur px-6 py-2 text-white font-label-sm uppercase tracking-widest">With ${name}</div>
 </div>
 </div>
 </section>

 <!-- 4. WHY THIS PRODUCT -->
 <section class="section-box">
 <span class="section-label">Design Excellence</span>
 <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter">
 ${designPillars.map((b) => `
 <div class="p-8 border border-outline-variant/30 flex flex-col items-center text-center bg-surface-container-lowest/80 hover:border-accent-gold/40 transition-colors rounded-lg">
 <span class="material-symbols-outlined text-4xl mb-6 text-accent-gold">${b.icon || 'star'}</span>
 <h3 class="text-headline-md font-headline-md mb-4">${b.title}</h3>
 <p class="text-body-md font-body-md text-on-surface-variant">${b.desc}</p>
 </div>
 `).join('')}
 </div>
 </section>

 <!-- 5. PLACEMENT IDEAS -->
 <section class="section-box">
 <span class="section-label">Versatility in Every Room</span>
 <h2 class="text-headline-lg font-headline-lg text-primary text-center mb-16">Designed for Your Space</h2>
 <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
 ${placements.map((p) => `
 <div class="group cursor-pointer">
 <div class="overflow-hidden mb-6 rounded-lg border border-outline-variant/20">
 <img class="w-full aspect-[4/5] object-cover transition-transform duration-1000 group-hover:scale-105" data-alt="${p.room} Placement" src="${p.img}"/>
 </div>
 <h4 class="text-headline-md font-headline-md text-center group-hover:text-accent-gold transition-colors">${p.room}</h4>
 </div>
 `).join('')}
 </div>
 </section>

 <!-- 6. SOCIAL IMPACT -->
 <section class="section-box bg-surface-container/90">
 <span class="section-label">Customer Voices</span>
 <h2 class="text-headline-lg font-headline-lg text-primary text-center mb-16 italic">"Guests love this"</h2>
 <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
 ${reviews.map((r) => `
 <div class="bg-surface p-10 border border-outline-variant/20 flex flex-col shadow-sm rounded-lg relative overflow-hidden group">
 <div class="absolute top-0 right-0 p-4 opacity-5">
 <span class="material-symbols-outlined text-6xl">format_quote</span>
 </div>
 <div class="flex text-accent-gold mb-4">
 ${Array(5).fill(0).map((_, idx) => `<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' ${idx < (r.stars || 5) ? 1 : 0};">star</span>`).join('')}
 </div>
 <p class="text-body-lg font-body-lg text-primary mb-8 italic leading-relaxed">"${r.quote}"</p>
 <span class="text-label-sm font-label-sm uppercase tracking-widest mt-auto text-accent-gold">— ${r.name}, ${r.role || 'Customer'}</span>
 </div>
 `).join('')}
 </div>
 </section>

 <!-- 7. MATERIAL / DETAILS -->
 <section class="section-box">
 <span class="section-label">Technical Details</span>
 <div class="max-w-3xl mx-auto">
 <h2 class="text-headline-lg font-headline-lg text-primary mb-12 text-center">Product Specifications</h2>
 <div class="divide-y divide-outline-variant/30 border-t border-outline-variant/30">
 ${technicalSpecs.map((spec) => `
 <div class="py-6">
 <button class="w-full flex justify-between items-center text-left group" onclick="this.nextElementSibling.classList.toggle('hidden')">
 <span class="text-headline-md font-headline-md group-hover:text-accent-gold transition-colors">${spec.title}</span>
 <span class="material-symbols-outlined transition-transform duration-300 group-hover:rotate-45 text-accent-gold">add</span>
 </button>
 <div class="mt-4 text-body-md text-on-surface-variant leading-relaxed hidden">
 ${spec.desc}
 </div>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- FREQUENTLY ASKED QUESTIONS SECTION -->
 <section class="section-box bg-surface-container-low/95">
 <span class="section-label">FAQ</span>
 <div class="max-w-3xl mx-auto">
 <h2 class="text-headline-lg font-headline-lg text-primary mb-12 text-center">Frequently Asked Questions</h2>
 <div class="space-y-6">
 ${faqs.map((faq) => `
 <div class="bg-surface p-6 border border-outline-variant/30 rounded-lg shadow-sm group hover:border-accent-gold/30 transition-colors">
 <h4 class="text-headline-md font-headline-md mb-3 text-primary group-hover:text-accent-gold transition-colors">${faq.q}</h4>
 <p class="text-body-md text-on-surface-variant">${faq.a}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>

 <!-- 8. FINAL CTA BLOCK -->
 <section class="section-box !bg-primary/95 text-on-primary text-center">
 <span class="section-label !bg-primary">Final Invitation</span>
 <div class="max-w-4xl mx-auto py-12">
 <h2 class="text-display-xl font-display-xl mb-6">Complete your space today</h2>
 <p class="text-body-lg font-body-lg text-white/70 mb-12 max-w-xl mx-auto">Invest in a piece that transcends trends and brings a timeless elegance to your daily life.</p>
 <button class="buy-btn bg-accent-gold text-white px-16 py-5 border border-accent-gold hover:bg-white hover:text-primary transition-all duration-300 font-headline-md uppercase tracking-widest"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
 Secure Your ${name}
 </button>
 </div>
 </section>

 <!-- MOBILE STICKY CTA -->
 <div class="fixed bottom-0 left-0 w-full p-4 md:hidden bg-white/90 backdrop-blur-lg border-t border-outline-variant/30 z-50">
 <button class="buy-btn w-full bg-primary text-white font-bold py-5 uppercase tracking-widest"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Secure - ₹${price.toLocaleString('en-IN')}</button>
 </div>
 </main>
 `;

 setupProductButtons(product, name, price, image);
}


// ======================
// 🐾 PANTOPET (PET) RENDERER — LOVE & CARE EDITION
// ======================
function renderPetProduct(product, container) {
 const name = product.name || "Cloud-Comfort Pet Bed";
 const price = Number(product.price) || 0;
 const description = product.description || "A sanctuary of soft textures and orthopedic support for your most loyal companion.";
 const image = getImageUrl(product.mainImage || product.image);
 const tagline = product.tagline || "Because unconditional love deserves unconditional quality.";

 const materials = product.materials || [
 {title: "Eco-Soft Fiber", desc: "Hypoallergenic and breathable for sensitive skin.", icon: "eco"},
 {title: "Orthopedic Base", desc: "Medical-grade support for healthy joints.", icon: "health_and_safety"},
 {title: "Pet-Safe Dyes", desc: "0% toxins, 100% safe for inquisitive paws.", icon: "check_circle"}
 ];

 const benefits = product.benefits || [
 {title: "Pure Comfort", desc: "Soft-touch textures for anxiety reduction.", icon: "favorite"},
 {title: "Daily Hygiene", desc: "Easy-wash materials for a cleaner home.", icon: "clean_hands"},
 {title: "Lasting Health", desc: "Designed to support longevity and joy.", icon: "vital_signs"}
 ];

 const steps = product.steps || [
 {step: "Introduce", desc: "Place in their favorite sunlit corner."},
 {step: "Acclimatize", desc: "Let them explore the soft textures naturally."},
 {step: "Bond", desc: "Watch them settle into their new sanctuary."}
 ];

 const faqs = product.faqs || [
 {q: "Is the Artisanal Wool Nest machine washable?", a: "While organic Merino wool is naturally stain and odor-resistant, we recommend gentle spot cleaning with a wool-safe detergent. For a deep refresh, professional dry cleaning is advised to maintain the structural integrity of the weave."},
 {q: "Is it safe for kittens and puppies?", a: "Absolutely. Our wool is 100% organic and non-toxic, with no harsh chemicals or dyes. The soft, rounded rim provides a nesting sensation that mimics their mother's warmth, helping young pets feel secure."},
 {q: "Does the wool shed over time?", a: "Some minor pilling is a natural characteristic of high-quality unspun wool. This can be easily managed by gently removing pills with your fingers or a wool comb, which actually helps the nest settle into its permanent, cozy shape."},
 {q: "What if my pet doesn't take to it immediately?", a: "Pets often need a few days to adjust to new scents and textures. We recommend placing a familiar blanket inside the nest for the first 48 hours to help them recognize it as their new safe sanctuary."}
 ];

 const reviews = product.reviews && product.reviews.length > 0 ? product.reviews : [
 {name: "Eleanor M.", role: "Verified Collector", initials: "EM", quote: "Finally, a bed that doesn't ruin the living room aesthetic. My Golden hasn't slept anywhere else since it arrived.", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuBQkc-wSCJ5t971NQVNZw8ec7dOguwrjokO_Ny51hGW7mHG0sKrljbBxaONg_DMjIAHGx2-1P862Hpqauy8zqATUORwIyxnM98whX2xVEEMmItLr9Z4Jhfmn5Z019GsyczY42f3AApI8agD5YN8S6eJyKfBVHoDT0gkRxq7FRUgt7ySQS948T0O7N_9jKNkirdWQTs2qd9PXa0B6Grq1cSWkmcKMi4_sVsTzuXoO6oxjf7_Tb7lv-I0iFvo9vYVjgQFwYibitndHFlf"},
 {name: "Julian R.", role: "Verified Collector", initials: "JR", quote: "The softness is unparalleled. Luna purrs the moment she touches the wool. It's her safe space now.", img: "https://lh3.googleusercontent.com/aida-public/AB6AXuCH1PiURsWiz9LttCexmkKlfNaHTB290MC9Qp8hSzscrkyzN11levh4wzOgtfEbuuN7uDXrCZn65iSTL5sC1ib27KCi_-KixOncdjaZ1N2Qsl4AUIQGDLURYDtDHmgGhYBTNoe56JhU_WOBC9WZXd4SUIrNlgp1_yaUAs-NVBnBM65yN9BvqHGDsXGuRTS1tY5iiQ1ltor7YnLlZOxGlxeilwg4MHYje-4KxuA1YKeuO77vUnlKVFhxqNLlRpYIwl3WrCpXlRRkoZlQ"}
 ];

 

 document.body.style.backgroundImage = "";
 document.body.style.backgroundAttachment = "";
 document.body.style.backgroundPosition = "";
 document.body.style.backgroundSize = "";

 container.innerHTML = `
 
 
 <div class="fixed-bg"></div>
 <div class="bg-overlay"></div>

 <main class="max-w-container-max mx-auto px-margin-page py-8 relative z-10 text-on-background font-body-md overflow-x-hidden">
 <!-- 1. HERO -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">auto_awesome</span>Featured Collection</div>
 <section class="relative min-h-[700px] flex items-center overflow-hidden">
 <div class="absolute inset-0 z-0">
 <img alt="${name} Hero" class="w-full h-full object-cover" data-alt="${name}" src="${image}"/>
 <div class="absolute inset-0 bg-gradient-to-r from-surface/60 to-transparent"></div>
 </div>
 <div class="relative z-10 px-margin-page w-full">
 <div class="max-w-xl">
 <span class="text-label-sm font-label-sm uppercase tracking-widest text-primary mb-4 block">New Collection</span>
 <h1 class="font-display-xl text-display-xl text-primary mb-6">${name}</h1>
 <p class="font-body-lg text-body-lg text-on-surface-variant mb-10 max-w-md">${tagline}</p>
 <button class="buy-btn px-10 py-4 border border-primary text-primary font-headline-md hover:bg-primary hover:text-on-primary transition-all duration-300 rounded-lg"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
 Care for Your Pet
 </button>
 </div>
 </div>
 </section>
 </div>

 <!-- 2. TRUST BAR -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">verified_user</span>Quality Assurance</div>
 <section class="bg-surface-container-low/50 py-8">
 <div class="px-margin-page">
 <div class="flex flex-wrap justify-between items-center gap-gutter">
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-sm" data-icon="shield_check">shield</span>
 <span class="font-label-sm text-on-surface-variant">Safe for Pets</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-sm" data-icon="eco">eco</span>
 <span class="font-label-sm text-on-surface-variant">Non-Toxic</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-sm" data-icon="medical_services">medical_services</span>
 <span class="font-label-sm text-on-surface-variant">Vet-Friendly</span>
 </div>
 <div class="flex items-center gap-2">
 <span class="material-symbols-outlined text-primary text-sm" data-icon="favorite">favorite</span>
 <span class="font-label-sm text-on-surface-variant">Loved by Pet Owners</span>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 3. PROBLEM -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">error_outline</span>The Comfort Gap</div>
 <section class="py-16 bg-transparent">
 <div class="px-margin-page">
 <div class="grid md:grid-cols-2 gap-16 items-center">
 <div class="rounded-xl overflow-hidden shadow-sm border border-outline-variant/30">
 <img alt="Uncomfortable pet" class="w-full h-[400px] object-cover " data-alt="A close-up shot of an older dog lying uncomfortably on a cold, hard tile floor in a modern kitchen." src="https://lh3.googleusercontent.com/aida-public/AB6AXuB6rdQVzW61ES12Ta2AtysBk8npJMyEEnt4HDYvp5H_OvLguKWAgKHu6q_W8ivdHEb7E7LzpM6SjQM-yLZukdvbeOyG0sWp1PKOVaqVrMn2fC5ewZJtzc2k-Y5W6_GeK_XpN_5UNW6uumZUUtf3R0TLrbOmU5DoK5B-Fjn8R5gy8dAEOQr_rDKzNi8_TXfGCa_8IUPKMsw19bIz7dWoJZ8NrYGmMh_gTyT2xLzCwbzdxDloyzvrt1zng_FPU1ptMIJPp-KgUrWtRDfs"/>
 </div>
 <div>
 <h2 class="font-headline-lg text-headline-lg text-primary mb-6">Rest shouldn't be a struggle.</h2>
 <p class="font-body-lg text-body-lg text-on-surface-variant mb-4">Hard floors and thin beds offer zero support for your pet's aging joints, leading to restless nights and morning stiffness.</p>
 <p class="font-body-lg text-body-lg text-on-surface-variant">Standard synthetic materials also fail to regulate temperature, leaving your companion too hot in summer and shivering in the winter chill.</p>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 4. SOLUTION -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">check_circle</span>The Aetheris Solution</div>
 <section class="py-16 bg-surface-container-low/50">
 <div class="px-margin-page">
 <div class="grid md:grid-cols-2 gap-16 items-center">
 <div class="order-2 md:order-1">
 <h2 class="font-headline-lg text-headline-lg text-primary mb-6">Embrace the Aetheris Calm</h2>
 <p class="font-body-lg text-body-lg text-on-surface-variant mb-6">The ${name} is engineered to cradle every curve. Its unique structural weave provides orthopaedic relief while the dense wool fibers create a micro-climate of pure comfort.</p>
 <ul class="space-y-4">
 <li class="flex items-center gap-3">
 <span class="material-symbols-outlined text-secondary" data-icon="check_circle" style="font-variation-settings: 'FILL' 1;">check_circle</span>
 <span class="font-body-md text-on-surface">Adaptive joint support</span>
 </li>
 <li class="flex items-center gap-3">
 <span class="material-symbols-outlined text-secondary" data-icon="check_circle" style="font-variation-settings: 'FILL' 1;">check_circle</span>
 <span class="font-body-md text-on-surface">Self-regulating temperature control</span>
 </li>
 </ul>
 </div>
 <div class="order-1 md:order-2 rounded-xl overflow-hidden shadow-md border border-outline-variant/30">
 <img alt="Happy pet in nest" class="w-full h-[400px] object-cover" data-alt="A happy, relaxed cat stretching luxuriously inside a plush, oversized Artisanal Wool Nest in a soft peach color." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDLW1KD11RPU-QcJxaMJJWqh4IRJuY4p0xjIwYtZABe1RFQqrXCIWVAcZ1V9pZM1v0j8ChsuTcep50MYR_7_bCmvpxou0GmpDfKuPqikoAwn7si6ExCH1LaHjxojXYfMtFSsHeIEUAHS4CBffc2tIG_3Qjh5OGIHr6sOMxvZFywhmwlCMYEGeNi7t-vnmgBbSQ6cwPaLHDK8pbexpiUqUDpv4eyh6ditIpz_4CUHmtEnjBc-YKkxALGXakDQl3CUY4yZdsWluyniGHn"/>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 5. MATERIALS -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">compost</span>Born from Nature</div>
 <section class="py-16 bg-transparent">
 <div class="px-margin-page">
 <div class="text-center mb-12">
 <h2 class="font-headline-lg text-headline-lg text-primary mb-4">Born from Nature</h2>
 <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">We use only the finest raw materials to ensure a legacy of quality and care.</p>
 </div>
 <div class="grid md:grid-cols-2 gap-gutter">
 <div class="p-10 bg-surface-container-low/50 rounded-xl border border-outline-variant/30 text-center backdrop-blur-sm">
 <span class="material-symbols-outlined text-4xl mb-6 block text-secondary" data-icon="compost">compost</span>
 <h3 class="font-headline-md text-headline-md text-primary mb-4">100% Organic Merino</h3>
 <p class="font-body-md text-on-surface-variant">Sourced from sustainable farms, our wool is processed without harsh chemicals, preserving its natural elasticity and silk-like softness.</p>
 </div>
 <div class="p-10 bg-surface-container-low/50 rounded-xl border border-outline-variant/30 text-center backdrop-blur-sm">
 <span class="material-symbols-outlined text-4xl mb-6 block text-secondary" data-icon="clean_hands">clean_hands</span>
 <h3 class="font-headline-md text-headline-md text-primary mb-4">Hypoallergenic Shield</h3>
 <p class="font-body-md text-on-surface-variant">Naturally resistant to dust mites and allergens, providing a safe haven for even the most sensitive pets and their human companions.</p>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 6. BENEFITS GRID -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">spa</span>Wellness Benefits</div>
 <section class="py-16 bg-surface-container-highest/10">
 <div class="px-margin-page">
 <div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
 <div class="flex flex-col items-center text-center p-8 bg-white/50 backdrop-blur-sm rounded-xl border border-outline-variant/30">
 <span class="material-symbols-outlined text-5xl text-secondary mb-6" data-icon="cloud">cloud</span>
 <h4 class="font-headline-md text-headline-md text-primary mb-3">Cloud-Like Comfort</h4>
 <p class="font-body-md text-on-surface-variant">High-loft fibers create a buoyant surface that mimics the feeling of being held.</p>
 </div>
 <div class="flex flex-col items-center text-center p-8 bg-white/50 backdrop-blur-sm rounded-xl border border-outline-variant/30">
 <span class="material-symbols-outlined text-5xl text-secondary mb-6" data-icon="wash">wash</span>
 <h4 class="font-headline-md text-headline-md text-primary mb-3">Easy Hygiene</h4>
 <p class="font-body-md text-on-surface-variant">Naturally odor-resistant and easy to spot clean for a fresh home environment.</p>
 </div>
 <div class="flex flex-col items-center text-center p-8 bg-white/50 backdrop-blur-sm rounded-xl border border-outline-variant/30">
 <span class="material-symbols-outlined text-5xl text-secondary mb-6" data-icon="spa">spa</span>
 <h4 class="font-headline-md text-headline-md text-primary mb-3">Anxiety Relief</h4>
 <p class="font-body-md text-on-surface-variant">The raised rim creates a sense of security that lowers cortisol levels in anxious pets.</p>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 7. HOW TO USE -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">footprint</span>The Journey to Better Rest</div>
 <section class="py-16 bg-transparent">
 <div class="px-margin-page">
 <h2 class="font-headline-lg text-headline-lg text-primary mb-12 text-center">The Journey to Better Rest</h2>
 <div class="grid md:grid-cols-3 gap-12">
 <div class="relative p-8 rounded-xl border border-outline-variant/10 bg-surface-container-lowest/80 backdrop-blur-sm shadow-sm">
 <div class="text-[80px] font-headline-lg text-outline-variant/30 absolute -top-10 -left-4 z-0">1</div>
 <div class="relative z-10">
 <h5 class="font-headline-md text-headline-md text-primary mb-4">Unbox</h5>
 <p class="font-body-md text-on-surface-variant">Remove the nest from its eco-friendly packaging and let it breathe in the fresh air.</p>
 </div>
 </div>
 <div class="relative p-8 rounded-xl border border-outline-variant/10 bg-surface-container-lowest/80 backdrop-blur-sm shadow-sm">
 <div class="text-[80px] font-headline-lg text-outline-variant/30 absolute -top-10 -left-4 z-0">2</div>
 <div class="relative z-10">
 <h5 class="font-headline-md text-headline-md text-primary mb-4">Shape</h5>
 <p class="font-body-md text-on-surface-variant">Lightly fluff the wool to your pet's preference, creating a perfect custom bowl.</p>
 </div>
 </div>
 <div class="relative p-8 rounded-xl border border-outline-variant/10 bg-surface-container-lowest/80 backdrop-blur-sm shadow-sm">
 <div class="text-[80px] font-headline-lg text-outline-variant/30 absolute -top-10 -left-4 z-0">3</div>
 <div class="relative z-10">
 <h5 class="font-headline-md text-headline-md text-primary mb-4">Observe</h5>
 <p class="font-body-md text-on-surface-variant">Watch as they instinctively sink in and drift into a deeper, healthier sleep.</p>
 </div>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 8. SOCIAL PROOF -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">auto_stories</span>Captured Moments of Calm</div>
 <section class="py-16 bg-surface-container-low/50 overflow-hidden">
 <div class="px-margin-page">
 <h2 class="font-headline-lg text-headline-lg text-primary mb-12 text-center">Captured Moments of Calm</h2>
 <div class="flex gap-gutter overflow-x-auto pb-8 snap-x">
 ${reviews.map((r) => `
 <div class="min-w-[300px] md:min-w-[400px] snap-center bg-surface/90 backdrop-blur-sm p-6 rounded-xl border border-outline-variant/20 shadow-sm">
 <img alt="${r.name} review" class="w-full h-48 object-cover rounded-lg mb-6 border border-outline-variant/20" data-alt="${r.name} review image" src="${r.img}"/>
 <p class="font-body-md italic text-on-surface mb-4">"${r.quote}"</p>
 <div class="flex items-center gap-3">
 <div class="w-10 h-10 rounded-full bg-secondary-fixed flex items-center justify-center font-label-sm">${r.initials || 'P'}</div>
 <div>
 <div class="font-label-sm text-primary">${r.name}</div>
 <div class="text-[10px] text-on-surface-variant">${r.role || 'Verified Collector'}</div>
 </div>
 </div>
 </div>
 `).join('')}
 </div>
 </div>
 </section>
 </div>

 <!-- 9. SAFETY -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">shield</span>Safety Standards</div>
 <section class="py-12 bg-surface-container-highest/20">
 <div class="px-margin-page">
 <div class="flex flex-col md:flex-row justify-center items-center gap-12">
 <div class="flex items-center gap-4">
 <div class="w-16 h-16 rounded-full border border-primary/20 flex items-center justify-center bg-surface-container-low shadow-sm">
 <span class="material-symbols-outlined text-primary text-3xl" data-icon="verified">verified</span>
 </div>
 <div>
 <div class="font-label-sm text-primary">Zero Harmful Chemicals</div>
 <div class="text-[11px] text-on-surface-variant uppercase tracking-wider">Lab Tested &amp; Approved</div>
 </div>
 </div>
 <div class="flex items-center gap-4">
 <div class="w-16 h-16 rounded-full border border-primary/20 flex items-center justify-center bg-surface-container-low shadow-sm">
 <span class="material-symbols-outlined text-primary text-3xl" data-icon="calendar_today">calendar_today</span>
 </div>
 <div>
 <div class="font-label-sm text-primary">Daily Use Certified</div>
 <div class="text-[11px] text-on-surface-variant uppercase tracking-wider">Durability Assured</div>
 </div>
 </div>
 </div>
 </div>
 </section>
 </div>

 <!-- 10. FAQ SECTION -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">quiz</span>Care &amp; Questions</div>
 <section class="py-16 bg-transparent">
 <div class="max-w-3xl mx-auto px-margin-page">
 <h2 class="font-headline-lg text-headline-lg text-primary mb-12 text-center">Frequently Asked Questions</h2>
 <div class="space-y-6">
 ${faqs.map((faq) => `
 <div class="p-6 rounded-xl border border-outline-variant/30 bg-surface-container-low/70 backdrop-blur-sm">
 <h4 class="font-headline-md text-[20px] text-primary mb-3">${faq.q}</h4>
 <p class="font-body-md text-on-surface-variant">${faq.a}</p>
 </div>
 `).join('')}
 </div>
 </div>
 </section>
 </div>

 <!-- 11. FINAL CTA -->
 <div class="section-container">
 <div class="section-label"><span class="material-symbols-outlined text-[14px]">pets</span>Final Invitation</div>
 <section class="py-16 bg-transparent">
 <div class="px-margin-page">
 <div class="bg-surface-container-low/80 rounded-[2rem] p-16 text-center border border-outline-variant/30 relative overflow-hidden shadow-sm backdrop-blur-sm">
 <div class="absolute top-0 right-0 p-12 opacity-10">
 <span class="material-symbols-outlined text-[200px]" data-icon="pets">pets</span>
 </div>
 <div class="relative z-10 max-w-2xl mx-auto">
 <h2 class="font-display-xl text-display-xl text-primary mb-8 leading-tight">Because they deserve the best.</h2>
 <p class="font-body-lg text-body-lg text-on-surface-variant mb-12">Give them the gift of restorative sleep and a lifetime of gentle comfort with the ${name}.</p>
 <button class="buy-btn px-12 py-5 bg-primary text-on-primary font-headline-md hover:opacity-90 transition-all duration-300 rounded-lg shadow-lg"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
 Care for Your Pet
 </button>
 </div>
 </div>
 </div>
 </section>
 </div>
 
 <!-- MOBILE STICKY CTA -->
 <div class="fixed bottom-0 left-0 w-full p-4 md:hidden bg-surface/90 backdrop-blur-lg border-t border-outline-variant/30 z-50">
 <button class="buy-btn w-full bg-primary text-on-primary font-bold py-4 uppercase tracking-widest rounded-lg shadow-lg"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Care - ₹${price.toLocaleString('en-IN')}</button>
 </div>
 </main>
 `;

 setupProductButtons(product, name, price, image);
}


// ======================
// 🧱 DEFAULT RENDERER
// ======================
function renderDefaultProduct(product, container) {
 const name = product.name || "Premium Selection";
 const price = Number(product.price) || 0;
 const description = product.description || "A testament to quality and intentional design.";
 const image = getImageUrl(product.mainImage || product.image);

 container.innerHTML = `
 <main class="mt-24 px-margin-page py-section-padding">
 <div class="max-w-container-max mx-auto grid md:grid-cols-2 gap-gutter items-center">
 <div class="aspect-square bg-surface-container-low rounded-3xl overflow-hidden shadow-inner">
 <img class="w-full h-full object-cover mix-blend-multiply" src="${image}" onerror="this.src='./assets/images/placeholder.jpg'"/>
 </div>
 <div class="space-y-12 md:pl-16">
 <div class="space-y-6">
 <span class="text-label-sm font-label-sm uppercase tracking-widest text-primary">Limited Edition</span>
 <h1 class="text-display-xl font-display-xl text-on-surface">${name}</h1>
 <div class="flex items-center gap-4">
 <span class="text-headline-lg font-headline-lg text-primary">₹${price.toLocaleString('en-IN')}</span>
 <div class="h-4 w-px bg-outline-variant"></div>
 <div class="flex gap-1 text-primary">
 ${Array(5).fill(0).map(() => '<span class="material-symbols-outlined text-sm" style="font-variation-settings: \'FILL\' 1;">star</span>').join('')}
 </div>
 </div>
 <p class="text-body-xl font-body-xl text-on-surface-variant leading-relaxed">${description}</p>
 </div>
 
 <div class="grid grid-cols-2 gap-8 border-y border-outline-variant/30 py-8">
 <div class="space-y-2">
 <h5 class="text-label-sm font-label-sm uppercase text-on-surface-variant opacity-60">Sourcing</h5>
 <p class="text-body-md font-body-md">Ethically Crafted</p>
 </div>
 <div class="space-y-2">
 <h5 class="text-label-sm font-label-sm uppercase text-on-surface-variant opacity-60">Delivery</h5>
 <p class="text-body-md font-body-md">Global Shipping</p>
 </div>
 </div>

 <div class="flex flex-col gap-4">
 <button class="buy-btn w-full py-6 bg-primary text-on-primary font-label-sm uppercase tracking-widest hover:bg-on-surface transition-all duration-500 rounded-none shadow-xl"
 data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
 ADD TO COLLECTION
 </button>
 <div class="flex items-center justify-center gap-6 text-on-surface-variant/40">
 <span class="material-symbols-outlined">verified</span>
 <span class="text-label-sm">Secured Checkout</span>
 </div>
 </div>
 </div>
 </div>
 </main>
 `;

 setupProductButtons(product, name, price, image);
}

// ======================
// 🖼️ PREMIUM BACKGROUND SYSTEM
// ======================
function initFixedBackground(image) {
 // Add category class to body for specific overrides if needed
 document.body.classList.add('product-page');
 
 // Set the body background properties
 document.body.style.backgroundImage = 'url(' + JSON.stringify(image) + ')';
 document.body.style.backgroundAttachment = 'fixed';
 document.body.style.backgroundSize = 'cover';
 document.body.style.backgroundPosition = 'center';

 // Body background color (subtle neutral in case image fails)
 document.body.style.backgroundColor = '#f4f4f4';

 // Inject gap styling for floating boxes
 var st = document.getElementById('product-fixed-bg-style');
 if (!st) {
 st = document.createElement('style');
 st.id = 'product-fixed-bg-style';
 document.head.appendChild(st);
 }
 st.textContent = `
 /* Clear out any inline backgrounds that might conflict */
 #product-container > div { background: transparent !important; }
 
 /* Ensure spacing between floating sections */
 #product-container section, 
 #product-container .sp-box,
 #product-container .fit-page > div,
 #product-container .fit-strip,
 #product-container .fit-eng,
 #product-container .fit-outcome,
 #product-container .fit-social,
 #product-container .fit-final,
 #product-container .sp-hero,
 #product-container .sp-atm,
 #product-container .sp-story-inner,
 #product-container .sp-mat-inner,
 #product-container .sp-tf,
 #product-container .sp-pl-inner,
 #product-container .sp-soc-inner,
 #product-container .sp-final-inner {
 margin-top: 60px !important;
 margin-bottom: 60px !important;
 }
 
 /* Hero sections specific adjustments */
 .fit-hero, .sp-hero { height: 80vh !important; border-radius: 24px !important; overflow: hidden !important; }
 `;
}

// ======================
// 🌌 PARALLAX ENGINE — Runs on every product page
// ======================
function initParallax() {
 // Clean up any previous parallax listeners to avoid stacking
 if (window._parallaxCleanup) window._parallaxCleanup();

 let ticking = false;

 function update() {
 const scrollY = window.scrollY || window.pageYOffset;
 
 // Smooth background parallax effect
 document.body.style.backgroundPosition = `center ${scrollY * 0.35}px`;
 
 ticking = false;
 }

 function onScroll() {
 if (!ticking) {
 window.requestAnimationFrame(update);
 ticking = true;
 }
 }

 update();
 window.addEventListener('scroll', onScroll, { passive: true });

 window._parallaxCleanup = function() {
 window.removeEventListener('scroll', onScroll);
 document.body.style.backgroundPosition = '';
 window._parallaxCleanup = null;
 };
}

// ======================
// ✨ SCROLL REVEAL ENGINE
// ======================
function initScrollReveal() {
 const container = document.getElementById('product-container');
 if (!container) return;

 // Select all premium boxes based on the CSS rules
 const selectors = [
 '#product-container > div > div',
 '#product-container > div > section',
 '.product-layout',
 '.editorial-banner',
 '.ingredient-box',
 '.review-summary',
 '.review-card',
 '.qa-item',
 '.fit-strip',
 '.fit-why-cell',
 '.fit-eng-item',
 '.fit-outcome-cell',
 '.fit-review',
 '.sp-box'
 ];

 const boxes = new Set();
 selectors.forEach(sel => {
 document.querySelectorAll(sel).forEach(el => boxes.add(el));
 });

 if (boxes.size === 0) return;

 // Initialize observer
 const observer = new IntersectionObserver((entries, obs) => {
 entries.forEach(entry => {
 if (entry.isIntersecting) {
 entry.target.classList.add('visible');
 // Optional: stop observing once revealed
 // obs.unobserve(entry.target);
 }
 });
 }, {
 root: null,
 threshold: 0.1, // Trigger when 10% visible
 rootMargin: '0px 0px -50px 0px' // Slight offset to trigger slightly later
 });

 // Apply reveal-box class and observe
 boxes.forEach(box => {
 // Avoid applying to raw wrapper divs that just hold content but aren't styled as boxes
 if (box.style.background === 'transparent' || box.id === 'product-container') return;
 
 box.classList.add('reveal-box');
 observer.observe(box);
 });
}


// ======================
// 🛒 HELPER: CART INTEGRATION
// ======================
function setupProductButtons(product, name, price, image) {
 const buyBtns = document.querySelectorAll('.buy-btn');
 buyBtns.forEach(btn => {
 btn.onclick = () => {
 const item = {
 _id: product._id,
 name: name,
 price: price,
 image: image,
 quantity: 1
 };
 
 if (window.addToCart) {
 window.addToCart(item);
 } else {
 console.warn('Cart system not loaded. Item:', item);
 alert('Item added to cart (System Simulation)');
 }
 };
 });
}
