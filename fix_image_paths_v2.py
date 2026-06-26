import json
import os

image_root = 'c:/Users/yarra/OneDrive/Desktop/PantoMart'
backend_dir = 'c:/Users/yarra/OneDrive/Desktop/backend'
json_path = os.path.join(backend_dir, 'products.json')

with open(json_path, 'r', encoding='utf-8') as f:
    products = json.load(f)

extensions = ['.webp', '.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.WEBP']

fixed_count = 0
not_found_count = 0

for p in products:
    original_path = p.get('mainImage', '')
    if not original_path:
        continue
    
    # Remove leading slash for local path joining
    rel_path = original_path.lstrip('/')
    abs_path = os.path.join(image_root, rel_path)
    
    # Check if original exists
    if os.path.exists(abs_path):
        continue
    
    # If not, try other extensions
    base_path_no_ext = os.path.splitext(abs_path)[0]
    found = False
    for ext in extensions:
        test_path = base_path_no_ext + ext
        if os.path.exists(test_path):
            # Found it! Update the JSON path
            new_rel_path = os.path.relpath(test_path, image_root).replace('\\', '/')
            p['mainImage'] = '/' + new_rel_path
            print(f"Fixed: {original_path} -> {p['mainImage']}")
            fixed_count += 1
            found = True
            break
    
    if not found:
        print(f"Warning: Image not found for {p['name']} (tried {original_path} with various extensions)")
        not_found_count += 1

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f"\nFinished. Fixed {fixed_count} paths. {not_found_count} still missing.")
