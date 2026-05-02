import sys

with open('build_all_products.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove shuffle
content = content.replace('random.shuffle(real_names)', '# random.shuffle(real_names)  # Removed so names match images consistently')

# 2. Update price to INR
content = content.replace('price_val = random.randint(85, 450) # Increased luxury pricing\\n        price = f"{price_val}.00"', 'price_val = random.randint(3500, 25000)\\n        price = f"₹{price_val:,}"')
content = content.replace('old_price = f"${float(price) + 45}.00"', 'old_price = f"₹{price_val + random.randint(1500, 5000):,}"')

# 3. Remove $ from HTML
content = content.replace('>${price}</span>', '>{price}</span>')
content = content.replace('data-price="${price}"', 'data-price="{price}"')
content = content.replace('>${rel[\\'price\\']}</div>', '>{rel[\\'price\\']}</div>')
content = content.replace('>${price}</div>', '>{price}</div>')

# 4. Update category_template to have a background image
old_cat_hero = """  <section class="category-hero flex-center" style="min-height:40vh; background:var(--bg-secondary);">
    <div class="text-center aos">
      <h1 style="font-size:3rem; margin-bottom:16px;">{CatName}</h1>
      <p class="text-muted" style="font-size:1.2rem;">{subtitle}</p>
    </div>
  </section>"""

new_cat_hero = """  <section class="category-hero flex-center position-relative" style="min-height:40vh; background-image: url('{cat_bg}'); background-size: cover; background-position: center;">
    <div class="editorial-overlay" style="position: absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:1;"></div>
    <div class="text-center aos" style="position:relative; z-index:2; color:#fff;">
      <h1 style="font-size:3rem; margin-bottom:16px; color:#fff;">{CatName}</h1>
      <p style="font-size:1.2rem; color:#f8f8f8;">{subtitle}</p>
    </div>
  </section>"""
content = content.replace(old_cat_hero, new_cat_hero)

# 5. Inject cat_bg into category_template.format
old_format = 'f.write(category_template.format(CatName=cat_name, subtitle=data["title"] + " Luxury Collection", grid_content=cat_grid_content))'
new_format = 'cat_bg_img = cat_products[0]["web_path"].replace("../../", "../") if cat_products else ""\\n        f.write(category_template.format(CatName=cat_name, subtitle=data["title"] + " Luxury Collection", grid_content=cat_grid_content, cat_bg=cat_bg_img))'
content = content.replace(old_format, new_format)

with open('build_all_products.py', 'w', encoding='utf-8') as f:
    f.write(content)
