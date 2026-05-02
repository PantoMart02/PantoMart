import os
import glob
import random

# --- DATA POOLS ---
names = ["Priya S.", "Rahul K.", "Aisha M.", "Sarah L.", "Emma T.", "Tom W.", "Vivek T.", "Kavya G.", "Greg F.", "Nina D.", "Chris M.", "Aditya P.", "Mia R.", "Leon R.", "Sunil K."]

review_texts_5 = [
    "Been using this for a few days. Feels absolutely incredible.", 
    "Exactly what I needed. Pure luxury and quality.", 
    "Love the elegant design and how effective it is.", 
    "A perfect, high-end addition to my daily routine.", 
    "Premium quality, definitely worth the investment.", 
    "It does exactly what it promises with such a sophisticated feel."
]
review_texts_4 = [
    "Really nice. Took some time to get used to, but it's very premium overall.", 
    "Great product, though the outer box was slightly dented.", 
    "Works beautifully, just slightly different texture than I expected.", 
    "Solid choice. A bit pricey but the quality justifies it."
]
review_texts_3 = [
    "It's okay, nice but nothing extraordinary.", 
    "Does the job, but shipping took a while.", 
    "Average product, it looks premium but I'm not wowed.", 
    "Slightly larger than I thought, but it's fine."
]

def generate_reviews():
    revs = []
    num_5 = random.choice([3, 4])
    for _ in range(num_5):
        n = random.choice(names)
        t = random.choice(review_texts_5)
        v = '<span class="verified-badge">Verified Purchase</span>' if random.random() > 0.3 else ''
        revs.append(f'<div class="review-card"><div class="review-header"><div><div class="reviewer">{n}</div>{v}</div><div class="stars">★★★★★</div></div><div class="review-text">{t}</div></div>')
    
    num_4 = random.choice([1, 2])
    for _ in range(num_4):
        n = random.choice(names)
        t = random.choice(review_texts_4)
        v = '<span class="verified-badge">Verified Purchase</span>' if random.random() > 0.5 else ''
        revs.append(f'<div class="review-card"><div class="review-header"><div><div class="reviewer">{n}</div>{v}</div><div class="stars">★★★★☆</div></div><div class="review-text">{t}</div></div>')

    n = random.choice(names)
    t = random.choice(review_texts_3)
    revs.append(f'<div class="review-card"><div class="review-header"><div><div class="reviewer">{n}</div></div><div class="stars">★★★☆☆</div></div><div class="review-text">{t}</div></div>')
    
    random.shuffle(revs)
    return "".join(revs), num_5 + num_4 + 1

category_data = {
    "care": {
        "title": "PantoCare Essential",
        "real_names": ["Radiant Glow Serum", "Obsidian Facial Roller", "Golden Elixir Cream", "Midnight Hydration Mask", "Luminous Pearl Cleanser", "Aura Botanical Oil", "Velvet Renewal Polish", "Celestial Eye Cream", "Pure Rosewater Mist", "Silk Barrier Cream", "Vitality Day Defense", "Nourishing Gold Balm", "Opulent Restorative Serum"],
        "descriptions": ["A concentrated serum that visibly brightens skin tone and reduces dark spots. Powered by Vitamin C and Niacinamide, it delivers a luminous, even complexion within weeks of consistent use.", "A facial roller crafted from smooth obsidian stone that reduces puffiness, improves circulation, and helps skincare products absorb deeper. Use it chilled for an instant de-puffing effect.", "A rich, golden-hued facial cream infused with botanical oils and skin-nourishing actives. Melts into the skin overnight and restores firmness and elasticity with each use.", "An indulgent, hydrating mask that replenishes lost moisture and soothes stressed skin. The gel-cream formula leaves skin plump, soft, and deeply refreshed in just 15 minutes.", "A gentle, pearl-infused facial cleanser that removes impurities without stripping the skin barrier. Lathers into a soft foam that leaves skin feeling clean, calm, and balanced.", "A 100% botanical facial oil blend designed to nourish and protect dry or mature skin. Rich in antioxidants, it absorbs quickly and adds a natural, healthy radiance.", "A gentle exfoliating polish that buffs away dull, tired skin to reveal a brighter, smoother complexion. Formulated with micro-exfoliants that are safe for sensitive skin.", "A lightweight eye cream that targets dark circles, puffiness, and fine lines. The cooling applicator tip helps depuff the under-eye area on contact.", "A refreshing facial mist made with pure distilled rosewater. Instantly hydrates and sets makeup, while the natural rose extracts calm and tone the skin throughout the day.", "A ceramide-rich barrier cream that repairs and strengthens compromised skin. Ideal for dry, sensitive, or eczema-prone skin — provides 24-hour hydration and protection.", "A lightweight SPF-infused day cream that shields skin from UV damage while keeping it hydrated. Its invisible finish makes it perfect under makeup or worn alone.", "A rich balm that targets dry patches and delivers intense nourishment. Formulated with gold-infused actives that leave skin soft, supple, and visibly revitalized.", "A potent restorative serum formulated for overnight use. Active peptides and retinol work while you sleep to smooth fine lines and restore a youthful, firm appearance by morning."],
        "hook": ["A luxurious addition to your morning routine.", "Pure, clean hydration for a luminous balance."],
        "problem": "Struggling with dull or inconsistent skin clarity?",
        "solution": "An opulent, balanced formula that integrates seamlessly into your daily luxury routine, providing consistent, glowing care without the fuss.",
        "benefits": ["Effortless luxury application", "Rapid lightweight absorption", "Supports luminous balance", "Elevates your daily routine"],
        "ingredients_para": "Crafted with premium ingredients like pure aloe and active niacinamide, helping keep skin radiant and comfortable.",
        "ingredients_list": ["Pure Aloe Extract – soothes and cools", "Niacinamide – supports flawless clarity", "Vitamin C Complex – improves brightness", "Hyaluronic Acid – locks in deep moisture"],
        "usage": "Apply a small pearl-sized amount to clean skin daily. Massage gently upward until fully absorbed.",
        "qna": [
            ("Is it safe for daily use?", "Yes, it's formulated for gentle, luxurious regular use every day."), 
            ("How long does it take to work?", "Results are gradual, revealing a consistent glow over time."),
            ("Does it leave a heavy residue?", "No, it absorbs rapidly leaving a flawless velvet finish."),
            ("Is it suitable for sensitive skin?", "Yes, the formulation is perfectly balanced for broad compatibility.")
        ]
    },
    "style": {
        "title": "PantoStyle Staple",
        "real_names": ["Cashmere Blend Wrap", "Obsidian Silk Tie", "Golden Thread Blazer", "Minimalist Cotton Tee", "Leather Trim Briefcase", "Midnight Suede Loafers", "Alabaster Knit Sweater", "Onyx Statement Belt", "Tailored Wool Trousers", "Cashmere Overcoat", "Silk Evening Scarf", "Bespoke Cufflinks"],
        "descriptions": ["A supremely soft cashmere wrap that drapes elegantly over any outfit. Hand-finished with clean edges, it transitions seamlessly from office to evening with timeless versatility.", "A precision-woven silk tie with a rich, deep finish. The fabric is tightly woven for a smooth knot and long-lasting shape, making it a wardrobe essential for formal occasions.", "A tailored blazer with fine golden thread detailing through the weave. The structured silhouette provides a powerful, polished look while the lining ensures all-day comfort.", "A minimalist 100% premium cotton tee that feels impossibly soft against the skin. Cut to a relaxed yet refined fit, it pairs effortlessly with tailored trousers or denim.", "A handcrafted briefcase with genuine leather trim and a sleek, structured form. Holds a 15-inch laptop and all daily essentials with smart internal organization.", "A pair of suede loafers in a deep midnight hue. Cushioned insole and flexible sole provide all-day comfort without compromising on the sharp, polished silhouette.", "A fine-knit sweater in an alabaster tone that complements any wardrobe. The breathable knit fabric keeps you warm without bulk, ideal for layering in every season.", "A wide-profile statement belt made from full-grain leather with a matte-black buckle. Adds a sharp finishing touch to trousers, skirts, and tailored outfits.", "Precisely tailored wool-blend trousers with a mid-rise fit and clean front pleat. The high-quality fabric holds its shape through the day and resists creasing.", "A double-breasted cashmere overcoat with a structured collar and clean-lined silhouette. The exceptional warmth-to-weight ratio makes it the ultimate cold-weather luxury staple.", "A hand-hemmed silk evening scarf in a flowing drape. The lightweight construction folds into any bag and instantly elevates any formal or smart-casual look.", "A pair of hand-finished sterling silver cufflinks with an understated geometric design. A refined accent for formal shirts that communicates attention to detail."],
        "hook": ["A high-fashion staple that fits perfectly.", "Effortless, bespoke comfort for everyday wear."],
        "problem": "Tired of fast fashion that loses its shape and elegance?",
        "solution": "A timeless, luxuriously crafted piece designed to effortlessly match your high-end wardrobe, ensuring you always look immaculate.",
        "benefits": ["Effortless sophisticated style", "Premium rich fabric feel", "Maintains flawless shape", "Practical yet luxurious for daily wear"],
        "ingredients_para": "",
        "ingredients_list": [],
        "usage": "Dry clean recommended, or machine wash on delicate cold setting. Do not tumble dry to maintain the premium fabric integrity.",
        "qna": [
            ("Will it shrink?", "It is pre-shrunk premium fabric, but we strongly recommend a cold delicate wash."), 
            ("How does the sizing run?", "Sizing is true to standard bespoke fit. Consider sizing down for a more tailored look."),
            ("Is the material breathable?", "Yes, designed specifically with premium natural fibers for all-day comfort."),
            ("Does it require special ironing?", "We recommend steaming to preserve the delicate finish.")
        ]
    },
    "fit": {
        "title": "PantoFit Essential",
        "real_names": ["AeroCore Resistance Band", "Obsidian Yoga Mat", "Titanium Grip Dumbbell", "Velocity Jump Rope", "Balance Stability Sphere", "Carbon Fiber Kettlebell", "Zenith Recovery Foam Roller", "Aura Fitness Tracker", "Elevate Push-up Grips", "Prime Core Slider", "Apex Pull-up Bar"],
        "descriptions": ["A professional-grade resistance band engineered from natural latex with precision tension control. Suitable for strength training, stretching, and physiotherapy — portable enough to take anywhere.", "A premium non-slip yoga mat with extra cushioning for joint support. The obsidian-textured surface provides exceptional grip in both dry and warm conditions, ideal for all yoga styles.", "A precision-balanced dumbbell with a knurled titanium grip handle that prevents slipping. The compact, rubber-coated head protects floors and reduces noise during intense sessions.", "A speed jump rope with precision ball bearings for effortless, tangle-free rotation. Adjustable cable length and ergonomic grip handles make it suitable for all fitness levels.", "An anti-burst stability ball that supports up to 300 kg and is ideal for core strengthening, balance training, and office use. Comes with a precision pump for easy inflation.", "A solid cast-iron kettlebell with a powder-coated finish for durability and grip. The wide, smooth handle accommodates both single and double-hand exercises with confidence.", "A high-density foam roller with a ridged surface that mimics deep-tissue massage. Effective for post-workout muscle recovery, IT band release, and improving flexibility.", "A slim, precision fitness tracker that monitors heart rate, steps, sleep quality, and calories burned. Water-resistant with a 7-day battery life and real-time health insights.", "Ergonomic push-up handles with a 30-degree rotation that reduces wrist strain and deepens the range of motion. Non-slip rubber base grips securely on any surface.", "A dual sliding disc set for core and full-body workouts on smooth floors or carpet. Activates deep stabilizer muscles and provides a challenging low-impact training option.", "A doorframe pull-up bar with multi-grip positions that installs without screws or drilling. Rated up to 120 kg and features foam-padded grips for a comfortable workout."],
        "hook": ["A clean, premium workout solution.", "Stay highly active with elegant, uncompromised gear."],
        "problem": "Finding time to stay active? Bulky, ugly equipment ruining your home aesthetic?",
        "solution": "A streamlined, highly effective fitness tool that maximizes your workout while looking like a piece of modern art in your living space.",
        "benefits": ["Ultra-portable and lightweight", "Aerospace-grade durable material", "Replaces clunky equipment", "Elegantly intuitive to use"],
        "ingredients_para": "",
        "ingredients_list": [],
        "usage": "Incorporate into your high-performance routine for 20 minutes daily. Wipe clean with a soft damp cloth after use.",
        "qna": [
            ("Is it suitable for beginners?", "Yes, it provides elegant, versatile resistance for all fitness levels."), 
            ("Will it break easily?", "No, it is forged from high-density, premium materials designed to last a lifetime."),
            ("How heavy is it?", "It is meticulously engineered to be lightweight yet profoundly effective."),
            ("Can I use it outdoors?", "Yes, the resilient build makes it suitable for both luxury home gyms and outdoor use.")
        ]
    },
    "space": {
        "title": "PantoSpace Piece",
        "real_names": ["Lumière Crystal Lamp", "Obsidian Abstract Sculpture", "Golden Ratio Planter", "Alabaster Centerpiece Vase", "Midnight Silk Throw", "Aura Diffuser Core", "Eternity Hourglass", "Velvet Accent Cushion", "Nordic Minimalist Clock", "Brass Geometric Bookends", "Onyx Coaster Set"],
        "descriptions": ["A hand-blown crystal table lamp that refracts light into a warm, atmospheric glow. Its sculptural form doubles as a statement art piece even when switched off, transforming any corner of a room.", "A hand-cast obsidian resin sculpture with an abstract flowing form. Each piece has a unique finish, making it a truly one-of-a-kind decorative object for shelves or coffee tables.", "A minimalist geometric planter cast from recycled concrete in a golden ratio proportion. Naturally porous and self-draining, it is ideal for succulents, cacti, and air plants.", "A tall, hand-thrown ceramic vase with an alabaster matte glaze. Its understated, organic silhouette makes it ideal as a standalone centerpiece or as a vessel for dried botanicals.", "A 100% silk-weighted throw in a deep midnight tone. The smooth drape and cool touch make it a luxurious accent for sofas, armchairs, or beds year-round.", "An ultrasonic aroma diffuser with a precision-milled wood core and ceramic top. Operates silently with a cool mist, runs up to 8 hours, and features warm ambient LED lighting.", "A handcrafted hourglass with a brushed brass frame and fine white sand measured to run exactly 30 minutes. A beautiful desk object that doubles as a mindfulness timer.", "A square velvet accent cushion with a hand-stitched edge and premium down-alternative insert. Its deep pile and rich tone add warmth and tactile luxury to any seating space.", "A wall clock with a flat Nordic minimal face — no numbers, just slim hour and minute hands on a clean matte dial. Silent sweep mechanism ensures zero tick noise.", "A pair of solid brass bookends with a precision-cut geometric faceted form. The weighted base holds books firmly while making a bold visual statement on any shelf.", "A set of four onyx stone coasters with a smooth polished top and felt base. Each piece is naturally unique and protects surfaces while adding a luxe, mineral aesthetic to your table."],
        "hook": ["A striking, aesthetic touch for any room.", "Luxurious minimalist design for your curated space."],
        "problem": "Looking for that perfect, high-end minimal decor to tie the room together?",
        "solution": "A precisely crafted artisanal piece that serves as a breathtaking focal point, instantly elevating the aesthetics of your environment.",
        "benefits": ["Instantly elevates room aesthetics", "Flawless premium finish", "Timeless, museum-quality shape", "Blends with modern luxury decor"],
        "ingredients_para": "",
        "ingredients_list": [],
        "usage": "Place in a well-lit area to highlight its texture. Dust occasionally with a dry microfiber cloth to maintain its luster.",
        "qna": [
            ("How do I clean it?", "Gently wipe it with a soft, slightly damp microfiber cloth."), 
            ("Is it fragile?", "It is sturdy, but like all fine art decor, it should be handled with utmost care."),
            ("Does it require assembly?", "No, it arrives fully assembled and ready to display in its premium packaging."),
            ("What are the dimensions?", "It is perfectly proportioned to fit elegantly on standard shelves and luxury side tables.")
        ]
    },
    "pet": {
        "title": "PantoPet Groomer",
        "real_names": ["Royal Velvet Pet Brush", "Obsidian Grooming Comb", "Golden Fleece DeShedder", "Silk Touch Pet Massager", "Aura Pet Wellness Roller", "Midnight Coat Polisher", "Alabaster Paw Cleanser", "Luxe Pet Bath Brush", "Premium Nail Grinder", "Elegance Detangling Spray", "Zenith Pet Towel"],
        "descriptions": ["A soft-bristle grooming brush with a vented velvet pad that distributes natural oils through the coat for a healthy, glossy finish. Suitable for both dogs and cats of all coat types.", "A precision-toothed stainless steel comb with a comfortable anti-slip handle. Effective at detangling mats and removing loose undercoat without scratching the skin.", "A professional-grade deshedding tool with a fine-toothed edge that reaches through the topcoat to remove loose fur from the undercoat. Reduces shedding by up to 90% after regular use.", "A soft silicone massager with flexible nodules that stimulate blood circulation and remove loose hair during bath time. Makes grooming feel like a spa massage for your pet.", "A lightweight grooming roller with gentle rubber bristles that attract and collect loose hair from the coat. Ideal for a quick daily touch-up between baths.", "A finishing brush with ultra-soft boar bristles that smooth and polish the coat to a high sheen. Perfect as a final grooming step to leave your pet looking salon-ready.", "A portable paw-cleaning cup with soft silicone bristles inside. Fill with water, insert your pet's paw, and twist gently to clean mud and debris — no bath required.", "A two-sided bath brush with a shampoo-dispensing side and a soft rubber massage side. Makes bath time thorough, efficient, and enjoyable for pets and owners alike.", "A whisper-quiet electric nail grinder with multiple speed settings and a protective guard. Gently files nails smooth to prevent scratching — stress-free for both pet and owner.", "A lightweight spray bottle with a nourishing formula that loosens knots on contact. Leaves the coat soft, hydrated, and easy to brush through without rinsing.", "A highly absorbent microfibre pet towel that dries coats three times faster than regular towels. The large size wraps around even large breeds and the soft pile is gentle on sensitive skin."],
        "hook": ["A luxurious routine for a pampered pet.", "Gentle, spa-level care for your beloved companion."],
        "problem": "Shedding getting out of hand? Pets hating their uncomfortable grooming time?",
        "solution": "A gentle, highly effective luxury tool that makes grooming a comforting spa experience for your pet and effortlessly easy for you.",
        "benefits": ["Incredibly gentle on sensitive skin", "Reduces shedding significantly with minimal effort", "Ergonomic and elegant to hold", "Quick-release cleaning mechanism"],
        "ingredients_para": "",
        "ingredients_list": [],
        "usage": "Use gentle, sweeping strokes along the direction of the fur. Press the elegant gold release button to instantly remove collected hair.",
        "qna": [
            ("Is this suitable for cats too?", "Yes, it works beautifully for both dogs and cats, offering a gentle massage."), 
            ("Will it scratch my pet's skin?", "No, the precision design completely protects the skin while grooming."),
            ("How often should I use it?", "2-3 times a week is optimal for maintaining a healthy, luxurious coat."),
            ("Is it easy to clean?", "Yes, it is specifically designed for rapid hair release and completely washable.")
        ]
    }
}

product_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | PantoMart Luxury</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="stylesheet" href="../../assets/css/product.css">
</head>
<body data-product-id="{cat}-{idx}">

  <div class="site-banner">
    <strong>PantoMart</strong> | <span>Smart products for everyday life</span>
  </div>

  <nav class="navbar">
    <div class="container flex-between">
      <a href="../../" class="brand-logo"><span class="brand-panto">Panto</span><span class="brand-suffix">{cat_capitalized}</span></a>
      <div class="search-wrap">
        <svg class="search-icon-pos" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="global-search" class="search-input" placeholder="Search our premium collection...">
        <div id="search-dropdown" class="search-dropdown"></div>
      </div>
      <div class="nav-actions">
        <a href="../../profile/#wishlist" class="nav-icon" title="Wishlist"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg><div class="badge" id="wish-badge">0</div></a>
        <a href="../../profile/#cart" class="nav-icon" title="Cart"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg><div class="badge" id="cart-badge">0</div></a>
        <a href="../../login/" class="nav-icon" title="Profile"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></a>
      </div>
    </div>
  </nav>

  <section class="container section">
    <div class="product-layout">
      <!-- HERO GALLERY -->
      <div class="product-gallery">
        <div class="main-img position-relative">
          <button class="wish-btn wish-btn-main" data-id="{cat}-{idx}" data-name="{title}" data-img="{img_path}" title="Add to Wishlist">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          </button>
          <button class="share-btn" onclick="shareProduct()" title="Share Product">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
          </button>
          <img src="{img_path}" id="main-product-image" alt="{title}">
        </div>
      </div>

      <!-- PRODUCT INFO -->
      <div class="product-info">
        <div class="rating-row">
          <div class="stars">★★★★☆</div>
          <div class="rating-count">4.7/5 ({rev_count} Reviews)</div>
        </div>
        <h1 class="product-title">{title}</h1>
        <div class="product-price"><span class="product-price-val">${price}</span> <span class="original">${old_price}</span></div>
        <p class="product-hook">"{hook}"</p>
        
        <div class="labels-row">
          <span class="label-tag accent">Exclusive Edition</span>
          <span class="label-tag">Premium Crafted</span>
          <span class="label-tag">Signature Series</span>
        </div>

        <button class="btn btn-primary btn-full buy-btn mt-3 mb-4" data-id="{cat}-{idx}" data-name="{title}" data-price="${price}" data-img="{img_path}">Add to Cart</button>

        <div class="divider"></div>

        <div class="mb-4">
          <h4 class="mb-2">About This Product</h4>
          <p class="text-muted">{description}</p>
        </div>

        <div class="mb-4">
          <h4 class="mb-2">The Concept</h4>
          <p class="text-muted">{problem}</p>
          <h4 class="mt-3 mb-2">The Execution</h4>
          <p class="text-muted">{solution}</p>
        </div>

        <div class="mb-4">
          <h4 class="mb-2">Why It's Exceptional</h4>
          <ul class="benefits-list text-muted">
            {benefits_html}
          </ul>
        </div>

        {ingredients_html}

        <div class="mb-4">
          <h4 class="mb-2">Care & Usage</h4>
          <p class="text-muted">{usage}</p>
        </div>

        <div class="delivery-box">
          <strong>White Glove Shipping</strong>
          <span class="dynamic-delivery text-muted">Calculating VIP delivery...</span>
        </div>
      </div>
    </div>
  </section>

  <section class="editorial-banner" style="background-image: url('{img_path}');">
    <div class="editorial-overlay"></div>
    <div class="editorial-content">
      <h2>{hook}</h2>
      <p>Experience the ultimate in {cat_capitalized} luxury.</p>
    </div>
  </section>

  <div id="sticky-buy-bar" class="sticky-buy-bar">
    <div style="flex:1;">
      <div style="font-weight:600;font-size:0.9rem;color:var(--white);">{title}</div>
      <div style="color:var(--accent);font-weight:700;">${price}</div>
    </div>
    <button class="btn btn-primary buy-btn" data-id="{cat}-{idx}" data-name="{title}" data-price="${price}" data-img="{img_path}">Add to Cart</button>
  </div>

  <section class="container section">
    <div class="section-head text-center">
      <h2>Curated Companions</h2>
    </div>
    <div class="grid-4" id="related-products-grid">
      {related_html}
    </div>
  </section>

  <section class="container section">
    <div class="section-head text-center">
      <h2>Client Experiences</h2>
      <p>Trusted by our exclusive community</p>
    </div>
    <div style="max-width: 800px; margin: 0 auto;">
      <div class="review-summary">
        <div class="review-big-score">4.7</div>
        <div>
          <div class="stars mb-1">★★★★★</div>
          <div class="text-muted">Based on {rev_count} verified client reviews</div>
        </div>
      </div>
      {reviews_html}
    </div>
  </section>

  <section class="container section">
    <div class="section-head text-center">
      <h2>Frequently Asked Questions</h2>
      <p>Everything you need to know</p>
    </div>
    <div style="max-width: 700px; margin: 0 auto;">
      {qna_html}
    </div>
  </section>

  <footer class="footer">
    <div class="container text-center">
      <div class="footer-logo">Panto<span style="color:var(--accent); font-weight:600; font-style:italic;">Mart</span></div>
      <p style="margin-bottom:24px; font-size:0.9rem; color:var(--muted);">Smart luxury products for elevated living.</p>
      <ul class="footer-links flex-center" style="gap:24px;">
        <li><a href="../../about/">About Us</a></li>
        <li><a href="../../contact/">Concierge</a></li>
        <li><a href="../../terms/">Terms</a></li>
        <li><a href="../../privacy-policy/">Privacy</a></li>
      </ul>
      <div class="footer-bottom">&copy; 2026 PantoMart Luxury. All rights reserved.</div>
    </div>
  </footer>
  <script src="../../assets/js/main.js"></script>
  <script src="../../assets/js/cart.js"></script>
  <script src="../../assets/js/search.js"></script>
  <script src="../../assets/js/delivery.js"></script>
  <script src="../../assets/js/auth.js"></script>
  <script src="../../assets/js/tracking.js"></script>
</body>
</html>
"""

category_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panto{CatName} Luxury Catalog | PantoMart</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/main.css">
  <link rel="stylesheet" href="../assets/css/product.css">
</head>
<body>

  <div class="site-banner">
    <strong>PantoMart</strong> | <span>Smart products for everyday life</span>
  </div>

  <nav class="navbar">
    <div class="container flex-between">
      <a href="../" class="brand-logo"><span class="brand-panto">Panto</span><span class="brand-suffix">{CatName}</span></a>
      <div class="search-wrap">
        <svg class="search-icon-pos" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="global-search" class="search-input" placeholder="Search the collection...">
        <div id="search-dropdown" class="search-dropdown"></div>
      </div>
      <div class="nav-actions">
        <a href="../profile/#wishlist" class="nav-icon" title="Wishlist"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg><div class="badge" id="wish-badge">0</div></a>
        <a href="../profile/#cart" class="nav-icon" title="Cart"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg><div class="badge" id="cart-badge">0</div></a>
        <a href="../login/" class="nav-icon" title="Profile"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></a>
      </div>
    </div>
  </nav>

  <section class="container">
    <div class="cat-banner">
      <h1>Panto{CatName}</h1>
      <p>{subtitle}</p>
    </div>

    <!-- FILTER SYSTEM -->
    <div class="flex-between mb-4" style="background:var(--bg-secondary); padding:20px 24px; border-radius:var(--radius); border:1px solid var(--border-color);">
      <div style="font-weight:500; color:var(--white); letter-spacing:0.1em; text-transform:uppercase; font-size:0.8rem;">Filter Collection:</div>
      <div class="flex" style="gap:16px;">
        <select id="type-filter" style="padding:10px 16px; border:1px solid var(--border-color); background:var(--bg); color:var(--white); border-radius:4px; outline:none; font-family:'Inter', sans-serif;">
          <option>All Types</option>
          <option>Premium</option>
          <option>Standard</option>
        </select>
        <select id="price-filter" style="padding:10px 16px; border:1px solid var(--border-color); background:var(--bg); color:var(--white); border-radius:4px; outline:none; font-family:'Inter', sans-serif;">
          <option>Price: Low to High</option>
          <option>Price: High to Low</option>
        </select>
      </div>
    </div>

    <div class="masonry">
{grid_content}
    </div>
  </section>

  <footer class="footer">
    <div class="container text-center">
      <div class="footer-logo">Panto<span style="color:var(--accent); font-weight:600; font-style:italic;">Mart</span></div>
      <p style="margin-bottom:24px; font-size:0.9rem; color:var(--muted);">Smart luxury products for elevated living.</p>
      <ul class="footer-links flex-center" style="gap:24px;">
        <li><a href="../about/">About Us</a></li>
        <li><a href="../contact/">Concierge</a></li>
        <li><a href="../terms/">Terms</a></li>
        <li><a href="../privacy-policy/">Privacy</a></li>
      </ul>
      <div class="footer-bottom">&copy; 2026 PantoMart Luxury. All rights reserved.</div>
    </div>
  </footer>
  <script src="../assets/js/main.js"></script>
  <script src="../assets/js/cart.js"></script>
  <script src="../assets/js/search.js"></script>
  <script src="../assets/js/delivery.js"></script>
  <script src="../assets/js/auth.js"></script>
  <script src="../assets/js/tracking.js"></script>
</body>
</html>
"""

base_dir = "assets/images/products"
all_products = []

for cat_id, data in category_data.items():
    images = []
    cat_path = os.path.join(base_dir, cat_id)
    if os.path.exists(cat_path):
        for ext in ('*.jpg', '*.jpeg', '*.png', '*.webp'):
            images.extend(glob.glob(os.path.join(cat_path, ext)))
    for ext in ('*.png',):
        images.extend(glob.glob(os.path.join(base_dir, f"{cat_id}_gallery_{ext}")))
    
    # Shuffle real names to avoid obvious ordering
    real_names = data["real_names"][:]
    random.shuffle(real_names)
    
    for idx, img_path in enumerate(images):
        web_path = "../../" + img_path.replace("\\", "/")
        # Assign a real luxurious name, fallback to generic if we run out
        title = real_names[idx] if idx < len(real_names) else f"{data['title']} Signature Edition {idx+1}"
        price_val = random.randint(85, 450) # Increased luxury pricing
        price = f"{price_val}.00"
        slug = title.lower().replace(" ", "-")
        all_products.append({
            "cat": cat_id,
            "idx": idx,
            "slug": slug,
            "title": title,
            "web_path": web_path,
            "price": price,
            "data": data,
            "raw_path": img_path
        })

for cat_id, data in category_data.items():
    cat_name = cat_id.capitalize()
    grid_content = ""
    
    cat_products = [p for p in all_products if p["cat"] == cat_id]
    
    for p in cat_products:
        idx = p["idx"]
        web_path = p["web_path"]
        title = p["title"]
        price = p["price"]
        old_price = f"${float(price) + 45}.00"
        
        ben_html = "".join([f"<li>{b}</li>" for b in data["benefits"]])
        
        if data["ingredients_para"]:
            ing_list_html = "".join([f"<li>{il}</li>" for il in data["ingredients_list"]])
            ing_html = f"""
            <div class="ingredient-box">
              <h4>Premium Ingredients</h4>
              <p class="text-muted mb-3">{data['ingredients_para']}</p>
              <ul class="ingredient-list text-muted">
                {ing_list_html}
              </ul>
            </div>
            """
        else:
            ing_html = ""
            
        qna_html = "".join([f"<div class='qa-item'><div class='qa-q'>Q: {q[0]}</div><div class='qa-a'>A: {q[1]}</div></div>" for q in data["qna"]])
        
        reviews_str, total_revs = generate_reviews()
        real_rev_count = random.randint(320, 850)
        
        same_cat_products = [p for p in all_products if p["cat"] == cat_id and p["idx"] != idx]
        if len(same_cat_products) >= 4:
            related_subset = random.sample(same_cat_products, 4)
        else:
            related_subset = same_cat_products
        related_html = ""
        for rel in related_subset:
            phrase = random.choice(["Curated Choice", "Signature Piece", "Bespoke Essential"])
            related_html += f"""
            <div class="card aos" data-search-name="{rel['title']}" data-search-url="../../{rel['cat']}/{rel['slug']}/" data-search-cat="{rel['cat']}">
              <a href="../../{rel['cat']}/{rel['slug']}/">
                <div class="card-img-wrap"><img src="{rel['web_path']}" alt="{rel['title']}"></div>
                <div class="card-body">
                  <div class="card-title">{rel['title']}</div>
                  <div class="card-sub">{phrase}</div>
                  <div class="card-price">${rel['price']}</div>
                </div>
              </a>
            </div>"""

        # Get per-product description
        descriptions = data.get("descriptions", [])
        description = descriptions[idx] if idx < len(descriptions) else data["solution"]
        
        html = product_template.format(
            title=title,
            cat_capitalized=cat_name,
            cat=cat_id,
            idx=idx,
            img_path=web_path,
            price=price,
            old_price=old_price,
            rev_count=real_rev_count,
            hook=random.choice(data["hook"]),
            problem=data["problem"],
            solution=data["solution"],
            usage=data["usage"],
            benefits_html=ben_html,
            ingredients_html=ing_html,
            reviews_html=reviews_str,
            qna_html=qna_html,
            related_html=related_html,
            description=description
        )
        
        slug = p["slug"]
        prod_file = f"{cat_id}/{slug}/index.html"
        os.makedirs(f"{cat_id}/{slug}", exist_ok=True)
        with open(prod_file, "w", encoding="utf-8") as f:
            f.write(html)
            
        phrase = random.choice(["Curated Choice", "Signature Piece", "Bespoke Essential", "Exclusive Addition"])
        grid_content += f"""
      <div class="card aos" data-search-name="{title}" data-search-url="/{cat_id}/{slug}/" data-search-cat="{cat_name}">
        <button class="wish-btn" data-id="{cat_id}-{idx}" data-name="{title}" data-img="{web_path}" data-url="../../{cat_id}/{slug}/">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
        </button>
        <a href="../../{cat_id}/{slug}/">
          <div class="card-img-wrap"><img src="{web_path}" alt="{title}"></div>
          <div class="card-body">
            <h3 class="card-title">{title}</h3>
            <p class="card-sub">{phrase}</p>
            <div class="card-price">${price}</div>
          </div>
        </a>
      </div>"""
      
    if not os.path.exists(cat_id):
        os.makedirs(cat_id)
    with open(f"{cat_id}/index.html", "w", encoding="utf-8") as f:
        f.write(category_template.format(CatName=cat_name, subtitle=data["title"] + " Luxury Collection", grid_content=grid_content))

print("Successfully generated luxury PantoMart with real names and updated aesthetics.")
