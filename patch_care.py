import re

file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new dynamic renderer
new_renderer = """function renderCareProduct(product, container) {
  const name = product.name || "Radiant Glow Serum";
  const price = Number(product.price) || 0;
  const description = product.description || "Experience the pinnacle of skincare science.";
  const image = getImageUrl(product.mainImage || product.image);
  const tagline = product.tagline || "For Luminous, Deeply Hydrated Skin";
  
  // Dynamic fields with fallbacks
  const hook = product.hook || {
    headline: "Dull, Dehydrated & Uneven Skin",
    problem: "Environmental stress and lack of moisture leave your skin looking tired.",
    solution: "Restore your natural luminosity with our targeted repair formula."
  };
  
  const benefits = product.benefits || [
    {title: "Instant Glow", desc: "Revitalizes dull skin.", icon: "✨"},
    {title: "Deep Hydration", desc: "Locks in moisture.", icon: "💧"},
    {title: "Velvet Finish", desc: "Smooths skin texture.", icon: "☁️"},
    {title: "Skin Repair", desc: "Strengthens skin barrier.", icon: "🛡️"}
  ];
  
  const ingredients = product.ingredients || [
    {name: "Pure Hyaluronic Acid", desc: "The ultimate hydrator.", icon: "🍃"},
    {name: "Vitamin C Complex", desc: "Brightens tone.", icon: "🍋"},
    {name: "Organic Aloe Extract", desc: "Calms inflammation.", icon: "🌿"},
    {name: "Active Peptides", desc: "Signals skin cells to repair.", icon: "🧪"}
  ];
  
  const howToUse = product.howToUse || [
    {step: "Cleanse", desc: "Wash face with warm water."},
    {step: "Apply", desc: "Massage drops onto face."},
    {step: "Absorb", desc: "Let sink in."},
    {step: "Repeat", desc: "Use daily."}
  ];
  
  const reviews = product.reviews || [
    {name: "Sarah J.", quote: "My skin has never felt this hydrated.", stars: 5},
    {name: "Michael R.", quote: "Clean, minimal, and actually works.", stars: 5},
    {name: "Amara K.", quote: "The perfect addition to my morning ritual.", stars: 5}
  ];

  const riskReversal = product.riskReversal || [
    "ALL SKIN TYPES",
    "NO HARMFUL CHEMICALS",
    "DERMATOLOGICALLY INSPIRED"
  ];
  
  const urgency = product.urgency || "HIGH DEMAND ALERT — STOCK IS MOVING FAST";

  container.innerHTML = `
    <div style="max-width: 1200px; margin: auto; font-family: 'Inter', sans-serif; color: #333; background: transparent; padding-bottom: 80px;">
      
      <!-- 1. HERO SECTION -->
      <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 60px; align-items: start; padding: 40px 0;">
        <div style="background: #fdfaf5; border-radius: 4px; padding: 20px; text-align: center;">
          <img src="${image}" alt="${name}" 
            style="width: 100%; max-height: 600px; object-fit: contain;"
            onerror="this.src='./assets/images/placeholder.jpg'">
        </div>
        <div style="padding-top: 20px;">
          <h1 style="font-family: 'Playfair Display', serif; font-size: 3rem; margin: 0 0 10px; font-weight: 500; color: #1a1a1a;">${name}</h1>
          <p style="font-size: 1.2rem; color: #c9a84c; font-weight: 600; margin-bottom: 15px; letter-spacing: 0.5px;">${tagline}</p>
          <div style="font-size: 2.2rem; font-weight: 400; margin-bottom: 20px; color: #111;">₹${price.toLocaleString('en-IN')}</div>
          
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 30px; padding: 12px 15px; background: #f9f9f9; border-radius: 4px; border-left: 3px solid #c9a84c;">
            <span style="font-size: 1.2rem;">✓</span>
            <span style="font-size: 0.95rem; font-weight: 500;">Dermatologically Tested • 100% Safe Formula</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px;">
            <button class="buy-btn"
              style="width: 100%; padding: 18px; background: #1a1a1a; color: #fff; border: none; cursor: pointer; border-radius: 4px; font-size: 1.1rem; font-weight: 600; transition: background 0.3s;"
              onmouseover="this.style.background='#c9a84c'"
              onmouseout="this.style.background='#1a1a1a'"
              data-id="${product._id}"
              data-name="${name}"
              data-price="${price}"
              data-img="${image}">
              ADD TO CART
            </button>
            <button id="buy-now"
              style="width: 100%; padding: 18px; background: #fff; color: #1a1a1a; border: 1px solid #1a1a1a; cursor: pointer; border-radius: 4px; font-size: 1.1rem; font-weight: 600; transition: all 0.3s;"
              onmouseover="this.style.background='#f9f9f9'"
              onmouseout="this.style.background='#fff'">
              BUY NOW
            </button>
          </div>
          
          <div style="margin-top: 20px; font-size: 0.9rem; color: #e74c3c; font-weight: 600; display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.2rem;">🔥</span> ${urgency}
          </div>
        </div>
      </div>

      <!-- 3. PROBLEM → RESULT (HOOK) -->
      <div style="background: #fdfaf5; padding: 60px 40px; border-radius: 8px; margin-bottom: 80px;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; text-align: center; margin-bottom: 30px; color: #111;">${hook.headline}</h2>
        <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 40px; align-items: center;">
            <div style="text-align: center;">
              <div style="font-size: 0.9rem; text-transform: uppercase; color: #888; margin-bottom: 10px;">The Reality</div>
              <p style="font-size: 1.05rem; color: #555; line-height: 1.8;">${hook.problem}</p>
            </div>
            <div style="font-size: 2.5rem; color: #c9a84c;">⟶</div>
            <div style="text-align: center;">
              <div style="font-size: 0.9rem; text-transform: uppercase; color: #c9a84c; margin-bottom: 10px;">The Transformation</div>
              <p style="font-size: 1.05rem; color: #111; line-height: 1.8;">${hook.solution}</p>
            </div>
        </div>
      </div>

      <!-- 4. BENEFITS SECTION -->
      <div style="display: grid; grid-template-columns: repeat(${benefits.length}, 1fr); gap: 25px; margin-bottom: 80px;">
        ${benefits.map(b => `
            <div style="background: #fff; padding: 30px; border: 1px solid #f0f0f0; border-radius: 8px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
              <div style="font-size: 1.8rem; margin-bottom: 15px;">${b.icon || '✨'}</div>
              <h4 style="margin-bottom: 10px; color: #111;">${b.title}</h4>
              <p style="font-size: 0.9rem; color: #555; line-height: 1.6;">${b.desc}</p>
            </div>
        `).join('')}
      </div>

      <!-- 5. INGREDIENTS SECTION -->
      <div style="margin-bottom: 80px;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; text-align: center; margin-bottom: 40px; color: #111;">What's Inside & Why It Works</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
          ${ingredients.map(ing => `
            <div style="background: #fdfaf5; padding: 30px; border-radius: 8px; display: flex; gap: 20px; align-items: center;">
              <div style="width: 80px; height: 80px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; flex-shrink: 0;">${ing.icon || '🌿'}</div>
              <div>
                <h4 style="margin-bottom: 8px; color: #111; font-size: 1.1rem;">${ing.name}</h4>
                <p style="font-size: 0.95rem; color: #555; line-height: 1.6;">${ing.desc}</p>
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- 6. HOW TO USE SECTION -->
      <div style="background: #fff; border: 1px solid #eee; padding: 60px 40px; border-radius: 8px; margin-bottom: 80px;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; text-align: center; margin-bottom: 40px; color: #111;">How To Use</h2>
        <div style="display: grid; grid-template-columns: repeat(${howToUse.length}, 1fr); gap: 30px;">
          ${howToUse.map((step, index) => `
            <div style="text-align: center;">
              <div style="font-weight: 700; color: #c9a84c; margin-bottom: 10px;">STEP 0${index + 1}</div>
              <h4 style="margin-bottom: 10px; color: #111; font-size: 1.2rem;">${step.step}</h4>
              <p style="font-size: 0.95rem; color: #555; line-height: 1.6;">${step.desc}</p>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- 7. SOCIAL PROOF SECTION -->
      <div style="margin-bottom: 80px;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; text-align: center; margin-bottom: 40px; color: #111;">Real Stories</h2>
        <div style="display: grid; grid-template-columns: repeat(${reviews.length}, 1fr); gap: 30px;">
          ${reviews.map(r => `
            <div style="background: #fdfaf5; padding: 30px; border-radius: 8px;">
              <div style="color: #f39c12; margin-bottom: 15px; font-size: 1.2rem;">${'★'.repeat(r.stars)}${'☆'.repeat(5 - r.stars)}</div>
              <p style="font-style: italic; margin-bottom: 20px; font-size: 1.05rem; color: #444; line-height: 1.7;">"${r.quote}"</p>
              <div style="font-weight: 700; font-size: 0.9rem; color: #888; text-transform: uppercase;">— ${r.name}</div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- 8. SAFETY / TRUST SECTION -->
      <div style="background: #111; color: #fff; padding: 30px; border-radius: 4px; display: flex; justify-content: center; flex-wrap: wrap; gap: 30px; margin-bottom: 80px; font-size: 0.85rem; letter-spacing: 1px; font-weight: 500; text-transform: uppercase;">
        ${riskReversal.map(r => `<div>✓ ${r}</div>`).join('')}
      </div>

      <!-- 9. FINAL CTA SECTION -->
      <div class="reveal-box premium-cta-box" style="margin-top: 80px;">
        <h2>Your skin has been asking for this.</h2>
        <p>One tube. One daily habit. One version of you that walks into every room with quiet, effortless confidence.</p>
        <button class="buy-btn"
          data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
          Claim Your Glow - &#8377;${price.toLocaleString('en-IN')}
        </button>
        <div style="margin-top: 20px; font-size: 0.85rem; color: var(--cat-btn-color); opacity: 0.7;">Free delivery on orders above ₹499 · Easy 15-day returns</div>
      </div>

    </div>
  `;

  setupProductButtons(product, name, price, image);
}"""

pattern = re.compile(r'function renderCareProduct\(product, container\) \{.*?(?=\n// ======================\n// 👔 FASHION \(STYLE\) RENDERER)', re.DOTALL)
new_content, count = pattern.subn(new_renderer, content)

if count == 1:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully patched renderCareProduct!")
else:
    print(f"Failed to find the renderCareProduct function block. Count: {count}")
