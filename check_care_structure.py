import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    cat = p.get('category', '').lower()
    if cat == 'care':
        print(f"Care Product: {p.get('name')}")
        if 'howToUse' in p and len(p['howToUse']) > 0:
            print(f"  First howToUse: {p['howToUse'][0]}")
        break
