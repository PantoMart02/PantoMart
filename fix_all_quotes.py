file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# All the patterns that need fixing - unescaped single quotes inside HTML attributes
# within JS single-quoted strings

fixes = [
    # Line 362 - Style renderer benefits box-shadow
    (
        """onmouseover=\"this.style.boxShadow='0 20px 40px rgba(0,0,0,0.06)'\" onmouseout=\"this.style.boxShadow='none'\"""",
        """onmouseover=\"this.style.boxShadow=\\'0 20px 40px rgba(0,0,0,0.06)\\'\" onmouseout=\"this.style.boxShadow=\\'none\\'\""""
    ),
    # Line 403 - Style renderer reviews translateY
    (
        """onmouseover=\"this.style.transform='translateY(-6px)'\" onmouseout=\"this.style.transform='translateY(0)'\"""",
        """onmouseover=\"this.style.transform=\\'translateY(-6px)\\'\" onmouseout=\"this.style.transform=\\'translateY(0)\\'\""""
    ),
    # Line 691 - Space renderer benefits box-shadow (inside template literal, OK as-is)
    # Line 717 - Space renderer reviews translateY (inside template literal, OK as-is)
    # Line 738 - Space hero image scale (inside template literal attributes, OK as-is)
    # Line 919 - Pet hero image scale (inside inline HTML style, OK as-is)
]

count = 0
for bad, good in fixes:
    if bad in content:
        content = content.replace(bad, good, 1)
        count += 1
        print(f"Fixed: {bad[:60]}...")
    else:
        print(f"NOT FOUND: {bad[:60]}...")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone. Fixed {count} issues.")
print("\nVerifying remaining issues...")

# Re-check
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

remaining = []
for i, line in enumerate(lines, 1):
    if ('onmouseover=' in line or 'onmouseout=' in line):
        if "transform='" in line or "boxShadow='" in line:
            # Only flag if it's inside a single-quoted JS string (not template literal)
            # Template literals use backticks - check if line starts with backtick context
            stripped = line.strip()
            if stripped.startswith("'") or "' +" in line:
                remaining.append((i, line.rstrip()[:130]))

if remaining:
    print(f"Still {len(remaining)} issues in single-quoted strings:")
    for ln, txt in remaining:
        print(f"  Line {ln}: {txt}")
else:
    print("All clear in single-quoted string contexts!")
