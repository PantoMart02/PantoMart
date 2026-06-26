import re, subprocess

# Read the new function from the clean JS file
with open(r'fixed_bg_fn.js', 'r', encoding='utf-8') as f:
    raw = f.read()
# Strip the comment line at the top
new_fn = '\n'.join(line for line in raw.split('\n') if not line.startswith('//')).strip()

# Read product.js
with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the initFixedBackground function
pat = re.compile(r'function initFixedBackground\(image\)\s*\{.*?\n\}', re.DOTALL)
matches = pat.findall(content)
print(f'Found {len(matches)} match(es)')
if matches:
    print('First 80 chars:', matches[0][:80].encode('ascii','replace').decode())

content, n = pat.subn(new_fn, content, count=1)
print(f'Replacements: {n}')

with open(r'assets\js\product.js', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(['node', '--check', r'assets\js\product.js'], capture_output=True, text=True)
if result.returncode == 0:
    print('Syntax check: PASSED')
else:
    print('Syntax check: FAILED')
    print(result.stderr[:400])
