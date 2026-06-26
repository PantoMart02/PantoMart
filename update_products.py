import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r') as f:
    products = json.load(f)

# Update product 1 (Sunscreen)
p1 = {
    'name': 'Plum Rice Water & Niacinamide 2% Hybrid Sunscreen',
    'price': 499,
    'category': 'care',
    'mainImage': '/assets/images/products/care/1.jpg',
    'tagline': 'Protection that works. Skincare that transforms.',
    'hook': {
        'headline': 'You Wash Your Face Every Morning. So Why Does Your Skin Still Look Tired, Tan, and Uneven?',
        'problem': 'You\'re doing everything right. Cleanser. Moisturiser. Maybe even a serum. But every time you step into the sun — even for 10 minutes — your skin pays the price. Darker around the cheeks. A little duller than yesterday. Those patches you\'ve been fighting for months? Still there. Still winning. The truth no one tells you: skincare without sunscreen is skincare going backwards.',
        'solution': 'Introducing Plum Rice Water & Niacinamide 2% Hybrid Sunscreen SPF 50 PA++++. This isn\'t just a sunscreen. It\'s the daily ritual your skin has been waiting for — a hybrid formula that shields, brightens, and fades tan simultaneously, while feeling like nothing on your skin. Lightweight. Non-greasy. Built for Indian skin and Indian sun.'
    },
    'benefits': [
        {'title': 'Your Tan Meets Its Match', 'desc': '3x faster tan reduction means the damage the sun has been quietly building — undone.', 'icon': '☀️'},
        {'title': 'Glow That Doesn\'t Wash Off', 'desc': 'Rice water has softened and brightened skin for generations.', 'icon': '✨'},
        {'title': 'Hydration That Lasts', 'desc': 'No more tight, parched skin by afternoon. The formula locks in moisture.', 'icon': '💧'},
        {'title': 'Zero White Cast', 'desc': 'Non-comedogenic means it won\'t clog your pores or trigger acne. It disappears into skin.', 'icon': '🌿'}
    ],
    'ingredients': [
        {'name': 'Rice Water', 'desc': 'Used for centuries across Asia for soft, glowing skin. It calms inflammation, reduces dark spots, and gives skin a natural luminosity.', 'icon': '🌾'},
        {'name': 'Niacinamide 2%', 'desc': 'Visibly fades pigmentation, minimises enlarged pores, and strengthens the skin barrier so it can defend itself better.', 'icon': '🧪'},
        {'name': 'Hybrid Technology', 'desc': 'Physical filters reflect UV rays instantly. Chemical filters absorb and neutralise them. Seamless, full-spectrum protection.', 'icon': '🛡️'}
    ],
    'howToUse': [
        {'step': 'Cleanse', 'desc': 'Start with a clean, dry face. Pat gently. No need to rush.'},
        {'step': 'Apply', 'desc': 'Take a coin-sized amount. Dot across forehead, cheeks, nose, and chin. Blend outward.'},
        {'step': 'Go', 'desc': 'That\'s it. No waiting. No white cast to blend away.'}
    ],
    'reviews': [
        {'name': 'Priya R.', 'quote': 'My pigmentation has visibly lightened. The texture is so light I forget I\'m wearing sunscreen.', 'stars': 5},
        {'name': 'Arjun M.', 'quote': 'The water resistance is real — I sweat a lot and it holds up. Game changer.', 'stars': 5},
        {'name': 'Sneha T.', 'quote': 'I have acne-prone skin and I was terrified this would break me out. It didn\'t. Not even a little.', 'stars': 5}
    ],
    'rating': 4.9,
    'reviewsCount': 12000
}

# Update product 2 (Night Gel)
p2 = {
    'name': 'Plum Green Tea Renewed Clarity Night Gel',
    'price': 575,
    'category': 'care',
    'mainImage': '/assets/images/products/care/2.jpg',
    'tagline': 'Your skin\'s overnight reset. While you sleep, it works.',
    'hook': {
        'headline': 'You wash your face every night. So why do you still wake up looking tired, dull, and broken out?',
        'problem': 'Your skin is working against you while you sleep — clogging, dulling, aging — and your basic moisturizer is doing absolutely nothing to stop it.',
        'solution': 'You deserve to wake up to skin that looks rested, clear, and radiant. Not puffy. Not congested. Not "good for my age." Just genuinely, effortlessly glowing skin — every single morning.'
    },
    'benefits': [
        {'title': 'Glowing, Not Greasy', 'desc': 'Lightweight gel absorbs fully, so you feel nothing but soft, dewy skin by morning.', 'icon': '✨'},
        {'title': 'Breakouts Don\'t Stand A Chance', 'desc': 'Overnight, it quietly unclogs pores and calms inflammation you didn\'t notice.', 'icon': '🌿'},
        {'title': 'Dark Spots Visibly Fade', 'desc': 'Week by week, your skin tone becomes more even, more lit-from-within.', 'icon': '🌙'},
        {'title': 'Zero Tightness', 'desc': 'Just deeply hydrated, plump skin that bounces back when you touch it.', 'icon': '💧'}
    ],
    'ingredients': [
        {'name': 'Green Tea Extract', 'desc': 'Loaded with antioxidants, it fights daily damage — pollution, stress, screen time. Clears congestion.', 'icon': '🍵'},
        {'name': 'Glycolic Acid', 'desc': 'Works while you sleep to gently resurface your skin, fading spots and smoothing texture.', 'icon': '🧪'},
        {'name': 'Hyaluronic Acid', 'desc': 'Pulls moisture deep into the skin and holds it there all night so you wake up plump.', 'icon': '💧'}
    ],
    'howToUse': [
        {'step': 'Cleanse', 'desc': 'Cleanse your face thoroughly at night.'},
        {'step': 'Apply', 'desc': 'Take a small amount of gel (a pea-sized amount is enough) and apply across face.'},
        {'step': 'Sleep', 'desc': 'Let it absorb fully — no rinsing needed. Sleep. Wake up glowing.'}
    ],
    'reviews': [
        {'name': 'Ananya R.', 'quote': 'Within 3 weeks of using this, my skin looked cleaner than it ever has.', 'stars': 5},
        {'name': 'Priya M.', 'quote': 'My skin used to look so dull. Now people keep asking me if I\'m doing something different.', 'stars': 5},
        {'name': 'Shreya K.', 'quote': 'Lightweight, non-sticky, and actually works. My dark spots have genuinely faded.', 'stars': 5}
    ],
    'rating': 4.8,
    'reviewsCount': 8500
}

care_count = 0
for i in range(len(products)):
    if products[i]['category'] == 'care':
        if care_count == 0:
            products[i].update(p1)
        elif care_count == 1:
            products[i].update(p2)
        care_count += 1

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w') as f:
    json.dump(products, f, indent=2)

print('Updated products.json successfully')
