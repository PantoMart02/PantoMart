import re, subprocess

with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. PATCH setupProductButtons to call initFixedBackground ─────────────────
OLD_SETUP = '''function setupProductButtons(product, name, price, image) {
  var buyNowBtn = document.getElementById("buy-now");
  if (buyNowBtn) {
    buyNowBtn.addEventListener("click", function () {
      alert("🚀 Redirecting to checkout...");
    });
  }
  // Kick off parallax after the renderer has painted
  requestAnimationFrame(function() {
    initParallax();
  });
}'''

NEW_SETUP = '''function setupProductButtons(product, name, price, image) {
  var buyNowBtn = document.getElementById("buy-now");
  if (buyNowBtn) {
    buyNowBtn.addEventListener("click", function () {
      alert("🚀 Redirecting to checkout...");
    });
  }
  // Kick off effects after the renderer has painted
  requestAnimationFrame(function() {
    initFixedBackground(image);
    initParallax();
  });
}

// ======================
// 🖼️  FIXED BACKGROUND ENGINE — universal across all product pages
// ======================
function initFixedBackground(image) {
  // Remove previous instance
  var old = document.getElementById('product-fixed-bg');
  if (old) old.remove();
  var oldStyle = document.getElementById('product-fixed-bg-style');
  if (oldStyle) oldStyle.remove();

  // Create fixed background layer
  var bg = document.createElement('div');
  bg.id = 'product-fixed-bg';
  bg.style.cssText = [
    'position:fixed',
    'top:0','left:0',
    'width:100%','height:100%',
    'z-index:-1',
    'background-image:url(' + JSON.stringify(image) + ')',
    'background-size:cover',
    'background-position:center',
    'filter:brightness(0.22) saturate(0.7) blur(2px)',
    'pointer-events:none',
    'transition:opacity 0.6s ease',
  ].join(';');
  document.body.appendChild(bg);

  // Inject global style: ensure product-container is positioned over fixed bg
  // and every direct section gets a small margin gap to reveal bg between them
  var st = document.createElement('style');
  st.id = 'product-fixed-bg-style';
  st.textContent = [
    // Product container sits on top of the fixed bg
    '#product-container { position:relative; z-index:1; }',

    // ── Fitness gaps ──
    '.fit-strip, .fit-motion, .fit-why, .fit-eng, .fit-outcome, .fit-howto, .fit-social, .fit-final {',
    '  margin-top: 6px;',
    '}',

    // ── Fashion gaps ──
    '.fit-page > section, .fit-page > div { margin-top: 6px; }',

    // Care / Default / Pet generic section gaps
    '#product-container > div > div[style] + div[style] { margin-top: 6px; }',
  ].join('\n');
  document.head.appendChild(st);
}'''

if OLD_SETUP in content:
    content = content.replace(OLD_SETUP, NEW_SETUP, 1)
    print('setupProductButtons patched OK')
else:
    print('WARNING: OLD_SETUP not found exactly — trying regex fallback')
    content = re.sub(
        r'function setupProductButtons\(product, name, price, image\)\s*\{.*?requestAnimationFrame\(function\(\)\s*\{[^}]*initParallax\(\);[^}]*\}\);?\s*\}',
        NEW_SETUP,
        content,
        count=1,
        flags=re.DOTALL
    )
    print('regex fallback applied')

# ── 2. REWRITE renderSpaceProduct ────────────────────────────────────────────
space_start = content.find('function renderSpaceProduct(product, container)')
pet_start   = content.find('function renderPetProduct(product, container)')

NEW_SPACE = r'''function renderSpaceProduct(product, container) {
  const name = product.name || 'Sculptural Accent Piece';
  const price = Number(product.price) || 0;
  const description = product.description || 'Objects that hold the room in quiet reverence.';
  const image = getImageUrl(product.mainImage || product.image);

  container.innerHTML = `
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
      /* ── ROOT ── */
      .sp { font-family:'Inter',sans-serif; color:#2E2A25; padding-bottom:80px; }

      /* ── PREMIUM BOX — shared ── */
      .sp-box {
        margin: 24px auto;
        max-width: 1200px;
        background: rgba(246,241,234,0.97);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(255,255,255,0.45);
        box-shadow: 0 12px 48px rgba(0,0,0,0.18), 0 2px 8px rgba(0,0,0,0.08);
        border-radius: 6px;
        overflow: hidden;
      }
      .sp-box-dark {
        background: rgba(30,26,22,0.95);
        border: 1px solid rgba(255,255,255,0.08);
        color: #F6F1EA;
      }
      .sp-box-alt {
        background: rgba(237,232,223,0.97);
      }

      /* ── HERO — full bleed, no box ── */
      .sp-hero {
        position: relative; width:100%; height:100vh; overflow:hidden;
        margin-bottom: 24px;
      }
      .sp-hero img {
        width:100%; height:100%; object-fit:cover; object-position:center;
        filter:brightness(0.78); transition:transform 8s ease; display:block;
      }
      .sp-hero:hover img { transform:scale(1.04); }
      .sp-hero-text {
        position:absolute; bottom:10%; left:8%; max-width:520px; color:#F6F1EA;
      }
      .sp-hero-text h1 {
        font-family:'Cormorant Garamond',serif;
        font-size:clamp(2.8rem,5.5vw,5rem); font-weight:300; line-height:1.1;
        letter-spacing:0.5px; margin-bottom:14px;
      }
      .sp-hero-text .tag {
        font-size:0.72rem; letter-spacing:3.5px; text-transform:uppercase;
        opacity:0.65; margin-bottom:34px; display:block;
      }
      .sp-ghost-btn {
        display:inline-block; padding:16px 42px;
        background:transparent; color:#F6F1EA;
        border:1px solid rgba(246,241,234,0.45);
        font-size:0.72rem; letter-spacing:3px; text-transform:uppercase;
        cursor:pointer; transition:all 0.4s; font-family:'Inter',sans-serif;
      }
      .sp-ghost-btn:hover { background:rgba(246,241,234,0.12); border-color:#F6F1EA; }

      /* ── STRIP ── */
      .sp-strip-inner {
        display:flex; justify-content:space-around; flex-wrap:wrap;
        padding:50px 60px;
      }
      .sp-si { text-align:center; padding:10px 20px; }
      .sp-si .lbl {
        font-size:0.6rem; letter-spacing:3px; text-transform:uppercase;
        color:#9A8E82; margin-bottom:10px; display:block;
      }
      .sp-si .val {
        font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:400;
      }
      .sp-si + .sp-si { border-left:1px solid rgba(46,42,37,0.12); }

      /* ── ATMOSPHERE ── */
      .sp-atm { display:grid; grid-template-columns:1fr 1fr; }
      .sp-atm-img { overflow:hidden; min-height:400px; }
      .sp-atm-img img {
        width:100%; height:100%; object-fit:cover; display:block;
        transition:transform 6s ease;
      }
      .sp-atm-img:hover img { transform:scale(1.06); }
      .sp-atm-txt {
        display:flex; flex-direction:column; justify-content:center;
        padding:70px 60px;
      }
      .sp-atm-txt.inv { padding:70px 60px; }
      .sp-atm-txt .ey {
        font-size:0.6rem; letter-spacing:3px; text-transform:uppercase;
        color:#9A8E82; margin-bottom:22px; display:block;
      }
      .sp-atm-txt h2 {
        font-family:'Cormorant Garamond',serif;
        font-size:clamp(1.7rem,2.8vw,2.6rem); font-weight:300; line-height:1.3;
        margin-bottom:20px;
      }
      .sp-atm-txt p {
        font-size:0.88rem; line-height:2; color:#7A6F65; max-width:340px;
      }
      .sp-atm-txt.dark h2 { color:#F6F1EA; }
      .sp-atm-txt.dark p  { color:#A89E94; }
      .sp-atm-txt.dark .ey { color:#6A8E6A; }

      /* ── STORY ── */
      .sp-story-inner { padding:90px 80px; max-width:720px; margin:0 auto; text-align:center; }
      .sp-story-inner .ey {
        font-size:0.6rem; letter-spacing:3px; text-transform:uppercase;
        color:#9A8E82; margin-bottom:28px; display:block;
      }
      .sp-story-inner blockquote {
        font-family:'Cormorant Garamond',serif;
        font-size:clamp(1.5rem,2.5vw,2.1rem); font-weight:300; font-style:italic;
        line-height:1.5; margin-bottom:34px;
      }
      .sp-story-inner p {
        font-size:0.9rem; line-height:2.1; color:#7A6F65; font-weight:300;
      }

      /* ── MATERIAL ── */
      .sp-mat-inner { display:grid; grid-template-columns:1fr 1fr; }
      .sp-mat-img { overflow:hidden; aspect-ratio:4/5; }
      .sp-mat-img img { width:100%; height:100%; object-fit:cover; display:block; transition:transform 6s ease; }
      .sp-mat-img:hover img { transform:scale(1.08); }
      .sp-mat-txt {
        display:flex; flex-direction:column; justify-content:center;
        padding:70px 60px;
      }
      .sp-mat-txt .ey {
        font-size:0.6rem; letter-spacing:3px; text-transform:uppercase;
        color:#9A8E82; margin-bottom:26px; display:block;
      }
      .sp-mat-txt h2 {
        font-family:'Cormorant Garamond',serif; font-size:2.3rem;
        font-weight:300; margin-bottom:34px;
      }
      .sp-mat-txt ul { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:16px; }
      .sp-mat-txt ul li {
        font-size:0.86rem; color:#7A6F65; padding-left:18px;
        border-left:1px solid #C5B9AC; line-height:1.7;
      }

      /* ── TRANSFORM (Before/After) ── */
      .sp-tf { display:grid; grid-template-columns:1fr 1fr; }
      .sp-tf-panel { position:relative; overflow:hidden; }
      .sp-tf-panel img {
        width:100%; min-height:480px; object-fit:cover; display:block;
        opacity:0.5; transition:opacity 0.5s, transform 7s ease;
      }
      .sp-tf-panel:hover img { opacity:0.72; transform:scale(1.05); }
      .sp-tf-lbl {
        position:absolute; bottom:36px; left:36px; color:#F6F1EA;
      }
      .sp-tf-lbl .num {
        font-family:'Cormorant Garamond',serif; font-size:4.5rem;
        font-weight:300; opacity:0.18; line-height:1; display:block;
      }
      .sp-tf-lbl p {
        font-size:0.68rem; letter-spacing:3px; text-transform:uppercase; opacity:0.65;
      }

      /* ── PLACEMENT (scroll) ── */
      .sp-pl-inner { padding:60px 50px; }
      .sp-pl-inner h2 {
        font-family:'Cormorant Garamond',serif; font-size:2rem;
        font-weight:300; margin-bottom:50px;
      }
      .sp-pl-scroll {
        display:flex; gap:24px; overflow-x:auto; padding-bottom:16px;
        scroll-snap-type:x mandatory; scrollbar-width:none;
      }
      .sp-pl-scroll::-webkit-scrollbar { display:none; }
      .sp-pl-item { flex:0 0 300px; scroll-snap-align:start; }
      .sp-pl-photo { overflow:hidden; aspect-ratio:3/4; margin-bottom:16px; border-radius:4px; }
      .sp-pl-photo img { width:100%; height:100%; object-fit:cover; display:block; transition:transform 5s ease; }
      .sp-pl-item:hover .sp-pl-photo img { transform:scale(1.07); }
      .sp-pl-lbl { font-size:0.6rem; letter-spacing:3px; text-transform:uppercase; color:#9A8E82; margin-bottom:5px; }
      .sp-pl-name { font-family:'Cormorant Garamond',serif; font-size:1.2rem; font-weight:300; }

      /* ── SOCIAL ── */
      .sp-soc-inner { padding:70px 70px; }
      .sp-soc-inner .ey {
        font-size:0.6rem; letter-spacing:3px; text-transform:uppercase;
        color:#9A8E82; margin-bottom:55px; display:block; text-align:center;
      }
      .sp-soc-row {
        padding:34px 0; border-top:1px solid rgba(46,42,37,0.1);
        display:grid; grid-template-columns:130px 1fr; gap:36px; align-items:start;
      }
      .sp-soc-by {
        font-size:0.68rem; letter-spacing:2px; text-transform:uppercase;
        color:#9A8E82; padding-top:5px;
      }
      .sp-soc-q {
        font-family:'Cormorant Garamond',serif; font-size:1.35rem;
        font-weight:300; font-style:italic; line-height:1.5;
      }

      /* ── FINAL CTA ── */
      .sp-final-inner { padding:110px 60px; text-align:center; }
      .sp-final-inner .ey {
        font-size:0.6rem; letter-spacing:4px; text-transform:uppercase;
        opacity:0.45; margin-bottom:28px; display:block; color:#F6F1EA;
      }
      .sp-final-inner h2 {
        font-family:'Cormorant Garamond',serif;
        font-size:clamp(2rem,4vw,3.8rem); font-weight:300; font-style:italic;
        line-height:1.2; margin-bottom:16px; color:#F6F1EA;
      }
      .sp-final-inner .pr {
        font-family:'Cormorant Garamond',serif; font-size:1.5rem;
        font-weight:300; opacity:0.5; margin-bottom:50px; color:#F6F1EA;
      }
      .sp-final-btn {
        display:inline-block; padding:20px 60px;
        border:1px solid rgba(246,241,234,0.35); color:#F6F1EA;
        font-size:0.72rem; letter-spacing:3px; text-transform:uppercase;
        cursor:pointer; transition:all 0.4s; font-family:'Inter',sans-serif;
        background:transparent;
      }
      .sp-final-btn:hover { background:rgba(246,241,234,0.09); border-color:rgba(246,241,234,0.75); }
    </style>

    <div class="sp">

      <!-- ① HERO — full bleed -->
      <div class="sp-hero">
        <img src="${image}" alt="${name}" onerror="this.src='./assets/images/placeholder.jpg'">
        <div class="sp-hero-text">
          <h1>${name}</h1>
          <span class="tag">Presence through restraint.</span>
          <button class="sp-ghost-btn buy-btn"
            data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
            Bring This Into Your Space
          </button>
        </div>
      </div>

      <!-- ② SILENT DETAILS STRIP -->
      <div class="sp-box">
        <div class="sp-strip-inner">
          <div class="sp-si"><span class="lbl">Material</span><span class="val">Hand-finished Ceramic</span></div>
          <div class="sp-si"><span class="lbl">Dimensions</span><span class="val">32 × 18 × 12 cm</span></div>
          <div class="sp-si"><span class="lbl">Finish</span><span class="val">Soft Matte · Ivory</span></div>
          <div class="sp-si"><span class="lbl">Origin</span><span class="val">Studio Craft, India</span></div>
          <div class="sp-si"><span class="lbl">Price</span><span class="val" style="font-size:1.3rem;">&#8377;${price.toLocaleString('en-IN')}</span></div>
        </div>
      </div>

      <!-- ③ ATMOSPHERE — left image / right text -->
      <div class="sp-box">
        <div class="sp-atm">
          <div class="sp-atm-img">
            <img src="${image}" alt="calm interior" onerror="this.src='./assets/images/placeholder.jpg'">
          </div>
          <div class="sp-atm-txt">
            <span class="ey">The feeling</span>
            <h2>Creates a sense of calm you didn't know you were missing.</h2>
            <p>The right object doesn't demand attention. It earns it — slowly, quietly, permanently.</p>
          </div>
        </div>
      </div>

      <!-- ④ ATMOSPHERE — right image / left text (dark variant) -->
      <div class="sp-box sp-box-dark">
        <div class="sp-atm" style="grid-template-columns:1fr 1fr;">
          <div class="sp-atm-txt dark">
            <span class="ey">The intention</span>
            <h2>Designed for quiet luxury.</h2>
            <p>Form arrived at after years of iteration. Function kept entirely out of sight. The result is an object that simply belongs.</p>
          </div>
          <div class="sp-atm-img">
            <img src="${image}" style="filter:sepia(0.08) brightness(0.82);" alt="warm light" onerror="this.src='./assets/images/placeholder.jpg'">
          </div>
        </div>
      </div>

      <!-- ⑤ DESIGN STORY -->
      <div class="sp-box">
        <div class="sp-story-inner">
          <span class="ey">The story</span>
          <blockquote>"An object is complete when nothing can be removed from it."</blockquote>
          <p>This piece was drawn from a study of traditional craft — the weight of well-made things, the way they hold light differently at morning and dusk. No shortcuts in its making. No trend in its form. Only the intention that it would outlast every room it inhabits.</p>
        </div>
      </div>

      <!-- ⑥ MATERIAL FOCUS -->
      <div class="sp-box sp-box-alt">
        <div class="sp-mat-inner">
          <div class="sp-mat-img">
            <img src="${image}" style="filter:contrast(1.06) brightness(0.93);" alt="texture" onerror="this.src='./assets/images/placeholder.jpg'">
          </div>
          <div class="sp-mat-txt">
            <span class="ey">Material &amp; Craft</span>
            <h2>Every surface tells you something.</h2>
            <ul>
              <li>Hand-finished ceramic — no two pieces identical</li>
              <li>Soft matte glaze — resists fingerprints, ages beautifully</li>
              <li>Dense, considered weight — sits without shifting</li>
              <li>Lead-free clay, kiln-fired at 1240 °C</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- ⑦ SPACE IMPACT (Before → After) -->
      <div class="sp-box sp-box-dark">
        <div class="sp-tf">
          <div class="sp-tf-panel">
            <img src="${image}" style="filter:grayscale(0.75) brightness(0.4);" alt="before" onerror="this.src='./assets/images/placeholder.jpg'">
            <div class="sp-tf-lbl"><span class="num">01</span><p>The space before</p></div>
          </div>
          <div class="sp-tf-panel">
            <img src="${image}" style="filter:sepia(0.08) brightness(0.65);" alt="after" onerror="this.src='./assets/images/placeholder.jpg'">
            <div class="sp-tf-lbl"><span class="num">02</span><p>The space after</p></div>
          </div>
        </div>
      </div>

      <!-- ⑧ PLACEMENT FLOW -->
      <div class="sp-box">
        <div class="sp-pl-inner">
          <h2>Where it lives</h2>
          <div class="sp-pl-scroll">
            ${[
              {lbl:'Setting 01',name:'The Living Room',filter:''},
              {lbl:'Setting 02',name:'The Bedroom',filter:'filter:sepia(0.1);'},
              {lbl:'Setting 03',name:'The Workspace',filter:'filter:brightness(0.88) contrast(1.05);'},
              {lbl:'Setting 04',name:'The Entryway',filter:'filter:saturate(0.8);'},
            ].map(function(pl){ return '<div class="sp-pl-item"><div class="sp-pl-photo"><img src="' + image + '" style="' + pl.filter + '" onerror="this.src=\'./assets/images/placeholder.jpg\'"></div><div class="sp-pl-lbl">' + pl.lbl + '</div><div class="sp-pl-name">' + pl.name + '</div></div>'; }).join('')}
          </div>
        </div>
      </div>

      <!-- ⑨ SOFT SOCIAL PROOF -->
      <div class="sp-box">
        <div class="sp-soc-inner">
          <span class="ey">Lived with</span>
          ${[
            {by:'Priya S., Pune',q:'"It changed the feel of my room. Not dramatically — quietly. The way good things do."'},
            {by:'Rohan K., Mumbai',q:'"Every guest asks about it. I just smile."'},
            {by:'Ananya M., Bangalore',q:'"I bought it for my desk. I now have three more in different rooms."'},
          ].map(function(r){ return '<div class="sp-soc-row"><div class="sp-soc-by">' + r.by + '</div><blockquote class="sp-soc-q">' + r.q + '</blockquote></div>'; }).join('')}
        </div>
      </div>

      <!-- ⑩ FINAL CTA -->
      <div class="sp-box sp-box-dark">
        <div class="sp-final-inner">
          <span class="ey">Available now</span>
          <h2>Complete your space<br>with intention.</h2>
          <div class="pr">&#8377;${price.toLocaleString('en-IN')}</div>
          <button class="sp-final-btn buy-btn"
            data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
            Add to Space
          </button>
        </div>
      </div>

    </div>
  `;

  setupProductButtons(product, name, price, image);
}

'''

content = content[:space_start] + NEW_SPACE + content[pet_start:]
print('renderSpaceProduct rewritten OK')

# ── 3. WRITE & VERIFY ─────────────────────────────────────────────────────────
with open(r'assets\js\product.js', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(['node', '--check', r'assets\js\product.js'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax check: PASSED')
else:
    print('Syntax check: FAILED')
    print(result.stderr[:600])
