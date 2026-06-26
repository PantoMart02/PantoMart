file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '// Home Decor (Space) Renderer'
end_marker = '\nfunction renderPetProduct'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

print(f"Start: {start_idx}, End: {end_idx}, Block size: {end_idx - start_idx}")

new_block = '''// Home Decor (Space) Renderer — Dynamic Quiet Luxury Edition
// ======================
function renderSpaceProduct(product, container) {
  const name = product.name || 'Sculptural Accent Piece';
  const price = Number(product.price) || 0;
  const image = getImageUrl(product.mainImage || product.image);
  const tagline = product.tagline || 'Objects that hold the room in quiet reverence.';

  const hook = product.hook || {
    headline: "Your Space Deserves to Look Like It Was Designed on Purpose.",
    problem: "A bare overhead light. A desk that looks functional but never beautiful. Guests come over and your study gets a polite glance — not a second look.",
    solution: "Close your eyes and picture this. Warm, amber light curves softly over your desk. The whole corner looks curated, considered, and completely yours."
  };

  const benefits = product.benefits || [
    {icon:'✨', title:'Instant Elegance', desc:'Transforms any surface from overlooked to unmistakable.'},
    {icon:'🏡', title:'Room With a Soul', desc:'Signals taste, intention, and personality that furniture alone never can.'},
    {icon:'👀', title:'Guests Notice', desc:'They ask about it before they notice anything else.'},
    {icon:'📸', title:'Photographs Beautifully', desc:'Your space starts looking like the life you want to be living.'}
  ];

  const ingredients = product.ingredients || [
    {icon:'🏺', name:'Premium Materials', desc:'Crafted with weight, texture and finish that mass-produced alternatives cannot replicate.'},
    {icon:'✨', name:'Hand-Applied Details', desc:'Carefully applied finishes that create gallery-worthy contrast and richness.'},
    {icon:'🪵', name:'Considered Proportions', desc:'Every dimension intentional — creating visual harmony that feels effortless.'},
    {icon:'🌾', name:'Curated Accessories', desc:'What arrives is styled and ready to display. No arrangement skills needed.'}
  ];

  const howToUse = product.howToUse || [
    {step:'Unbox', desc:'Arrives ready. No assembly. No styling expertise needed.'},
    {step:'Place', desc:'Set on your console, shelf, dresser, or desk surface.'},
    {step:'Admire', desc:'Watch the room transform. Watch guests react.'}
  ];

  const reviews = product.reviews || [
    {name:'Sneha A.', quote:"I moved this to three different spots in my apartment because every corner looked better with it.", stars:5},
    {name:'Rahul M.', quote:"I genuinely look forward to sitting at my desk now. The warm light in the evening is something else.", stars:5},
    {name:'Priya K.', quote:"She called me the same day it arrived to say it was the most thoughtful gift she'd ever received.", stars:5}
  ];

  const riskReversal = product.riskReversal || ['Free Delivery', 'Gift-Ready Packaging', 'Premium Build Quality'];
  const urgency = product.urgency || 'Limited Stock Available — Your space has been waiting for this.';

  const benefitsHTML = benefits.map(b =>
    `<div style="background:#fff;padding:40px 30px;border-radius:12px;text-align:center;border:1px solid #EDE8DF;transition:box-shadow 0.3s;" onmouseover="this.style.boxShadow='0 20px 50px rgba(0,0,0,0.06)'" onmouseout="this.style.boxShadow='none'">
      <div style="font-size:2rem;margin-bottom:16px;">${b.icon}</div>
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:500;margin-bottom:12px;color:#2E2A25;">${b.title}</h4>
      <p style="font-size:0.9rem;color:#7A6F65;line-height:1.7;">${b.desc}</p>
    </div>`
  ).join('');

  const ingredientsHTML = ingredients.map(ing =>
    `<div style="background:#FAF7F2;padding:35px;border-radius:12px;display:flex;gap:20px;align-items:flex-start;">
      <div style="width:64px;height:64px;background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0;border:1px solid #EDE8DF;">${ing.icon}</div>
      <div>
        <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.25rem;font-weight:500;margin-bottom:8px;color:#2E2A25;">${ing.name}</h4>
        <p style="font-size:0.9rem;color:#7A6F65;line-height:1.7;">${ing.desc}</p>
      </div>
    </div>`
  ).join('');

  const stepsHTML = howToUse.map((s, i) =>
    `<div style="text-align:center;">
      <div style="font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;color:#C9A84C;margin-bottom:12px;font-weight:600;">STEP 0${i+1}</div>
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;font-weight:500;margin-bottom:12px;color:#2E2A25;">${s.step}</h4>
      <p style="font-size:0.9rem;color:#7A6F65;line-height:1.7;">${s.desc}</p>
    </div>`
  ).join('');

  const reviewsHTML = reviews.map(r =>
    `<div class="reveal-box" style="background:#fff;padding:50px 40px;border-radius:20px;border:1px solid #EDE8DF;position:relative;transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-6px)'" onmouseout="this.style.transform='translateY(0)'">
      <div style="position:absolute;top:20px;left:30px;font-family:'Cormorant Garamond',serif;font-size:4rem;color:#F0EBE3;line-height:1;z-index:0;">"</div>
      <div style="position:relative;z-index:1;">
        <div style="color:#C9A84C;font-size:1rem;letter-spacing:3px;margin-bottom:20px;">${'★'.repeat(r.stars)}</div>
        <p style="font-style:italic;font-size:1.05rem;color:#4A4440;line-height:1.8;margin-bottom:24px;font-family:'Cormorant Garamond',serif;">"${r.quote}"</p>
        <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;color:#7A6F65;font-weight:600;">— ${r.name}</div>
      </div>
    </div>`
  ).join('');

  const riskHTML = riskReversal.map(r => `<div style="display:flex;align-items:center;gap:10px;"><span style="color:#C9A84C;font-size:1.1rem;">✦</span><span style="font-size:0.85rem;letter-spacing:1px;font-weight:500;">${r}</span></div>`).join('');

  container.innerHTML = `
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <div style="font-family:'Inter',sans-serif;color:#2E2A25;background:transparent;overflow-x:hidden;">

      <!-- 1. HERO -->
      <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:0;min-height:90vh;margin-bottom:80px;">
        <div style="background:#FAF7F2;display:flex;align-items:center;justify-content:center;padding:60px;overflow:hidden;">
          <img src="${image}" alt="${name}"
            style="max-width:100%;max-height:600px;object-fit:contain;transition:transform 0.8s ease;"
            onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'"
            onerror="this.src='./assets/images/placeholder.jpg'">
        </div>
        <div style="background:#fff;display:flex;flex-direction:column;justify-content:center;padding:80px 60px;">
          <div style="font-size:0.7rem;letter-spacing:4px;text-transform:uppercase;color:#C9A84C;margin-bottom:20px;">Home Collection</div>
          <h1 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,4vw,3.5rem);font-weight:400;line-height:1.15;margin:0 0 20px;color:#2E2A25;">${name}</h1>
          <p style="font-size:1.05rem;color:#7A6F65;margin-bottom:30px;line-height:1.7;font-style:italic;">"${tagline}"</p>
          <div style="font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:400;margin-bottom:35px;color:#2E2A25;">&#8377;${price.toLocaleString('en-IN')}</div>
          <div style="margin-bottom:30px;padding:20px;background:#FAF7F2;border-radius:8px;border-left:3px solid #C9A84C;font-size:0.9rem;color:#4A4440;line-height:1.6;">
            ${riskHTML}
          </div>
          <div style="display:flex;flex-direction:column;gap:12px;">
            <button class="buy-btn"
              style="width:100%;padding:20px;background:#2E2A25;color:#F6F1EA;border:none;cursor:pointer;font-size:0.85rem;font-weight:600;letter-spacing:3px;text-transform:uppercase;transition:background 0.3s;border-radius:4px;"
              onmouseover="this.style.background='#C9A84C'" onmouseout="this.style.background='#2E2A25'"
              data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
              Add to Home
            </button>
            <button id="buy-now"
              style="width:100%;padding:20px;background:transparent;color:#2E2A25;border:1px solid #2E2A25;cursor:pointer;font-size:0.85rem;font-weight:600;letter-spacing:3px;text-transform:uppercase;transition:all 0.3s;border-radius:4px;"
              onmouseover="this.style.background='#FAF7F2'" onmouseout="this.style.background='transparent'">
              Buy Now
            </button>
          </div>
          <div style="margin-top:20px;font-size:0.85rem;color:#C9A84C;font-weight:600;line-height:1.5;">${urgency}</div>
        </div>
      </div>

      <!-- 2. HOOK — PROBLEM TO SOLUTION -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:80px 60px;background:#0a0a0a;border-radius:16px;">
        <div style="text-align:center;max-width:800px;margin:0 auto;">
          <div style="color:#C9A84C;font-size:1.2rem;letter-spacing:6px;margin-bottom:25px;">✦  ✦  ✦</div>
          <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:400;color:#F6F1EA;line-height:1.3;margin-bottom:30px;">${hook.headline}</h2>
          <p style="font-size:1.05rem;color:#888;line-height:1.9;margin-bottom:25px;">${hook.problem}</p>
          <div style="width:40px;height:1px;background:#C9A84C;margin:30px auto;"></div>
          <p style="font-size:1.1rem;color:#F6F1EA;line-height:1.9;font-style:italic;">${hook.solution}</p>
        </div>
      </div>

      <!-- 3. BENEFITS -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:0 40px;">
        <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,3.5vw,2.8rem);text-align:center;margin-bottom:50px;font-weight:400;color:#2E2A25;">What This Does For Your Space</h2>
        <div style="display:grid;grid-template-columns:repeat(${benefits.length},1fr);gap:24px;">
          ${benefitsHTML}
        </div>
      </div>

      <!-- 4. CRAFTSMANSHIP -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:0 40px;">
        <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,3.5vw,2.8rem);text-align:center;margin-bottom:50px;font-weight:400;color:#2E2A25;">Every Detail Is Deliberate</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">
          ${ingredientsHTML}
        </div>
      </div>

      <!-- 5. HOW TO USE -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:80px 60px;background:#FAF7F2;border-radius:16px;">
        <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,3.5vw,2.8rem);text-align:center;margin-bottom:60px;font-weight:400;color:#2E2A25;">From Box to Beautiful</h2>
        <div style="display:grid;grid-template-columns:repeat(${howToUse.length},1fr);gap:50px;max-width:900px;margin:0 auto;">
          ${stepsHTML}
        </div>
      </div>

      <!-- 6. REVIEWS -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:0 40px;">
        <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,3.5vw,2.8rem);text-align:center;margin-bottom:50px;font-weight:400;color:#2E2A25;">What Guests Say When They Walk In</h2>
        <div style="display:grid;grid-template-columns:repeat(${reviews.length},1fr);gap:30px;">
          ${reviewsHTML}
        </div>
      </div>

      <!-- 7. FINAL CTA -->
      <div class="reveal-box premium-cta-box" style="max-width:1200px;margin:0 auto;">
        <div style="color:#C9A84C;font-size:1.2rem;letter-spacing:6px;margin-bottom:25px;">✦</div>
        <h2>Your space is one decision away from looking exactly how you've always wanted it to.</h2>
        <p>Not after a renovation. Not after new furniture. Today. With this.</p>
        <button class="buy-btn"
          data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
          Elevate Your Space — &#8377;${price.toLocaleString('en-IN')}
        </button>
        <div style="margin-top:20px;font-size:0.85rem;color:#7A6F65;">Free Delivery · Gift-Ready Packaging · Limited Stock</div>
      </div>

    </div>
  `;

  setupProductButtons(product, name, price, image);
}
'''

before = content[:start_idx]
after = content[end_idx:]
new_content = before + new_block + after

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully patched renderSpaceProduct!")
