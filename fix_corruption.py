import re, subprocess

with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Fix the orphan setupProductButtons/} at lines 243-244 ─────────────────
# This is a floating `  setupProductButtons(...)\n}` block outside any function
# It appears right after the renderCareProduct closing }
content = content.replace(
    '  setupProductButtons(product, name, price, image);\n}\n// ======================\n// 👔 FASHION (STYLE) RENDERER',
    '// ======================\n// 👔 FASHION (STYLE) RENDERER',
    1
)

# ── 2. Fix the broken renderFitProduct declaration (comment merged with function)
content = content.replace(
    '// ========function renderFitProduct(product, container) {',
    'function renderFitProduct(product, container) {',
    1
)

print('Fixes applied. Running syntax check...')

with open(r'assets\js\product.js', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(['node', '--check', r'assets\js\product.js'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax check: PASSED')
else:
    print('Syntax check: FAILED')
    print(result.stderr[:600])
