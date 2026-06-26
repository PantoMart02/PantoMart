import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove inline styles
content = re.sub(r'<style>([\s\S]*?)</style>', '', content)

# Update Search Dropdown UI (Phase 2)
content = content.replace('id="search-dropdown" class="search-dropdown"', 'id="search-dropdown" class="absolute top-full mt-2 left-0 right-0 bg-surface border border-outline-variant/30 z-50 max-h-[400px] overflow-y-auto shadow-xl hidden rounded-xl"')

# Remove bg-black/10 from hero and ensure no blur on images
content = content.replace('bg-black/10', 'bg-gradient-to-t from-black/40 via-black/10 to-transparent')
content = content.replace('bg-surface/30 backdrop-blur-sm', 'bg-surface/90 shadow-2xl') # No blur on hero card

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('category.html', 'r', encoding='utf-8') as f:
    cat_content = f.read()

# Remove inline styles
cat_content = re.sub(r'<style>([\s\S]*?)</style>', '', cat_content)
with open('category.html', 'w', encoding='utf-8') as f:
    f.write(cat_content)

with open('product.html', 'r', encoding='utf-8') as f:
    prod_content = f.read()
prod_content = re.sub(r'<style>([\s\S]*?)</style>', '', prod_content)
with open('product.html', 'w', encoding='utf-8') as f:
    f.write(prod_content)

print("HTML cleanup complete.")
