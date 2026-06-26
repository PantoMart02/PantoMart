import json, os

# Map of category -> actual files on disk
image_dir = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/images/products'

# Build a map of actual files per category
actual_files = {}
for cat in ['care', 'style', 'fit', 'space', 'pet']:
    cat_dir = os.path.join(image_dir, cat)
    if os.path.isdir(cat_dir):
        files = sorted([
            f for f in os.listdir(cat_dir)
            if f[0].isdigit()  # Only numbered files (1.webp, 2.jpg etc)
        ], key=lambda x: int(x.split('.')[0]))
        actual_files[cat] = files
        print(f"[{cat}] actual files: {files}")

print()

# Fix mainImage paths in products.json to match actual extensions
with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

fixed = 0
for p in products:
    cat = p.get('category', '')
    mainImage = p.get('mainImage', '')
    if not mainImage or cat not in actual_files:
        continue

    # Extract the number from the path (e.g. "1" from "/assets/.../1.jpg")
    basename = os.path.basename(mainImage)  # "1.jpg"
    num_str = basename.split('.')[0]        # "1"

    # Find the actual file with that number in the real directory
    matches = [f for f in actual_files[cat] if f.split('.')[0] == num_str]
    if matches:
        actual_ext = matches[0].split('.')[-1]
        new_path = f"/assets/images/products/{cat}/{num_str}.{actual_ext}"
        if mainImage != new_path:
            print(f"FIXED [{cat}] {num_str}: {mainImage} -> {new_path}")
            p['mainImage'] = new_path
            fixed += 1
    else:
        print(f"WARNING [{cat}] no file found for '{basename}' - available: {actual_files[cat]}")

print(f"\nFixed {fixed} image paths.")

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Saved products.json")
