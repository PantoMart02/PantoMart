import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for i, p in enumerate(products):
    if p.get('category', '').lower() == 'style':
        reviews = p.get('reviews', [])
        print(f"Product {i}: {p.get('name')} - Reviews Count: {len(reviews)}")
        if reviews:
            print(f"  First review keys: {list(reviews[0].keys())}")
