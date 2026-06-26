import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    cat = p.get('category', '').lower()
    if cat == 'fit':
        print(f"Fit Product: {p.get('name')}")
        if 'reviews' in p:
            for i, r in enumerate(p['reviews']):
                print(f"  Review {i} keys: {list(r.keys())}")
