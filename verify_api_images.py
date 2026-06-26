import urllib.request
import json

try:
    with urllib.request.urlopen('http://localhost:5000/products') as response:
        data = response.read().decode()
        products = json.loads(data)
        for p in products:
            print(f"Product: {p.get('name')} | Image: {p.get('mainImage')}")
except Exception as e:
    print(f"Error: {e}")
