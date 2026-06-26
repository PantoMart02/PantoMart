premium_css = """/* ── Premium Page Background System ── */

/* Shared subtle noise texture via pseudo-element */
.product-page::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 180px;
}

/* Product page content sits above noise */
.product-page #product-container { position: relative; z-index: 1; }

/* SKINCARE: soft botanical warmth */
.product-page.category-care {
  background-color: #fdf8f4;
  background-image:
    radial-gradient(ellipse 80% 60% at 15% 5%, rgba(232,218,196,0.6) 0%, transparent 55%),
    radial-gradient(ellipse 60% 50% at 85% 90%, rgba(210,230,215,0.35) 0%, transparent 55%);
}
.dark .product-page.category-care {
  background-color: #141210;
  background-image:
    radial-gradient(ellipse 80% 60% at 15% 5%, rgba(80,58,28,0.55) 0%, transparent 55%),
    radial-gradient(ellipse 60% 50% at 85% 90%, rgba(22,50,32,0.35) 0%, transparent 55%);
}

/* FITNESS: bold contrast with red energy */
.product-page.category-fit {
  background-color: #f6f6f6;
  background-image:
    radial-gradient(ellipse 70% 50% at 90% 5%, rgba(220,38,38,0.07) 0%, transparent 55%),
    radial-gradient(ellipse 50% 40% at 5% 90%, rgba(0,0,0,0.04) 0%, transparent 55%),
    linear-gradient(160deg, #f9f9f9 0%, #efefef 100%);
}
.dark .product-page.category-fit {
  background-color: #0d0d0d;
  background-image:
    radial-gradient(ellipse 70% 50% at 90% 5%, rgba(220,38,38,0.18) 0%, transparent 55%),
    radial-gradient(ellipse 50% 40% at 5% 90%, rgba(185,28,28,0.1) 0%, transparent 55%);
}

/* HOME DECOR: warm stone and linen */
.product-page.category-space {
  background-color: #f9f5ef;
  background-image:
    radial-gradient(ellipse 90% 60% at 10% 5%, rgba(222,202,175,0.65) 0%, transparent 55%),
    radial-gradient(ellipse 70% 50% at 90% 90%, rgba(195,182,155,0.38) 0%, transparent 55%);
}
.dark .product-page.category-space {
  background-color: #12100e;
  background-image:
    radial-gradient(ellipse 90% 60% at 10% 5%, rgba(80,58,26,0.6) 0%, transparent 55%),
    radial-gradient(ellipse 70% 50% at 90% 90%, rgba(60,44,18,0.42) 0%, transparent 55%);
}

/* STYLE: editorial cool off-white */
.product-page.category-style {
  background-color: #faf9f8;
  background-image:
    radial-gradient(ellipse 80% 60% at 5% 0%, rgba(218,213,208,0.55) 0%, transparent 55%),
    radial-gradient(ellipse 60% 50% at 95% 95%, rgba(200,193,186,0.3) 0%, transparent 55%),
    linear-gradient(180deg, #faf9f8 0%, #f2f0ee 100%);
}
.dark .product-page.category-style {
  background-color: #111110;
  background-image:
    radial-gradient(ellipse 80% 60% at 5% 0%, rgba(52,50,46,0.75) 0%, transparent 55%),
    radial-gradient(ellipse 60% 50% at 95% 95%, rgba(40,38,34,0.55) 0%, transparent 55%);
}

/* PET: warm amber and cream */
.product-page.category-pet {
  background-color: #fdf8f2;
  background-image:
    radial-gradient(ellipse 80% 60% at 20% 8%, rgba(235,208,170,0.55) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 88%, rgba(210,183,148,0.32) 0%, transparent 55%);
}
.dark .product-page.category-pet {
  background-color: #130f0a;
  background-image:
    radial-gradient(ellipse 80% 60% at 20% 8%, rgba(90,58,18,0.6) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 88%, rgba(70,44,14,0.42) 0%, transparent 55%);
}

/* Section boxes: frosted glass card effect */
.product-page .section-box {
  background: rgba(255,255,255,0.6) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.8) !important;
  box-shadow: 0 4px 32px rgba(0,0,0,0.05), 0 1px 4px rgba(0,0,0,0.03) !important;
}
.dark .product-page .section-box {
  background: rgba(28,27,27,0.65) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  box-shadow: 0 4px 32px rgba(0,0,0,0.35) !important;
}

"""

with open('assets/css/product.css', 'r', encoding='utf-8') as f:
    existing = f.read()

# Only prepend if not already done
if 'Premium Page Background System' not in existing:
    with open('assets/css/product.css', 'w', encoding='utf-8') as f:
        f.write('/* ===== PRODUCT SPECIFIC STYLES =====  */\n\n' + premium_css + existing.replace('/* ===== PRODUCT SPECIFIC STYLES ===== */', '', 1).lstrip())
    print("Premium backgrounds added.")
else:
    print("Already applied.")
