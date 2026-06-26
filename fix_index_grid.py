import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The issue: the old orphaned Skincare card block appears after the </section> closing tag
# We need to find it and remove it. It starts with whitespace + <a href="category.html?cat=care"
# and ends before <!-- The Edit

# Find the position of the second section close (after the grid)
# Strategy: find the duplicated block between </section> and <!-- The Edit
pattern = re.compile(
    r'(</section>\r?\n\r?\n)\s+<a href="category\.html\?cat=care" class="md:col-span-4.*?</div>\r?\n\s+</a>\r?\n\s+<div class="absolute bottom-10.*?</div>\r?\n\s+</a>\r?\n\r?\n\s+(<!-- The Edit)',
    re.DOTALL
)

new_content = re.sub(
    r'(</section>\r?\n\r?\n)(\s+<a href="category\.html\?cat=care".*?</a>\r?\n\s+</div>\r?\n\s+</a>\r?\n\r?\n\s+)(<!-- The Edit)',
    r'\1    \3',
    content,
    flags=re.DOTALL
)

if new_content == content:
    print("Pattern not matched - checking structure")
    # Find the orphan block manually
    idx1 = content.find('</section>\n\n        <a href="category.html?cat=care"')
    if idx1 == -1:
        idx1 = content.find('</section>\r\n\r\n        <a href="category.html?cat=care"')
    print(f"Orphan found at index: {idx1}")
    if idx1 != -1:
        # Find where The Edit section starts
        idx2 = content.find('<!-- The Edit', idx1)
        print(f"The Edit found at index: {idx2}")
        new_content = content[:idx1 + len('</section>\n\n')] + '    ' + content[idx2:]
else:
    print("Pattern matched and fixed")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
