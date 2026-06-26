import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for i, p in enumerate(products):
    if p.get('category', '').lower() == 'space':
        print(f"Index {i}: {p.get('name')}")
        if 'ingredients' in p and len(p['ingredients']) > 0:
            print(f"  First Ingredients keys: {list(p['ingredients'][0].keys())}")
        if 'benefits' in p and len(p['benefits']) > 0:
            print(f"  First Benefits keys: {list(p['benefits'][0].keys())}")
