import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panto{CatName} | PantoMart</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <nav class="navbar container">
    <a href="/" class="brand-logo"><span class="brand-panto">Panto</span><span class="brand-suffix">{CatName}</span></a>
    <div class="nav-links">
      <a href="/care/">Care</a><a href="/style/">Style</a><a href="/fit/">Fit</a><a href="/space/">Space</a><a href="/pet/">Pet</a>
      <div style="display: flex; gap: 16px; margin-left: 24px; border-left: 1px solid var(--secondary); padding-left: 24px;">
        <a href="/profile/#wishlist" class="nav-icon" title="Wishlist"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg><div class="badge" id="wish-badge">0</div></a>
        <a href="/profile/#cart" class="nav-icon" title="Cart"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg><div class="badge" id="cart-badge">0</div></a>
      </div>
    </div>
  </nav>

  <section class="container section">
    <h1 class="text-center mb-5">Panto{CatName} Collection</h1>
    <div class="card-grid" style="max-width: 400px; margin: 0 auto;">
      <a href="/product/{cat_lower}.html" class="card">
        <div class="card-img-wrap">
          <img src="{img_path}" alt="{title}">
        </div>
        <div class="card-content">
          <h3 class="card-title">{title}</h3>
          <p class="card-subtitle">{subtitle}</p>
        </div>
      </a>
    </div>
  </section>
  <footer class="footer" style="position: absolute; bottom: 0; width: 100%;"><div class="container text-center text-muted"><p>&copy; 2026 PantoMart. All rights reserved.</p></div></footer>
  <script src="../script.js"></script>
</body>
</html>"""

categories = [
    ("Care", "care", "../IMAGES/care/618kh-4NkxL._SY879_.jpg", "Daily Hydration Serum", "Clear skin routines"),
    ("Style", "style", "../IMAGES/style/51ZMqctLSyL._SY879_.jpg", "Essential Cotton Tee", "Effortless outfit ideas"),
    ("Fit", "fit", "../IMAGES/fit/51D5TWsGAsL._SY300_SX300_QL70_FMwebp_.webp", "Minimal Resistance Band", "Simple workout systems"),
    ("Space", "space", "../IMAGES/space/51TS-8zqmvL._SY300_SX300_QL70_FMwebp_.webp", "Minimalist Ceramic Vase", "Clean aesthetic spaces"),
    ("Pet", "pet", "../IMAGES/pet/41RpccfhbLL._SY300_SX300_QL70_FMwebp_.webp", "Everyday Grooming Brush", "Gentle grooming tools")
]

for name, folder, img, title, subtitle in categories:
    content = template.format(CatName=name, cat_lower=folder, img_path=img, title=title, subtitle=subtitle)
    with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
        f.write(content)

print("Categories built.")
