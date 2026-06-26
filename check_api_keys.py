import requests
import json

try:
    r = requests.get('http://localhost:5000/products')
    products = r.json()
    for p in products:
        print(f"Product: {p.get('name')} - Keys: {list(p.keys())}")
except Exception as e:
    print(f"Error: {e}")
