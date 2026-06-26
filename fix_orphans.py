import re, subprocess

with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of the orphan pattern:
# A setupProductButtons call + closing brace that appears OUTSIDE any function
# (i.e. it's a duplicate - the real one is already inside the function above it)
# Pattern: \n\n  setupProductButtons(product, name, price, image);\n}\n
# followed immediately by a comment or function declaration (not more code)

orphan_pattern = re.compile(
    r'\n\n  setupProductButtons\(product, name, price, image\);\n\}\n(?=// )',
    re.MULTILINE
)

matches = orphan_pattern.findall(content)
print(f'Found {len(matches)} orphan block(s)')

# Remove the orphan blocks (keep just the newline separator)
cleaned, count = orphan_pattern.subn('\n', content)
print(f'Removed {count} orphan block(s)')

with open(r'assets\js\product.js', 'w', encoding='utf-8') as f:
    f.write(cleaned)

result = subprocess.run(['node', '--check', r'assets\js\product.js'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax check: PASSED')
    # final function count
    fns = ['renderCareProduct','renderStyleProduct','renderFitProduct','renderSpaceProduct',
           'renderPetProduct','renderDefaultProduct','setupProductButtons','initProduct',
           'initParallax','initFixedBackground']
    for fn in fns:
        c = len(re.findall(r'function ' + fn, cleaned))
        print(f'  {fn}: {c}')
else:
    print('Syntax check: FAILED')
    print(result.stderr[:600])
