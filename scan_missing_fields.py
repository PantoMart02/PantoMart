import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

required_base = ['name', 'price', 'category', 'mainImage', 'tagline', 'hook']

for i, p in enumerate(products):
    cat = p.get('category', '').lower()
    missing = [f for f in required_base if f not in p]
    
    if cat == 'care':
        if 'ingredients' not in p: missing.append('ingredients')
    elif cat == 'style':
        if 'materialText' not in p: missing.append('materialText')
    elif cat == 'fit':
        if 'features' not in p: missing.append('features')
    elif cat == 'space':
        if 'ingredients' not in p: missing.append('ingredients')
    elif cat == 'pet':
        if 'ingredients' not in p: missing.append('ingredients')

    if 'howToUse' not in p: missing.append('howToUse')
    if 'reviews' not in p: missing.append('reviews')

    if missing:
        print(f"Product {i} ({p.get('name')}): Missing {missing}")

print("\nScan complete.")
