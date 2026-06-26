import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

p3 = {
    'name': 'Bare Anatomy Rosemary & Rice Water Hair Growth Spray',
    'price': 500,
    'category': 'care',
    'mainImage': '/assets/images/products/care/3.jpg',
    'tagline': 'Clinically inspired. Effortlessly simple. Visibly powerful.',
    'hook': {
        'headline': "You're losing more hair than you're growing. And deep down, you know it.",
        'problem': "You've tried the oils. The masks. The \"miracle\" shampoos. And every morning, the shower drain tells you the same painful truth — it's not working. Thinning edges. Slower growth. Hair that used to feel thick and full — now feels like a shadow of itself.",
        'solution': "Imagine running your fingers through hair that's actually growing back. Thicker strands. A fuller hairline. Introducing Bare Anatomy Rosemary & Rice Water Hair Growth Spray. That confidence isn't gone. It's just waiting for the right formula."
    },
    'benefits': [
        {'title': 'Hair Starts Growing Again', 'desc': 'Targets dormant follicles and reactivates them so you see real, measurable growth.', 'icon': '🌱'},
        {'title': 'Shedding Slows Down', 'desc': 'Less hair on your pillow, less hair in your brush, less heartbreak every morning.', 'icon': '🛑'},
        {'title': 'Scalp Feels Healthy', 'desc': 'No more itchiness, buildup, or uncomfortable tightness.', 'icon': '✨'},
        {'title': 'Thicker & Stronger', 'desc': 'Not just longer, but fuller, with actual density you can see and feel.', 'icon': '💪'}
    ],
    'ingredients': [
        {'name': 'Rosemary Extract', 'desc': 'Clinically shown to stimulate hair follicles and improve scalp circulation. Wakes your scalp up from a long sleep.', 'icon': '🌿'},
        {'name': 'Rice Water', 'desc': 'Rich in inositol and amino acids, it penetrates the hair shaft to repair damage from within.', 'icon': '🍚'},
        {'name': 'Scalp-Balancing Actives', 'desc': 'Regulate excess oil and buildup that silently suffocate follicles — because a clean scalp is a growing scalp.', 'icon': '💧'}
    ],
    'howToUse': [
        {'step': 'Part', 'desc': 'Part your hair into sections to expose the scalp.'},
        {'step': 'Spray', 'desc': 'Spray directly onto the scalp — not just the hair.'},
        {'step': 'Massage', 'desc': 'Massage gently with fingertips for 1–2 minutes.'},
        {'step': 'Leave In', 'desc': 'Do NOT rinse. Leave it in. Use daily or every alternate day.'}
    ],
    'reviews': [
        {'name': 'Divya S.', 'quote': 'After 5 weeks of this spray, I can see actual baby hair along my hairline. I cried happy tears.', 'stars': 5},
        {'name': 'Ritu A.', 'quote': 'Postpartum hair fall destroyed my confidence. This is the only thing that actually helped.', 'stars': 5},
        {'name': 'Karan M.', 'quote': 'I\'ve spent thousands on hair treatments at salons. This spray did more in 6 weeks than any of them.', 'stars': 5}
    ],
    'riskReversal': [
        'Free from sulphates, parabens & silicones',
        'No harmful steroids or DHT-blockers',
        'Safe for color-treated hair',
        'Suitable for all hair types'
    ],
    'urgency': 'High demand alert — this batch is nearly sold out. Stock sells out without warning.',
    'rating': 4.9,
    'reviewsCount': 10500
}

care_count = 0
for i in range(len(products)):
    if products[i]['category'] == 'care':
        if care_count == 2:  # Third item
            products[i].update(p3)
            break
        care_count += 1

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print('Updated 3rd product successfully')
