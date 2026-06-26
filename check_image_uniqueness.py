import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print("Product Name".ljust(50), "| Image Path")
print("-" * 80)
for p in products:
    name = p.get("name", "N/A")
    img = p.get("mainImage", "N/A")
    print(f"{name.ljust(50)} | {img}")

# Check for duplicates
images = [p.get("mainImage") for p in products if p.get("mainImage")]
if len(images) != len(set(images)):
    print("\n⚠️ WARNING: Duplicate image paths found!")
    from collections import Counter
    counts = Counter(images)
    for img, count in counts.items():
        if count > 1:
            print(f"  - {img} is used {count} times")
else:
    print("\n✅ All image paths are unique.")
