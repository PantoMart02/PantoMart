import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for i, p in enumerate(products):
    cat = p.get('category', '').lower()
    if cat in ['space', 'pet']:
        reviews = p.get('reviews', [])
        print(f"Product {i}: {p.get('name')} ({cat}) - Reviews Count: {len(reviews)}")
