import re

file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new dynamic renderer for Style
new_renderer = """function renderStyleProduct(product, container) {
  const name = product.name || "Signature Statement Piece";
  const price = Number(product.price) || 0;
  const description = product.description || "Designed for those who lead, not follow.";
  const image = getImageUrl(product.mainImage || product.image);
  const tagline = product.tagline || "Where relaxed confidence meets sharp, timeless style.";

  // Dynamic fields with fallbacks
  const hook = product.hook || {
    headline: "The Man Who Walks In Doesn't Need to Introduce Himself.",
    problem: "Some men dress to be seen. Others dress to be remembered.",
    solution: "That's not arrogance. That's the quiet power of a man who looks composed, intentional, and effortlessly put-together."
  };

  const benefits = product.benefits || [
    {title: "Impeccable Look", desc: "A tailored silhouette that instantly elevates your profile.", icon: "✦"},
    {title: "Absolute Comfort", desc: "Engineered to move flawlessly with your body all day.", icon: "✦"},
    {title: "Precision Fit", desc: "Flattering every angle — made to drape perfectly.", icon: "✦"},
    {title: "Versatility", desc: "From boardroom mornings to after-dark occasions.", icon: "✦"}
  ];

  const materialText = product.materialText || "Crafted from premium woven blend — structured, elegant, breathable. Exceptionally soft. Second-skin comfort from first wear. Crafted to maintain shape and colour across seasons.";

  const howToUse = product.howToUse || [
    {step: "The Casual Edge", desc: "Pair with slim chinos and loafers."},
    {step: "Formal Dominance", desc: "Tuck into tailored trousers."},
    {step: "Evening Prestige", desc: "Half-tuck into black trousers."}
  ];

  const reviews = product.reviews || [
    {name: "Alexander D.", quote: "The compliments are endless. It gives me a confidence I can't describe.", stars: 5},
    {name: "Christian M.", quote: "I've never felt more attractive. The fit is exceptionally flattering.", stars: 5},
    {name: "Sebastian V.", quote: "Pure luxury. You feel the quality instantly. It changes how you carry yourself.", stars: 5}
  ];

  const urgency = product.urgency || "⚠️ Limited Pieces Available. Once these sell out, they're gone.";

  container.innerHTML = `
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <div style="background:transparent;color:#000;font-family:'Inter',sans-serif;overflow-x:hidden;">

      <!-- 1. HERO SECTION -->
      <section style="display:grid;grid-template-columns:55% 45%;min-height:100vh;">
        <!-- Left: Full-height product image -->
        <div style="height:100vh;position:sticky;top:0;overflow:hidden;">
          <img src="${image}" alt="${name}"
            style="width:100%;height:100%;object-fit:contain;object-position:center;padding:20px;background:#fff;"
            onerror="this.src='./assets/images/placeholder.jpg'">
        </div>
        <!-- Right: Product details -->
        <div style="display:flex;flex-direction:column;justify-content:center;padding:8% 10%;background:#fff;overflow-y:auto;max-height:100vh;">
          <div style="max-width:460px;">
            <div style="font-size:0.7rem;letter-spacing:4px;text-transform:uppercase;color:#aaa;margin-bottom:18px;">Exclusive Collection</div>
            <h1 style="font-family:'Playfair Display',serif;font-size:3rem;line-height:1.1;margin:0 0 12px;font-weight:400;letter-spacing:-1px;text-transform:uppercase;">${name}</h1>
            <p style="font-size:1rem;color:#888;margin-bottom:25px;letter-spacing:0.5px;font-style:italic;">"${tagline}"</p>
            <div style="font-family:'Playfair Display',serif;font-size:2.2rem;color:#000;margin-bottom:35px;font-weight:500;">&#8377;${price.toLocaleString('en-IN')}</div>

            <!-- Size Selector -->
            <div style="margin-bottom:28px;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
                <label style="font-size:0.75rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;">Select Size</label>
                <a href="#" style="font-size:0.72rem;color:#888;text-decoration:underline;letter-spacing:1px;">Size Guide</a>
              </div>
              <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">
                ${['S','M','L','XL'].map(sz => `<div onclick="document.querySelectorAll('.sz-btn').forEach(b=>{b.style.background='#fff';b.style.color='#000';b.style.borderColor='#E5E5E5'});this.style.background='#000';this.style.color='#fff';this.style.borderColor='#000'" class="sz-btn" style="height:52px;border:1px solid #E5E5E5;display:flex;align-items:center;justify-content:center;font-size:0.88rem;cursor:pointer;transition:all 0.25s;background:#fff;color:#000;">${sz}</div>`).join('')}
              </div>
            </div>

            <!-- CTAs -->
            <div style="display:flex;flex-direction:column;gap:14px;margin-bottom:35px;">
              <button class="buy-btn"
                style="width:100%;padding:20px;background:#000;color:#fff;border:none;cursor:pointer;font-size:0.85rem;font-weight:600;letter-spacing:3px;text-transform:uppercase;transition:all 0.3s;"
                onmouseover="this.style.background='#222'"
                onmouseout="this.style.background='#000'"
                data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
                Add to Cart
              </button>
              <button id="buy-now" style="width:100%;padding:20px;background:#fff;color:#000;border:1px solid #000;cursor:pointer;font-size:0.85rem;font-weight:600;letter-spacing:3px;text-transform:uppercase;transition:all 0.3s;"
                onmouseover="this.style.background='#f5f5f5'"
                onmouseout="this.style.background='#fff'">
                Buy Now
              </button>
            </div>
            
            <div style="margin-top: 15px; font-size: 0.85rem; color: #e74c3c; font-weight: 600; line-height: 1.5;">
              ${urgency}
            </div>
          </div>
        </div>
      </section>

      <!-- 3. STYLE IMPACT SECTION (HOOK) -->
      <section style="padding:130px 20px;text-align:center;background:#0a0a0a;color:#fff;">
        <div style="max-width:800px;margin:0 auto;">
          <div style="color:#C9A84C;font-size:1.4rem;letter-spacing:6px;margin-bottom:25px;">✦  ✦  ✦</div>
          <h2 style="font-family:'Playfair Display',serif;font-size:3.5rem;margin-bottom:35px;font-weight:400;line-height:1.2;letter-spacing:-1px;">${hook.headline}</h2>
          <p style="font-size:1.1rem;line-height:1.9;color:#bbb;font-weight:300;max-width:650px;margin:0 auto 30px;">
            ${hook.problem}
          </p>
          <p style="font-size:1.2rem;line-height:1.9;color:#fff;font-weight:400;max-width:650px;margin:0 auto;">
            ${hook.solution}
          </p>
        </div>
      </section>

      <!-- 4. BENEFITS SECTION -->
      <section style="padding:100px 40px;background:#fff;">
        <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(${benefits.length}, 1fr);gap:30px;">
          ${benefits.map(b=>`
            <div style="text-align:center;padding:45px 25px;border:1px solid #F0F0F0;transition:box-shadow 0.3s;" onmouseover="this.style.boxShadow='0 20px 40px rgba(0,0,0,0.06)'" onmouseout="this.style.boxShadow='none'">
              <div style="color:#C9A84C;font-size:1.8rem;margin-bottom:20px;">${b.icon}</div>
              <h4 style="font-family:'Playfair Display',serif;font-size:1.3rem;margin-bottom:14px;font-weight:500;">${b.title}</h4>
              <p style="font-size:0.95rem;color:#666;line-height:1.7;">${b.desc}</p>
            </div>
          `).join('')}
        </div>
      </section>

      <!-- 5. MATERIAL & QUALITY SECTION -->
      <section style="padding:100px 40px;background:#FAFAFA;">
        <div style="max-width:1000px;margin:0 auto;text-align:center;">
          <h2 style="font-family:'Playfair Display',serif;font-size:2.8rem;margin-bottom:50px;font-weight:400;">The Anatomy of Luxury</h2>
          <p style="font-size:1.1rem;color:#444;line-height:1.8;max-width:800px;margin:0 auto;">
            ${materialText}
          </p>
        </div>
      </section>

      <!-- 6. HOW TO STYLE SECTION -->
      <section style="padding:100px 40px;background:#fff;">
        <div style="max-width:1200px;margin:0 auto;">
          <h2 style="font-family:'Playfair Display',serif;font-size:2.8rem;text-align:center;margin-bottom:70px;font-weight:400;">Define the Moment</h2>
          <div style="display:grid;grid-template-columns:repeat(${howToUse.length},1fr);gap:25px;">
            ${howToUse.map((step, index) => `
              <div style="padding: 40px 30px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                <div style="font-size:0.8rem;text-transform:uppercase;letter-spacing:3px;color:#C9A84C;margin-bottom:15px;font-weight:700;">LOOK 0${index + 1}</div>
                <h4 style="font-family:'Playfair Display',serif;font-size:1.6rem;color:#111;margin-bottom:15px;font-weight:500;">${step.step}</h4>
                <p style="font-size:1rem;color:#555;line-height:1.7;">${step.desc}</p>
              </div>
            `).join('')}
          </div>
        </div>
      </section>

      <!-- 7. REVIEWS SECTION -->
      <section style="padding:100px 40px;background:transparent;text-align:center;">
        <div style="max-width:1200px;margin:0 auto;">
          <h2 style="font-family:'Playfair Display',serif;font-size:2.8rem;text-align:center;margin-bottom:70px;font-weight:400;color:#111;">The Verdict</h2>
          <div style="display:grid;grid-template-columns:repeat(${reviews.length},1fr);gap:40px;">
            ${reviews.map(r=>`
              <div class="reveal-box" style="background:#fff;padding:50px 30px;border:1px solid #eaeaea;border-radius:24px;box-shadow:0 10px 30px rgba(0,0,0,0.02);position:relative;transition:transform 0.4s ease;" onmouseover="this.style.transform='translateY(-6px)'" onmouseout="this.style.transform='translateY(0)'">
                <div style="position:absolute;top:-20px;left:50%;transform:translateX(-50%);font-family:'Playfair Display',serif;font-size:5rem;color:#f4f4f4;line-height:1;z-index:0;">“</div>
                <div style="position:relative;z-index:1;">
                  <div style="color:#C9A84C;letter-spacing:4px;margin-bottom:24px;font-size:1.1rem;">${'★'.repeat(r.stars)}${'☆'.repeat(5 - r.stars)}</div>
                  <p style="font-size:1.05rem;line-height:1.8;color:#444;margin-bottom:30px;font-family:'Playfair Display',serif;font-style:italic;">"${r.quote}"</p>
                  <div style="font-size:0.8rem;text-transform:uppercase;letter-spacing:2px;color:#888;font-weight:600;">— ${r.name}</div>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </section>

      <!-- 8. FINAL CTA SECTION -->
      <section class="reveal-box premium-cta-box">
        <div style="color:#C9A84C;font-size:1.2rem;letter-spacing:6px;margin-bottom:30px;">✦</div>
        <h2>The Best-Dressed Version of You Is One Decision Away.</h2>
        <p>You don't need a new wardrobe. You need the right piece in it. This is that piece.</p>
        <button class="buy-btn"
          data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
          Step Into Confidence - &#8377;${price.toLocaleString('en-IN')}
        </button>
      </section>

    </div>
  `;

  setupProductButtons(product, name, price, image);
}"""

pattern = re.compile(r'function renderStyleProduct\(product, container\) \{.*?(?=\n// ======================\n// Fitness \(Fit\) Renderer)', re.DOTALL | re.IGNORECASE)
new_content, count = pattern.subn(new_renderer, content)

if count == 1:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully patched renderStyleProduct!")
else:
    print(f"Failed to find the renderStyleProduct function block. Count: {count}")
