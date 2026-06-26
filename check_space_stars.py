import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    cat = p.get('category', '').lower()
    if cat == 'space':
        print(f"Space Product: {p.get('name')}")
        if 'reviews' in p:
            for i, r in enumerate(p['reviews']):
                if 'stars' not in r:
                    print(f"  Review {i} is MISSING 'stars'! Keys: {list(r.keys())}")
                else:
                    print(f"  Review {i} has 'stars': {r['stars']}")
