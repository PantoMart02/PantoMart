import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# The new products have a 'tagline' or 'hook', whereas dummy products don't.
# We will filter the list to keep ONLY the products that we have updated.
cleaned_products = [p for p in products if 'hook' in p]

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_products, f, indent=2, ensure_ascii=False)

print(f"Removed {len(products) - len(cleaned_products)} previous products. Kept {len(cleaned_products)} new products.")
