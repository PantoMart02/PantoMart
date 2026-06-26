import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("=== mainImage values in products.json ===")
for p in products:
    cat = p.get('category', 'MISSING')
    name = p.get('name', 'MISSING')[:40]
    img = p.get('mainImage', 'MISSING')
    print(f"[{cat}] {name:40s} => {img}")
