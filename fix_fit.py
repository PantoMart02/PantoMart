import re

with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Find exact boundaries of renderFitProduct ──────────────────────────────
fit_start = content.find('// Fitness (Fit) Renderer')
if fit_start == -1:
    fit_start = content.find('function renderFitProduct')
space_start = content.find('// Home Decor (Space) Renderer')
if space_start == -1:
    space_start = content.find('function renderSpaceProduct')

old_fit = content[fit_start:space_start]
backticks = old_fit.count('`')
print(f'Old renderFitProduct backtick count: {backticks}')

# The .map() template literals inside the main template string must use
# escaped backticks or be replaced with string concatenation.
# Strategy: rewrite the entire function as a clean string that avoids nested
# template literal conflicts by using Array.join() with string concat instead.

NEW_FIT = r'''// ======================
// Fitness (Fit) Renderer — Apple / High-Performance Edition
// ======================
function renderFitProduct(product, container) {
  const name = product.name || 'Elite Performance Gear';
  const price = Number(product.price) || 0;
  const description = product.description || 'Forged for those who push past their limits.';
  const image = getImageUrl(product.mainImage || product.image);

  const stripItems = [
    {icon:'⚡',title:'Strength',desc:'Max force output with every rep'},
    {icon:'🎯',title:'Control',desc:'Engineered grip, zero slippage'},
    {icon:'🛡️',title:'Durability',desc:'Built for a thousand sessions'},
    {icon:'⚙️',title:'Efficiency',desc:'Every movement, amplified'},
  ];

  const engItems = [
    {icon:'✦',title:'Precision-Engineered Grip',desc:'Micro-textured surface increases friction by 40% — maximum transfer, zero slip.'},
    {icon:'◈',title:'Aero-Mesh Construction',desc:'Active airflow channels prevent thermal fatigue so you can train longer.'},
    {icon:'◉',title:'Impact Distribution',desc:'Internal load-sharing structure disperses force evenly, protecting your joints.'},
    {icon:'⊕',title:'Built for Consistency',desc:'Maintains structural integrity after 10,000+ reps — same on day one as day 1000.'},
    {icon:'⟁',title:'Adaptive Fit',desc:'Contoured ergonomics follow your natural movement — pure motion, no resistance.'},
    {icon:'◫',title:'Minimal Weight',desc:'Every gram is justified. Nothing extra. Nothing missing. Just what performance demands.'},
  ];

  const outcomes = [
    {stat:'+34%',title:'Stronger',desc:'Average force output increase reported within 6 weeks.'},
    {stat:'2×',title:'More Consistent',desc:'Users complete more sessions — better gear means fewer reasons to stop.'},
    {stat:'93%',title:'More Disciplined',desc:'Of users reported measurable improvement in their training discipline.'},
  ];

  const steps = [
    {num:'01',title:'Set Up',desc:'Integrate into your training environment in under 60 seconds.'},
    {num:'02',title:'Execute',desc:'Push harder. The gear absorbs stress so your body does not have to.'},
    {num:'03',title:'Evolve',desc:'Track progress. Increase intensity. Repeat until elite.'},
  ];

  const reviews = [
    {q:'Nothing else comes close. The grip alone changed how I lift. My PRs have gone up three weeks straight.',name:'Marcus T.',title:'Powerlifter'},
    {q:'Finally equipment that disappears during training. No adjustments, no distraction. Pure performance.',name:'Priya A.',title:'CrossFit Athlete'},
    {q:'I was skeptical. Two sessions in, I understood. The consistency it gives you is unlike anything.',name:'Rahul S.',title:'Marathon Runner'},
  ];

  const stripHTML = stripItems.map(function(i) {
    return '<div class="fit-strip-item"><span class="icon">' + i.icon + '</span><h3>' + i.title + '</h3><p>' + i.desc + '</p></div>';
  }).join('');

  const engHTML = engItems.map(function(d) {
    return '<div class="fit-eng-item"><div class="icon">' + d.icon + '</div><h3>' + d.title + '</h3><p>' + d.desc + '</p></div>';
  }).join('');

  const outcomeHTML = outcomes.map(function(o) {
    return '<div class="fit-outcome-cell"><span class="stat">' + o.stat + '</span><h3>' + o.title + '</h3><p>' + o.desc + '</p></div>';
  }).join('');

  const stepsHTML = steps.map(function(s) {
    return '<div class="fit-step"><div class="step-img"><img src="' + image + '" alt="step ' + s.num + '" onerror="this.src=\'./assets/images/placeholder.jpg\'"></div><span class="num">Step ' + s.num + '</span><h3>' + s.title + '</h3><p>' + s.desc + '</p></div>';
  }).join('');

  const reviewsHTML = reviews.map(function(r) {
    return '<div class="fit-review"><span class="stars">★★★★★</span><blockquote>"' + r.q + '"</blockquote><div class="reviewer"><span></span><div><div style="font-weight:600;font-size:0.82rem;">' + r.name + '</div><div>' + r.title + '</div></div></div></div>';
  }).join('');

  container.innerHTML = `
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
      .fit-page * { box-sizing: border-box; margin: 0; padding: 0; }
      .fit-page { background: #FFFFFF; color: #0A0A0A; font-family: 'Inter', sans-serif; overflow-x: hidden; }
      .fit-hero { position: relative; width: 100%; height: 100vh; background: #F5F5F7; overflow: hidden; display: flex; align-items: center; }
      .fit-hero-bg { position: absolute; inset: 0; }
      .fit-hero-bg img { width: 100%; height: 100%; object-fit: cover; object-position: center 20%; filter: brightness(0.6); transition: transform 10s ease; display: block; }
      .fit-hero:hover .fit-hero-bg img { transform: scale(1.04); }
      .fit-hero-content { position: relative; z-index: 2; padding: 0 8%; max-width: 800px; color: #fff; }
      .fit-hero-label { font-size: 0.72rem; letter-spacing: 4px; text-transform: uppercase; opacity: 0.6; margin-bottom: 24px; display: block; }
      .fit-hero h1 { font-size: clamp(3rem,7vw,6.5rem); font-weight: 800; line-height: 1.0; letter-spacing: -3px; margin-bottom: 24px; }
      .fit-hero h1 span { color: #007AFF; }
      .fit-hero p { font-size: 1.15rem; font-weight: 300; opacity: 0.75; max-width: 420px; line-height: 1.7; margin-bottom: 48px; }
      .fit-hero-price { font-size: 1.1rem; font-weight: 500; opacity: 0.6; margin-bottom: 36px; }
      .fit-hero-cta { display: inline-flex; align-items: center; gap: 10px; padding: 18px 44px; background: #007AFF; color: #fff; font-size: 0.88rem; font-weight: 600; letter-spacing: 0.5px; border: none; cursor: pointer; transition: all 0.35s; border-radius: 50px; font-family: 'Inter', sans-serif; }
      .fit-hero-cta:hover { background: #0063CC; transform: translateY(-3px); box-shadow: 0 20px 40px rgba(0,122,255,0.35); }
      .fit-strip { background: #F5F5F7; padding: 0 8%; display: grid; grid-template-columns: repeat(4,1fr); border-top: 1px solid #E8E8E8; border-bottom: 1px solid #E8E8E8; }
      .fit-strip-item { padding: 50px 30px; text-align: center; border-right: 1px solid #E8E8E8; transition: background 0.3s; }
      .fit-strip-item:last-child { border-right: none; }
      .fit-strip-item:hover { background: #EBEBED; }
      .fit-strip-item .icon { font-size: 2rem; margin-bottom: 16px; display: block; }
      .fit-strip-item h3 { font-size: 1.05rem; font-weight: 700; letter-spacing: -0.3px; margin-bottom: 8px; }
      .fit-strip-item p { font-size: 0.82rem; color: #6E6E73; line-height: 1.6; }
      .fit-motion { position: relative; height: 85vh; overflow: hidden; background: #000; }
      .fit-motion img { width: 100%; height: 100%; object-fit: cover; opacity: 0.75; transition: transform 8s ease; filter: contrast(1.1); display: block; }
      .fit-motion:hover img { transform: scale(1.04); }
      .fit-motion-label { position: absolute; bottom: 8%; right: 8%; color: #fff; text-align: right; }
      .fit-motion-label .eyebrow { font-size: 0.7rem; letter-spacing: 3px; text-transform: uppercase; opacity: 0.5; margin-bottom: 10px; display: block; }
      .fit-motion-label h2 { font-size: clamp(1.8rem,3vw,3rem); font-weight: 700; letter-spacing: -1px; line-height: 1.1; }
      .fit-why { padding: 130px 8%; background: #fff; }
      .fit-why-head { text-align: center; max-width: 600px; margin: 0 auto 80px; }
      .fit-why-head .eyebrow { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 20px; display: block; }
      .fit-why-head h2 { font-size: clamp(2rem,4vw,3.5rem); font-weight: 800; letter-spacing: -2px; line-height: 1.1; }
      .fit-why-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; max-width: 1100px; margin: 0 auto; }
      .fit-why-cell { padding: 60px 50px; }
      .fit-why-cell.problem { background: #F5F5F7; }
      .fit-why-cell.solution { background: #0A0A0A; color: #fff; }
      .fit-why-cell .tag { font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 22px; display: block; }
      .fit-why-cell.problem .tag { color: #6E6E73; }
      .fit-why-cell.solution .tag { color: #007AFF; }
      .fit-why-cell h3 { font-size: clamp(1.4rem,2.5vw,2rem); font-weight: 700; letter-spacing: -0.5px; line-height: 1.25; margin-bottom: 20px; }
      .fit-why-cell.problem h3 { color: #6E6E73; }
      .fit-why-cell p { font-size: 0.9rem; line-height: 1.8; }
      .fit-why-cell.problem p { color: #8E8E93; }
      .fit-why-cell.solution p { color: #AEAEB2; }
      .fit-eng { padding: 130px 8%; background: #F5F5F7; }
      .fit-eng-head { margin-bottom: 80px; }
      .fit-eng-head .eyebrow { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 20px; display: block; }
      .fit-eng-head h2 { font-size: clamp(2rem,4vw,3.2rem); font-weight: 800; letter-spacing: -2px; max-width: 500px; line-height: 1.1; }
      .fit-eng-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
      .fit-eng-item { background: #fff; padding: 50px 40px; transition: transform 0.4s, box-shadow 0.4s; }
      .fit-eng-item:hover { transform: translateY(-8px); box-shadow: 0 30px 60px rgba(0,0,0,0.08); }
      .fit-eng-item .icon { width: 48px; height: 48px; background: #007AFF; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; margin-bottom: 28px; color: #fff; }
      .fit-eng-item h3 { font-size: 1.15rem; font-weight: 700; letter-spacing: -0.3px; margin-bottom: 14px; }
      .fit-eng-item p { font-size: 0.88rem; color: #6E6E73; line-height: 1.8; }
      .fit-outcome { padding: 130px 8%; background: #0A0A0A; color: #fff; }
      .fit-outcome-head { text-align: center; max-width: 600px; margin: 0 auto 90px; }
      .fit-outcome-head .eyebrow { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 20px; display: block; }
      .fit-outcome-head h2 { font-size: clamp(2rem,4vw,3.5rem); font-weight: 800; letter-spacing: -2px; line-height: 1.1; }
      .fit-outcome-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 1px; }
      .fit-outcome-cell { padding: 60px 40px; text-align: center; background: #111; transition: background 0.3s; }
      .fit-outcome-cell:hover { background: #1A1A1A; }
      .fit-outcome-cell .stat { font-size: clamp(3rem,6vw,5rem); font-weight: 900; letter-spacing: -3px; color: #007AFF; display: block; margin-bottom: 12px; line-height: 1; }
      .fit-outcome-cell h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 12px; }
      .fit-outcome-cell p { font-size: 0.85rem; color: #6E6E73; line-height: 1.7; }
      .fit-howto { padding: 130px 8%; background: #fff; }
      .fit-howto-head { text-align: center; max-width: 500px; margin: 0 auto 80px; }
      .fit-howto-head h2 { font-size: clamp(2rem,3.5vw,3rem); font-weight: 800; letter-spacing: -1.5px; }
      .fit-howto-steps { display: grid; grid-template-columns: repeat(3,1fr); gap: 60px; max-width: 900px; margin: 0 auto; }
      .fit-step { text-align: center; }
      .fit-step .step-img { width: 100%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; margin-bottom: 30px; border: 3px solid #F5F5F7; }
      .fit-step .step-img img { width: 100%; height: 100%; object-fit: cover; display: block; }
      .fit-step .num { font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 10px; display: block; }
      .fit-step h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 10px; }
      .fit-step p { font-size: 0.85rem; color: #6E6E73; line-height: 1.7; }
      .fit-social { padding: 100px 8%; background: #F5F5F7; }
      .fit-social-head { text-align: center; margin-bottom: 70px; }
      .fit-social-head h2 { font-size: clamp(1.8rem,3vw,2.5rem); font-weight: 800; letter-spacing: -1px; }
      .fit-social-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }
      .fit-review { background: #fff; padding: 45px 40px; transition: transform 0.3s; }
      .fit-review:hover { transform: translateY(-5px); }
      .fit-review .stars { color: #007AFF; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 20px; display: block; }
      .fit-review blockquote { font-size: 1.02rem; font-weight: 500; line-height: 1.6; margin-bottom: 24px; letter-spacing: -0.2px; }
      .fit-review .reviewer { font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; color: #6E6E73; display: flex; align-items: center; gap: 12px; }
      .fit-review .reviewer > span { display: inline-block; width: 32px; height: 32px; background: #E8E8E8; border-radius: 50%; flex-shrink: 0; }
      .fit-final { padding: 160px 8%; background: #fff; text-align: center; }
      .fit-final h2 { font-size: clamp(2.5rem,6vw,5.5rem); font-weight: 900; letter-spacing: -3px; line-height: 1.0; margin-bottom: 30px; }
      .fit-final h2 .blue { color: #007AFF; }
      .fit-final p { font-size: 1.1rem; color: #6E6E73; margin-bottom: 55px; font-weight: 300; }
      .fit-final-price { font-size: 2.5rem; font-weight: 700; letter-spacing: -1px; margin-bottom: 50px; }
      .fit-final-btns { display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }
      .fit-btn-primary { padding: 20px 55px; background: #007AFF; color: #fff; font-size: 0.9rem; font-weight: 600; border: none; cursor: pointer; border-radius: 50px; transition: all 0.35s; font-family: 'Inter', sans-serif; }
      .fit-btn-primary:hover { background: #0063CC; transform: translateY(-3px); box-shadow: 0 20px 40px rgba(0,122,255,0.3); }
      .fit-btn-secondary { padding: 20px 55px; background: transparent; color: #007AFF; font-size: 0.9rem; font-weight: 600; border: 1.5px solid #007AFF; cursor: pointer; border-radius: 50px; transition: all 0.35s; font-family: 'Inter', sans-serif; }
      .fit-btn-secondary:hover { background: rgba(0,122,255,0.06); transform: translateY(-3px); }
    </style>

    <div class="fit-page">

      <!-- 1. HERO -->
      <div class="fit-hero">
        <div class="fit-hero-bg">
          <img src="${image}" alt="${name}" onerror="this.src='./assets/images/placeholder.jpg'">
        </div>
        <div class="fit-hero-content">
          <span class="fit-hero-label">Performance Series</span>
          <h1>Built for<br><span>Performance.</span></h1>
          <p>${description}</p>
          <div class="fit-hero-price">&#8377;${price.toLocaleString('en-IN')}</div>
          <button class="fit-hero-cta buy-btn"
            data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
            Upgrade Your Training &#8594;
          </button>
        </div>
      </div>

      <!-- 2. PERFORMANCE STRIP -->
      <div class="fit-strip">${stripHTML}</div>

      <!-- 3. PRODUCT IN MOTION -->
      <div class="fit-motion">
        <img src="${image}" alt="Product in use" onerror="this.src='./assets/images/placeholder.jpg'">
        <div class="fit-motion-label">
          <span class="eyebrow">In Action</span>
          <h2>${name}<br>at full capacity.</h2>
        </div>
      </div>

      <!-- 4. WHY IT MATTERS -->
      <div class="fit-why">
        <div class="fit-why-head">
          <span class="eyebrow">Why it matters</span>
          <h2>The gap between good and elite is your equipment.</h2>
        </div>
        <div class="fit-why-grid">
          <div class="fit-why-cell problem">
            <span class="tag">The Problem</span>
            <h3>Weak grip leads to reduced performance and wasted sessions.</h3>
            <p>Standard equipment fights you. Energy leaks out. Progress stalls. You plateau — not because of your body, but because of what's in your hands.</p>
          </div>
          <div class="fit-why-cell solution">
            <span class="tag">The Solution</span>
            <h3>Precision engineering that converts every effort into result.</h3>
            <p>Designed to disappear — so your focus stays entirely on your performance. Better control. Better output. Better you, every single session.</p>
          </div>
        </div>
      </div>

      <!-- 5. ENGINEERED DETAILS -->
      <div class="fit-eng">
        <div class="fit-eng-head">
          <span class="eyebrow">Engineered Details</span>
          <h2>Precision built for one purpose.</h2>
        </div>
        <div class="fit-eng-grid">${engHTML}</div>
      </div>

      <!-- 6. PERFORMANCE OUTCOME -->
      <div class="fit-outcome">
        <div class="fit-outcome-head">
          <span class="eyebrow">What you become</span>
          <h2>The results speak for themselves.</h2>
        </div>
        <div class="fit-outcome-row">${outcomeHTML}</div>
      </div>

      <!-- 7. HOW TO USE -->
      <div class="fit-howto">
        <div class="fit-howto-head">
          <h2>Three steps. One system.</h2>
        </div>
        <div class="fit-howto-steps">${stepsHTML}</div>
      </div>

      <!-- 8. SOCIAL PROOF -->
      <div class="fit-social">
        <div class="fit-social-head">
          <h2>Trusted by athletes who refuse to settle.</h2>
        </div>
        <div class="fit-social-grid">${reviewsHTML}</div>
      </div>

      <!-- 9. FINAL CTA -->
      <div class="fit-final">
        <h2>Train Better.<br><span class="blue">Perform Better.</span></h2>
        <p>Your best session is the next one. Make it count.</p>
        <div class="fit-final-price">&#8377;${price.toLocaleString('en-IN')}</div>
        <div class="fit-final-btns">
          <button class="fit-btn-primary buy-btn"
            data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
            Add to Cart
          </button>
          <button class="fit-btn-secondary">Learn More</button>
        </div>
      </div>

    </div>
  `;

  setupProductButtons(product, name, price, image);
}

'''

# Replace everything from renderFitProduct to renderSpaceProduct
new_content = content[:fit_start] + NEW_FIT + content[space_start:]

with open(r'assets\js\product.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Written successfully.')

# Verify syntax with node
import subprocess
result = subprocess.run(['node', '--check', r'assets\js\product.js'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax check: PASSED')
else:
    print('Syntax check: FAILED')
    print(result.stderr[:500])
