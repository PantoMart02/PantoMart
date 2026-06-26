import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for i, p in enumerate(products):
    if p.get('category', '').lower() == 'space':
        print(f"Index {i}: {p.get('name')} - Keys: {list(p.keys())}")
        if 'hook' in p:
            print(f"  Hook keys: {list(p['hook'].keys())}")
        if 'howToUse' in p and len(p['howToUse']) > 0:
            print(f"  First HowToUse keys: {list(p['howToUse'][0].keys())}")
        if 'reviews' in p and len(p['reviews']) > 0:
            print(f"  First Review keys: {list(p['reviews'][0].keys())}")
