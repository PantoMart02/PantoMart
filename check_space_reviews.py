import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    cat = p.get('category', '').lower()
    if cat == 'space':
        print(f"Space Product: {p.get('name')}")
        if 'reviews' in p and len(p['reviews']) > 0:
            print(f"  First review: {p['reviews'][0]}")
        break
