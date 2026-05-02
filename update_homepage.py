import os
import glob
import random

categories = ["care", "style", "fit", "space", "pet"]
base_dir = "IMAGES"
all_cards = ""

for cat_id in categories:
    images = []
    gallery_images = []
    for ext in ('*.png',):
        gallery_images.extend(glob.glob(os.path.join(base_dir, f"{cat_id}_gallery_{ext}")))
    cat_path = os.path.join(base_dir, cat_id)
    if os.path.exists(cat_path):
        for ext in ('*.jpg', '*.jpeg', '*.png', '*.webp'):
            images.extend(glob.glob(os.path.join(cat_path, ext)))
    images.extend(gallery_images)
    
    for idx, img_path in enumerate(images):
        web_path = "/" + img_path.replace("\\", "/") # Use absolute root path
        title = f"Panto{cat_id.capitalize()} Edition {idx+1}"
        phrase = random.choice(["Premium Essential", "Designed for daily use", "Simple addition", "Effortless upgrade"])
        
        all_cards += f"""
      <div class="card animate-on-scroll" style="margin-bottom:40px; break-inside: avoid;">
        <div class="wishlist-btn" data-id="{cat_id}-{idx}" data-name="{title}" data-img="{web_path}" style="position: absolute; top: 16px; right: 16px; width: 36px; height: 36px; background: var(--white); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.1); z-index: 2; color: var(--text-muted);">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
        </div>
        <a href="/product/{cat_id}-{idx}.html">
          <div class="card-img-wrap" style="position: relative; overflow: hidden; background: var(--accent-soft);">
            <img src="{web_path}" alt="{title}" style="width: 100%; display: block; transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);">
          </div>
          <div class="card-content" style="padding: 24px;">
            <h3 class="card-title" style="font-size: 1.1rem; font-family: 'Playfair Display', serif; margin-bottom: 8px;">{title}</h3>
            <p class="card-subtitle" style="margin-bottom: 0; color: var(--text-muted); font-size: 0.95rem;">{phrase}</p>
          </div>
        </a>
      </div>"""

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the categories section
import re
new_section = f"""<!-- Category Section -->
  <section id="categories" class="container section animate-on-scroll">
    <div class="text-center mb-5">
      <h2>All Premium Products</h2>
      <p class="text-muted">Explore our complete catalog of essentials.</p>
    </div>
    
    <div class="masonry-grid" style="column-count: 3; column-gap: 40px; margin-top: 48px;">
{all_cards}
    </div>
  </section>"""

# Find the section and replace it
# The section is between <!-- Category Section --> and <!-- Value Section -->
pattern = r"<!-- Category Section -->.*?<!-- Value Section -->"
content = re.sub(pattern, new_section + "\n\n  <!-- Value Section -->", content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Homepage updated with all 60 products!")
