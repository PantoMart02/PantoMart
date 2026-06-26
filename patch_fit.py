file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '// ======================\n// Fitness (Fit) Renderer'
end_marker = '\n// Home Decor (Space) Renderer'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

print(f"Start: {start_idx}, End: {end_idx}")

new_block = r'''// ======================
// Fitness (Fit) Renderer — Dynamic Edition
// ======================
function renderFitProduct(product, container) {
  const name = product.name || 'Elite Performance Gear';
  const price = Number(product.price) || 0;
  const image = getImageUrl(product.mainImage || product.image);
  const tagline = product.tagline || "Engineered for the athlete who doesn't make excuses.";

  const hook = product.hook || {
    headline: "Your wrists are giving up before your muscles do.",
    problem: "You're mid-set. Weight is loaded. Mentally locked in. Then your wrists buckle. You're not weak. You're unsupported.",
    solution: "You load the bar heavier than you ever have. Your grip is iron. Your wrists don't flinch. That's what proper support feels like."
  };

  const benefits = product.benefits || [
    {icon:'⚡',title:'Strength',desc:'Max force output with every rep'},
    {icon:'🎯',title:'Control',desc:'Engineered grip, zero slippage'},
    {icon:'🛡️',title:'Durability',desc:'Built for a thousand sessions'},
    {icon:'⚙️',title:'Efficiency',desc:'Every movement, amplified'},
  ];

  const features = product.features || [
    {icon:'✦',title:'Precision-Engineered',desc:'Micro-textured surface — maximum transfer, zero slip.'},
    {icon:'✦',title:'Thermoregulated',desc:'Advanced materials dissipate heat faster than standard fabrics.'},
    {icon:'✦',title:'Biomechanical Alignment',desc:'Locks joints into their strongest natural position.'},
  ];

  const howToUse = product.howToUse || [
    {step:'01',title:'Set Up',desc:'Integrate into your training environment in under 60 seconds.'},
    {step:'02',title:'Execute',desc:'Push harder. The gear absorbs stress so your body does not have to.'},
    {step:'03',title:'Evolve',desc:'Track progress. Increase intensity. Repeat until elite.'},
  ];

  const reviews = product.reviews || [
    {q:'Nothing else comes close. My PRs have gone up three weeks straight.',name:'Marcus T.',title:'Powerlifter'},
    {q:'Equipment that disappears during training. Pure performance.',name:'Priya A.',title:'CrossFit Athlete'},
    {q:'Two sessions in, I understood. The consistency it gives is unlike anything.',name:'Rahul S.',title:'Marathon Runner'},
  ];

  const urgency = product.urgency || "Stop leaving reps behind. Upgrade today.";

  const stripHTML = benefits.map(function(i) {
    return '<div class="fit-strip-item"><span class="icon">' + (i.icon||'') + '</span><h3>' + i.title + '</h3><p>' + i.desc + '</p></div>';
  }).join('');

  const engHTML = features.map(function(d) {
    return '<div class="fit-eng-item"><div class="fit-eng-icon">' + (d.icon||'') + '</div><h3>' + d.title + '</h3><p>' + d.desc + '</p></div>';
  }).join('');

  const stepsHTML = howToUse.map(function(s) {
    return '<div class="fit-step"><div class="fit-step-img"><img src="' + image + '" alt="' + s.step + '" onerror="this.src=\'./assets/images/placeholder.jpg\'"></div><span class="fit-step-num">Step ' + s.step + '</span><h3>' + s.title + '</h3><p>' + s.desc + '</p></div>';
  }).join('');

  const reviewsHTML = reviews.map(function(r) {
    return '<div class="fit-review"><span class="fit-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><blockquote>"' + r.q + '"</blockquote><div class="fit-reviewer"><span class="fit-avatar"></span><div><div class="fit-rname">' + r.name + '</div><div class="fit-rtitle">' + (r.title||'') + '</div></div></div></div>';
  }).join('');

  const numBenefits = benefits.length;
  const numFeatures = features.length;
  const numSteps = howToUse.length;

  container.innerHTML = `
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
      .fit-page * { box-sizing: border-box; margin: 0; padding: 0; }
      .fit-page { background: transparent; color: #0A0A0A; font-family: 'Inter', sans-serif; overflow-x: hidden; }
      .fit-hero { position: relative; width: 100%; height: 100vh; background: #F5F5F7; overflow: hidden; display: flex; align-items: center; }
      .fit-hero-bg { position: absolute; inset: 0; }
      .fit-hero-bg img { width: 100%; height: 100%; object-fit: contain; background: #111; padding: 40px; object-position: center; filter: brightness(0.85); transition: transform 10s ease; display: block; }
      .fit-hero:hover .fit-hero-bg img { transform: scale(1.04); }
      .fit-hero-content { position: relative; z-index: 2; padding: 0 8%; max-width: 800px; color: #fff; }
      .fit-hero-label { font-size: 0.72rem; letter-spacing: 4px; text-transform: uppercase; opacity: 0.6; margin-bottom: 24px; display: block; }
      .fit-hero h1 { font-size: clamp(2.5rem,6vw,5.5rem); font-weight: 800; line-height: 1.05; letter-spacing: -2px; margin-bottom: 24px; }
      .fit-hero h1 span { color: #007AFF; }
      .fit-hero-tagline { font-size: 1.1rem; font-weight: 300; opacity: 0.75; max-width: 420px; line-height: 1.7; margin-bottom: 40px; }
      .fit-hero-price { font-size: 1.1rem; font-weight: 500; opacity: 0.6; margin-bottom: 36px; }
      .fit-hero-cta { display: inline-flex; align-items: center; gap: 10px; padding: 18px 44px; background: #007AFF; color: #fff; font-size: 0.88rem; font-weight: 600; border: none; cursor: pointer; transition: all 0.35s; border-radius: 50px; font-family: 'Inter', sans-serif; }
      .fit-hero-cta:hover { background: #0063CC; transform: translateY(-3px); box-shadow: 0 20px 40px rgba(0,122,255,0.35); }
      .fit-strip { background: #F5F5F7; padding: 0 8%; display: grid; grid-template-columns: repeat(${numBenefits},1fr); border-top: 1px solid #E8E8E8; border-bottom: 1px solid #E8E8E8; }
      .fit-strip-item { padding: 50px 30px; text-align: center; border-right: 1px solid #E8E8E8; transition: background 0.3s; }
      .fit-strip-item:last-child { border-right: none; }
      .fit-strip-item:hover { background: #EBEBED; }
      .fit-strip-item .icon { font-size: 2rem; margin-bottom: 16px; display: block; }
      .fit-strip-item h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 8px; color: #0A0A0A; }
      .fit-strip-item p { font-size: 0.82rem; color: #6E6E73; line-height: 1.6; }
      .fit-why { padding: 130px 8%; background: #fff; }
      .fit-why-head { text-align: center; max-width: 800px; margin: 0 auto 80px; }
      .fit-why-eyebrow { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 20px; display: block; }
      .fit-why-head h2 { font-size: clamp(1.8rem,4vw,3rem); font-weight: 800; letter-spacing: -1.5px; line-height: 1.2; color: #0A0A0A; }
      .fit-why-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; max-width: 1100px; margin: 0 auto; }
      .fit-why-cell { padding: 60px 50px; }
      .fit-why-cell.problem { background: #F5F5F7; }
      .fit-why-cell.solution { background: #0A0A0A; color: #fff; }
      .fit-why-cell .tag { font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 22px; display: block; }
      .fit-why-cell.problem .tag { color: #6E6E73; }
      .fit-why-cell.solution .tag { color: #007AFF; }
      .fit-why-cell h3 { font-size: clamp(1.2rem,2vw,1.6rem); font-weight: 700; line-height: 1.4; margin-bottom: 20px; }
      .fit-why-cell.problem h3 { color: #6E6E73; }
      .fit-why-cell p { font-size: 0.95rem; line-height: 1.8; }
      .fit-why-cell.problem p { color: #8E8E93; }
      .fit-why-cell.solution p { color: #AEAEB2; }
      .fit-eng { padding: 130px 8%; background: #F5F5F7; }
      .fit-eng-head { margin-bottom: 80px; text-align: center; }
      .fit-eng-eyebrow { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 20px; display: block; }
      .fit-eng-head h2 { font-size: clamp(2rem,4vw,3.2rem); font-weight: 800; letter-spacing: -2px; line-height: 1.1; margin: 0 auto; max-width: 600px; color: #0A0A0A; }
      .fit-eng-grid { display: grid; grid-template-columns: repeat(${numFeatures},1fr); gap: 24px; max-width: 1200px; margin: 0 auto; }
      .fit-eng-item { background: #fff; padding: 50px 40px; transition: transform 0.4s, box-shadow 0.4s; text-align: center; border-radius: 8px; }
      .fit-eng-item:hover { transform: translateY(-8px); box-shadow: 0 30px 60px rgba(0,0,0,0.08); }
      .fit-eng-icon { width: 64px; height: 64px; background: #007AFF; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; margin: 0 auto 28px; color: #fff; }
      .fit-eng-item h3 { font-size: 1.15rem; font-weight: 700; margin-bottom: 14px; color: #0A0A0A; }
      .fit-eng-item p { font-size: 0.88rem; color: #6E6E73; line-height: 1.8; }
      .fit-howto { padding: 130px 8%; background: #fff; }
      .fit-howto-head { text-align: center; max-width: 500px; margin: 0 auto 80px; }
      .fit-howto-head h2 { font-size: clamp(2rem,3.5vw,3rem); font-weight: 800; letter-spacing: -1.5px; color: #0A0A0A; }
      .fit-howto-steps { display: grid; grid-template-columns: repeat(${numSteps},1fr); gap: 60px; max-width: 1000px; margin: 0 auto; }
      .fit-step { text-align: center; }
      .fit-step-img { width: 100%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; margin-bottom: 30px; border: 3px solid #F5F5F7; }
      .fit-step-img img { width: 100%; height: 100%; object-fit: contain; background: #fff; padding: 10px; display: block; }
      .fit-step-num { font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase; color: #007AFF; margin-bottom: 10px; display: block; }
      .fit-step h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 10px; color: #0A0A0A; }
      .fit-step p { font-size: 0.85rem; color: #6E6E73; line-height: 1.7; }
      .fit-social { padding: 100px 8%; background: #F5F5F7; }
      .fit-social-head { text-align: center; margin-bottom: 70px; }
      .fit-social-head h2 { font-size: clamp(1.8rem,3vw,2.5rem); font-weight: 800; letter-spacing: -1px; color: #0A0A0A; }
      .fit-social-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; max-width: 1200px; margin: 0 auto; }
      .fit-review { background: #fff; padding: 45px 40px; transition: transform 0.3s; border-radius: 8px; }
      .fit-review:hover { transform: translateY(-5px); }
      .fit-stars { color: #007AFF; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 20px; display: block; }
      .fit-review blockquote { font-size: 1.02rem; font-weight: 500; line-height: 1.6; margin-bottom: 24px; color: #0A0A0A; }
      .fit-reviewer { font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; color: #6E6E73; display: flex; align-items: center; gap: 12px; }
      .fit-avatar { display: inline-block; width: 32px; height: 32px; background: #E8E8E8; border-radius: 50%; flex-shrink: 0; }
      .fit-rname { font-weight: 600; font-size: 0.82rem; color: #0A0A0A; }
      .fit-rtitle { color: #6E6E73; font-size: 0.75rem; }
      .fit-final { padding: 160px 8%; background: #fff; text-align: center; }
      .fit-final h2 { font-size: clamp(2.5rem,6vw,5rem); font-weight: 900; letter-spacing: -3px; line-height: 1.0; margin-bottom: 30px; color: #0A0A0A; }
      .fit-final h2 .blue { color: #007AFF; }
      .fit-final-sub { font-size: 1.1rem; color: #6E6E73; margin-bottom: 40px; font-weight: 300; }
      .fit-final-price { font-size: 2.5rem; font-weight: 700; letter-spacing: -1px; margin-bottom: 50px; color: #0A0A0A; }
      .fit-btn-primary { padding: 20px 55px; background: #007AFF; color: #fff; font-size: 0.9rem; font-weight: 600; border: none; cursor: pointer; border-radius: 50px; transition: all 0.35s; font-family: 'Inter', sans-serif; }
      .fit-btn-primary:hover { background: #0063CC; transform: translateY(-3px); box-shadow: 0 20px 40px rgba(0,122,255,0.3); }
    </style>

    <div class="fit-page">
      <!-- 1. HERO -->
      <div class="fit-hero">
        <div class="fit-hero-bg"><img src="${image}" alt="${name}" onerror="this.src='./assets/images/placeholder.jpg'"></div>
        <div class="fit-hero-content">
          <span class="fit-hero-label">High-Performance Series</span>
          <h1><span>${name}</span></h1>
          <p class="fit-hero-tagline">${tagline}</p>
          <div class="fit-hero-price">&#8377;${price.toLocaleString('en-IN')}</div>
          <button class="fit-hero-cta buy-btn" data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
            Add to Loadout <span>&#8594;</span>
          </button>
        </div>
      </div>

      <!-- 2. BENEFITS STRIP -->
      <div class="fit-strip reveal-box">${stripHTML}</div>

      <!-- 3. PROBLEM & SOLUTION -->
      <div class="fit-why">
        <div class="fit-why-head reveal-box">
          <span class="fit-why-eyebrow">The Truth</span>
          <h2>${hook.headline}</h2>
        </div>
        <div class="fit-why-grid reveal-box">
          <div class="fit-why-cell problem">
            <span class="tag">The Barrier</span>
            <h3>Where You Stall</h3>
            <p>${hook.problem}</p>
          </div>
          <div class="fit-why-cell solution">
            <span class="tag">The Breakthrough</span>
            <h3>Where You Ascend</h3>
            <p>${hook.solution}</p>
          </div>
        </div>
      </div>

      <!-- 4. FEATURES -->
      <div class="fit-eng">
        <div class="fit-eng-head reveal-box">
          <span class="fit-eng-eyebrow">Architecture</span>
          <h2>Built Different. Performs Different.</h2>
        </div>
        <div class="fit-eng-grid reveal-box">${engHTML}</div>
      </div>

      <!-- 5. HOW TO USE -->
      <div class="fit-howto">
        <div class="fit-howto-head reveal-box"><h2>Application Protocol</h2></div>
        <div class="fit-howto-steps reveal-box">${stepsHTML}</div>
      </div>

      <!-- 6. SOCIAL PROOF -->
      <div class="fit-social">
        <div class="fit-social-head reveal-box"><h2>Trusted by the Elite</h2></div>
        <div class="fit-social-grid reveal-box">${reviewsHTML}</div>
      </div>

      <!-- 7. FINAL CTA -->
      <div class="fit-final reveal-box">
        <h2>Unleash Your <br><span class="blue">Potential.</span></h2>
        <p class="fit-final-sub">${urgency}</p>
        <div class="fit-final-price">&#8377;${price.toLocaleString('en-IN')}</div>
        <button class="fit-btn-primary buy-btn" data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">Equip Now</button>
      </div>
    </div>
  `;

  setupProductButtons(product, name, price, image);
}
'''

# Splice the new block in using index positions
before = content[:start_idx]
after = content[end_idx:]
new_content = before + new_block + after

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully patched renderFitProduct!")
