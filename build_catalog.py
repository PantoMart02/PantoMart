import os
import glob
import random

categories = {
    "care": ("Care", "Clear skin routines", "Daily Hydration Serum"),
    "style": ("Style", "Effortless outfit ideas", "Essential Cotton Tee"),
    "fit": ("Fit", "Simple workout systems", "Minimal Resistance Band"),
    "space": ("Space", "Clean aesthetic spaces", "Minimalist Ceramic Vase"),
    "pet": ("Pet", "Gentle grooming tools", "Everyday Grooming Brush")
}

phrases = ["Premium Essential", "Designed for daily use", "Simple addition", "Effortless upgrade", "Clean aesthetic", "Minimalist choice"]

template_top = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panto{CatName} Catalog | PantoMart</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <nav class="navbar container">
    <a href="/" class="brand-logo"><span class="brand-panto">Panto</span><span class="brand-suffix">{CatName}</span></a>
    <div class="nav-links">
      <a href="/care/">Care</a><a href="/style/">Style</a><a href="/fit/">Fit</a><a href="/space/">Space</a><a href="/pet/">Pet</a>
      <div style="display: flex; gap: 16px; margin-left: 24px; border-left: 1px solid rgba(0,0,0,0.05); padding-left: 24px;">
        <a href="/profile/#wishlist" class="nav-icon" title="Wishlist"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg><div class="badge" id="wish-badge">0</div></a>
        <a href="/profile/#cart" class="nav-icon" title="Cart"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg><div class="badge" id="cart-badge">0</div></a>
      </div>
    </div>
  </nav>

  <!-- Hero Banner for Category -->
  <section class="container" style="margin-top: 32px;">
    <div class="hero" style="min-height: 45vh; border-radius: 32px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; text-align: center; background: var(--accent-soft);">
      <img src="{hero_img}" alt="{CatName} Banner" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; opacity: 0.8;">
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(250,249,246,0.1), rgba(250,249,246,0.95)); z-index: 1;"></div>
      <div style="position: relative; z-index: 2; padding: 40px; max-width: 600px;">
        <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: var(--text-main);">Panto{CatName}</h1>
        <p style="font-size: 1.25rem; color: var(--text-muted);">{subtitle}</p>
      </div>
    </div>
  </section>

  <!-- Products Grid -->
  <section class="container section" style="padding-top: 60px;">
    <div class="masonry-grid">
"""

template_card = """
      <div class="card animate-on-scroll">
        <div class="wishlist-btn" data-id="{cat}-{idx}" data-name="{title}" data-img="{img_path}">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
        </div>
        <a href="/product/{cat}.html">
          <div class="card-img-wrap">
            <img src="{img_path}" alt="{title}">
          </div>
          <div class="card-content" style="padding: 24px;">
            <h3 class="card-title" style="font-size: 1.1rem;">{title}</h3>
            <p class="card-subtitle" style="margin-bottom: 0;">{phrase}</p>
          </div>
        </a>
      </div>
"""

template_bottom = """
    </div>
  </section>
  <footer class="footer"><div class="container text-center text-muted"><p>&copy; 2026 PantoMart. All rights reserved.</p></div></footer>
  <script src="../script.js"></script>
</body>
</html>
"""

base_dir = "IMAGES"
for cat_id, (cat_name, subtitle, main_title) in categories.items():
    # Find all images in this category folder
    images = []
    
    # Check generated gallery images first for a nice banner
    gallery_images = []
    for ext in ('*.png',):
        gallery_images.extend(glob.glob(os.path.join(base_dir, f"{cat_id}_gallery_{ext}")))
    
    # Check main folder
    cat_path = os.path.join(base_dir, cat_id)
    if os.path.exists(cat_path):
        for ext in ('*.jpg', '*.jpeg', '*.png', '*.webp'):
            images.extend(glob.glob(os.path.join(cat_path, ext)))
            
    images.extend(gallery_images)
    
    # Pick hero image (prefer gallery images if they exist, else first image)
    hero_raw = gallery_images[0] if gallery_images else (images[0] if images else "")
    hero_web_path = "../" + hero_raw.replace("\\", "/") if hero_raw else ""
    
    html = template_top.format(CatName=cat_name, subtitle=subtitle, hero_img=hero_web_path)
    
    for idx, img_path in enumerate(images):
        web_path = "../" + img_path.replace("\\", "/")
        title = main_title if idx == 0 else f"{cat_name} Edition {idx+1}"
        phrase = random.choice(phrases)
        html += template_card.format(cat=cat_id, idx=idx, title=title, img_path=web_path, phrase=phrase)
        
    html += template_bottom
    
    # Write the file
    out_dir = cat_id
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Catalog built with Hero Banners successfully.")
