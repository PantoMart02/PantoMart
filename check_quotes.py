import re

with open('c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

errors = []
for i, line in enumerate(lines, 1):
    if 'onmouseover=' in line or 'onmouseout=' in line:
        # Look for style.transform=' or style.boxShadow=' with unescaped single quote
        if "transform='" in line or "boxShadow='" in line:
            errors.append((i, line.rstrip()))

if errors:
    print(f'Found {len(errors)} potential issues:')
    for lineno, txt in errors:
        print(f'  Line {lineno}: {txt[:140]}')
else:
    print('No unescaped single-quote issues found.')
