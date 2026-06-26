import re, subprocess

with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

OLD_FN = '''function initFixedBackground(image) {
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

    // -- Fitness gaps --
    '.fit-strip, .fit-motion, .fit-why, .fit-eng, .fit-outcome, .fit-howto, .fit-social, .fit-final {',
    '  margin-top: 6px;',
    '}',

    // -- Fashion gaps --
    '.fit-page > section, .fit-page > div { margin-top: 6px; }',

    // Care / Default / Pet generic section gaps
    '#product-container > div > div[style] + div[style] { margin-top: 6px; }',
  ].join('\\n');
  document.head.appendChild(st);
}'''

NEW_FN = """function initFixedBackground(image) {
  // Remove previous instance
  var old = document.getElementById('product-fixed-bg');
  if (old) old.remove();
  var oldOverlay = document.getElementById('product-fixed-bg-overlay');
  if (oldOverlay) oldOverlay.remove();
  var oldStyle = document.getElementById('product-fixed-bg-style');
  if (oldStyle) oldStyle.remove();

  // Fixed background: raw product image (slightly zoomed, dark overlay separately)
  var bg = document.createElement('div');
  bg.id = 'product-fixed-bg';
  bg.style.cssText = [
    'position:fixed',
    'top:0', 'left:0',
    'width:100%', 'height:100%',
    'z-index:-2',
    'background-image:url(' + JSON.stringify(image) + ')',
    'background-size:cover',
    'background-position:center 30%',
    'pointer-events:none',
    'transform:scale(1.08)',
    'transition:opacity 1s ease',
  ].join(';');
  document.body.appendChild(bg);

  // Dark cinematic overlay + blur on top of bg image
  var ov = document.createElement('div');
  ov.id = 'product-fixed-bg-overlay';
  ov.style.cssText = [
    'position:fixed',
    'top:0', 'left:0',
    'width:100%', 'height:100%',
    'z-index:-1',
    'background:rgba(6,4,3,0.68)',
    'backdrop-filter:blur(4px)',
    '-webkit-backdrop-filter:blur(4px)',
    'pointer-events:none',
  ].join(';');
  document.body.appendChild(ov);

  // Body dark so gaps between sections look cinematic (dark product bg visible)
  document.body.style.background = '#080604';

  // Inject global gap + z-index CSS for all category pages
  var st = document.createElement('style');
  st.id = 'product-fixed-bg-style';
  var css = [
    'body { background:#080604 !important; }',
    '#product-container { position:relative; z-index:1; }',

    // FITNESS gaps - each section floats over the bg
    '.fit-strip,.fit-motion,.fit-why,.fit-eng,.fit-outcome,.fit-howto,.fit-social,.fit-final { margin-top:8px; }',

    // HOME DECOR gaps already handled by .sp-box margin:24px auto
    // Add extra bottom margin so the final CTA has space below it too
    '.sp { padding-bottom:40px !important; }',

    // SKINCARE / CARE
    '#product-container > div > section + section { margin-top:8px; }',
    '#product-container > div > div + section    { margin-top:8px; }',

    // DEFAULT / PET generic block gaps
    '#product-container > div > div + div { margin-top:8px; }',

    // Ensure fashion hero and sections have gap between them
    '.fashion-page > section + section,',
    '.fashion-page > div + div { margin-top:8px; }',
  ].join('\\n');
  st.textContent = css;
  document.head.appendChild(st);
}"""

if OLD_FN in content:
    content = content.replace(OLD_FN, NEW_FN, 1)
    print('initFixedBackground replaced OK')
else:
    # Regex fallback
    pat = re.compile(r'function initFixedBackground\(image\)\s*\{.*?\n\}', re.DOTALL)
    content, n = pat.subn(NEW_FN, content, count=1)
    print(f'Regex fallback: {n} replacements')

with open(r'assets\js\product.js', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(['node', '--check', r'assets\js\product.js'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax check: PASSED')
else:
    print('FAILED:', result.stderr[:500])
