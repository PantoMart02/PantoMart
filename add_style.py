import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Product 1: Blue Stripe Oxford Button-Down Shirt
p1 = {
    'name': 'Blue Stripe Oxford Button-Down Shirt',
    'price': 1299,
    'category': 'style',
    'mainImage': '/assets/images/products/style/1.jpg',
    'tagline': 'Where relaxed confidence meets sharp, timeless style.',
    'hook': {
        'headline': 'The Man Who Walks In Doesn\'t Need to Introduce Himself.',
        'problem': 'Some men dress to be seen. Others dress to be remembered. This is for the second kind. One shirt. One decision. An entirely different version of how the world sees you — and more importantly, how you see yourself.',
        'solution': 'You Already Know the Feeling. The room shifts slightly when you walk in dressed right. Conversations start easier. Handshakes feel firmer. People lean in a little closer when you talk. That\'s not arrogance. That\'s the quiet power of a man who looks composed, intentional, and effortlessly put-together. Picture it: sunglasses on, collar slightly open, sleeves casually rolled — and every eye in the room doing a double take. That\'s not a fantasy. That\'s Tuesday in this shirt.'
    },
    'benefits': [
        {'title': 'Instant Upgrade, Zero Effort', 'desc': 'Throw this on and you look like you planned your outfit for an hour. You didn\'t have to. That\'s the point.', 'icon': '🔵'},
        {'title': 'Command Respect in Any Room', 'desc': 'Whether it\'s a client meeting, a rooftop brunch, or a first date — this shirt communicates taste, calm authority, and quiet confidence without a single word.', 'icon': '🤝'},
        {'title': 'Effortlessly Versatile', 'desc': 'One shirt. Ten occasions. You\'ll reach for it again and again because it works — every single time.', 'icon': '☀️'},
        {'title': 'That "Who Is He?" Energy', 'desc': 'There\'s a version of you that turns heads without trying. This shirt is how you find him.', 'icon': '😎'},
        {'title': 'Sharp Without Being Stiff', 'desc': 'Smart enough for the boardroom. Relaxed enough for the weekend. The rare shirt that genuinely does both.', 'icon': '✅'}
    ],
    'materialText': 'Built to Feel as Good as It Looks. Crafted from premium 100% cotton Oxford fabric — soft against your skin from the very first wear, yet structured enough to hold its shape through every hour of your day. The weave breathes. The colour doesn\'t fade. The buttons stay put. This is the kind of shirt that gets better with every wash — not worse. Quality you can feel the moment you pick it up. Attention to detail that only reveals itself up close: reinforced seams, precision-stitched stripe alignment, a collar that lays flat without pins or stays. Made for men who notice the difference. And wear it accordingly.',
    'howToUse': [
        {'step': 'The Polished Casual', 'desc': 'Pair with slim chinos or beige trousers. White sneakers or loafers. Sunglasses on. Top button open, sleeves rolled to the forearm. Effortless and sharp.'},
        {'step': 'The Sharp Professional', 'desc': 'Tuck it clean into tailored dark trousers or navy chinos. Add a tan leather belt and Oxford shoes. Leave the blazer at home — this shirt does the talking.'},
        {'step': 'The Weekend Off-Duty', 'desc': 'Over a white tee, unbuttoned and relaxed, with dark denim and clean white sneakers. Add a watch. Walk slowly.'},
        {'step': 'The Evening Upgrade', 'desc': 'Half-tuck into slim black trousers. Roll the sleeves once. Minimal jewellery. Transitions from day to dinner without missing a beat.'}
    ],
    'reviews': [
        {'name': 'Aryan S., Delhi', 'quote': 'I wore this to a work presentation and my manager asked me where I bought it before the meeting even started. Three compliments in one day.', 'stars': 5},
        {'name': 'Rohan M., Mumbai', 'quote': 'I\'ve bought a lot of shirts. This one hits differently. The fit, the colour, the way it sits on the shoulders — it just looks expensive.', 'stars': 5},
        {'name': 'Vikram T., Bengaluru', 'quote': 'I\'m usually a t-shirt guy. This shirt made me reconsider my entire wardrobe. Wore it to a casual Friday at work and three people asked if I had a meeting.', 'stars': 5},
        {'name': 'Kabir R., Hyderabad', 'quote': 'The stripe alignment is actually perfect — even at the pocket seam. That kind of detail tells you everything about the quality.', 'stars': 5}
    ],
    'urgency': '⚠️ Limited Pieces Available in This Colourway. Once these sell out, they\'re gone. Over 2,400 men added this to their wardrobe in the last 30 days alone.',
    'rating': 4.9,
    'reviewsCount': 2400
}

# Product 2: Dreamer Colorblock Hoodie
p2 = {
    'name': 'Dreamer Colorblock Hoodie',
    'price': 1499,
    'category': 'style',
    'mainImage': '/assets/images/products/style/2.jpg',
    'tagline': 'Not just a hoodie. A statement of who you\'re becoming.',
    'hook': {
        'headline': 'The Ones Who Dream Different, Dress Different.',
        'problem': 'There\'s a version of you that walks into a room and doesn\'t need to announce anything. Your presence does it. Your style does it. You already know who you are — your clothes just need to say it louder.',
        'solution': 'People notice the ones who look effortlessly put-together. Not overdressed. Not trying too hard. Just right. The kind of person who looks like they have somewhere cool to be — and always do. That\'s the energy this piece carries. Quiet confidence. Intentional cool. Unmistakably you.'
    },
    'benefits': [
        {'title': 'Sharp Without Trying', 'desc': 'The colorblock structure gives instant visual impact, even on the most casual days.', 'icon': '🖤'},
        {'title': 'Fits Every Version of Your Day', 'desc': 'Morning coffee run to late-night hangs, this hoodie transitions flawlessly.', 'icon': '☕'},
        {'title': 'Quiet Edge', 'desc': 'The embroidered script detail adds personality that sets you apart from every basic hoodie in the room.', 'icon': '✨'},
        {'title': 'Comfort That Looks Expensive', 'desc': 'Relaxed enough to live in, structured enough to actually look good in.', 'icon': '💯'}
    ],
    'materialText': 'Crafted from premium heavyweight fleece that feels substantial — not flimsy, not thin, not the kind that pills after two washes. The inner lining is soft against skin, the cuffs hold their shape, and the kangaroo pocket sits perfectly for that casual, hands-in stance that never goes out of style. The drawstring hood is reinforced and structured — it lays right, every time. This is the hoodie you keep. The one that survives every season, every wash, every phase of your life.',
    'howToUse': [
        {'step': 'The Effortless Casual Look', 'desc': 'Pair with straight-fit dark jeans and white sneakers. Clean, sharp, done.'},
        {'step': 'The Streetwear Statement', 'desc': 'Layer over a white longline tee, cargo pants, and chunky sneakers. Add a cap — own the street.'},
        {'step': 'The Travel-Ready Look', 'desc': 'Grey joggers, this hoodie, clean white shoes. Comfortable enough for a flight, cool enough for anywhere you land.'},
        {'step': 'The Layered Winter Look', 'desc': 'Throw a long overcoat on top, wear it with slim trousers and boots. Casual meets elevated — effortlessly.'}
    ],
    'reviews': [
        {'name': 'Arjun S., Pune', 'quote': 'I wore this to college on a random Tuesday and got three compliments before lunch. It just has this vibe that\'s hard to explain.', 'stars': 5},
        {'name': 'Rohan M., Delhi', 'quote': 'I\'ve bought so many hoodies. This is the only one where I actually feel cool wearing it, not just comfortable. The quality is insane for the price.', 'stars': 5},
        {'name': 'Karan V., Hyderabad', 'quote': 'The "dreamer" text got me. Bought it on impulse. Wore it the same day. Haven\'t stopped getting asked about it.', 'stars': 5},
        {'name': 'Nikhil T., Mumbai', 'quote': 'Fits perfectly, doesn\'t shrink, doesn\'t fade. My go-to piece for everything now.', 'stars': 5}
    ],
    'urgency': 'Limited pieces. High demand. This colorway moves fast — once this batch is gone, restock is not guaranteed.',
    'rating': 4.8,
    'reviewsCount': 1850
}

# Product 3: Maroon & Gold Silk Lehenga Choli
p3 = {
    'name': 'Maroon & Gold Silk Lehenga Choli',
    'price': 4999,
    'category': 'style',
    'mainImage': '/assets/images/products/style/8.jpg',
    'tagline': 'For the woman who doesn\'t just attend celebrations — she becomes the celebration.',
    'hook': {
        'headline': 'Walk In Like You Were Born For This Moment.',
        'problem': 'There are women who enter a room — and then there are women who change a room. The music seems to pause. Eyes follow. Conversations stop mid-sentence. It\'s not magic. It\'s presence. And presence begins with how you show up.',
        'solution': 'When you\'re dressed in something that carries centuries of artistry, you don\'t just look beautiful — you command the room. People lean in. They admire. They remember you long after the evening ends. That\'s not vanity. That\'s the quiet power of a woman who knows exactly who she is.'
    },
    'benefits': [
        {'title': 'Instant Regal Presence', 'desc': 'The richness of the color combination commands attention without demanding it.', 'icon': '👑'},
        {'title': 'Confidence from the Outside In', 'desc': 'When you know you look extraordinary, you become extraordinary.', 'icon': '✨'},
        {'title': 'Celebrates Every Curve', 'desc': 'The flared lehenga drapes and moves with you, creating a picture-perfect silhouette at every angle.', 'icon': '💃'},
        {'title': 'Timeless, Not Trendy', 'desc': 'This isn\'t a "this season" piece. This is the outfit you\'ll look back at in photographs twenty years from now and feel breathless.', 'icon': '⏳'}
    ],
    'materialText': 'The lehenga skirt is woven from rich silk-blend fabric — heavy enough to hold its flare, smooth enough to drape like a dream. The golden woven motifs across the skirt body are inspired by South Indian temple artistry, layered with a deep rust-and-gold bordered hem that anchors the entire look in timeless grandeur. The maroon blouse and dupatta feature hand-finished zari embroidery — golden floral work that catches light beautifully whether you\'re indoors under chandeliers or outdoors under the sun. The dupatta falls with natural weight, styled effortlessly across the shoulder. Built to last. Built to be passed down. Built to be remembered.',
    'howToUse': [
        {'step': 'The Bridal Guest Look', 'desc': 'Pair with polki or kundan jewellery — statement earrings, maang tikka, and stacked gold bangles. Opt for a neat bun with fresh flowers. Arrive last. Leave an impression that stays forever.'},
        {'step': 'The Festival Look', 'desc': 'Keep jewellery minimal — just gold jhumkas and a thin necklace. Let the lehenga do the talking. Loose waves, a bindi, and block heels complete the look effortlessly.'},
        {'step': 'The Family Celebration Look', 'desc': 'Style with antique gold jewellery and a sleek low bun with a centre part. Understated, elegant, and completely captivating.'},
        {'step': 'The Dance Floor Look', 'desc': 'Let the dupatta drape loose, hair open with soft curls. The flared skirt was made for movement — it photographs beautifully and flows even better when you dance.'}
    ],
    'reviews': [
        {'name': 'Lakshmi R., Chennai', 'quote': 'I wore this to my cousin\'s wedding and I genuinely lost count of how many people asked me where I got it from. I felt like a queen the entire night — and I wasn\'t even the bride.', 'stars': 5},
        {'name': 'Priya N., Hyderabad', 'quote': 'The quality is stunning. The gold work on the dupatta looks so rich in person — way better than the photos. I\'ve worn it twice already and it still looks brand new.', 'stars': 5},
        {'name': 'Ananya S., Bangalore', 'quote': 'My mother cried when she saw me in this. That\'s the only review that matters.', 'stars': 5},
        {'name': 'Deepika M., Mumbai', 'quote': 'I\'ve never felt more confident in an outfit. The fit, the color, the way it moves — everything is perfect. Worth every rupee and more.', 'stars': 5}
    ],
    'urgency': 'This Is A Limited Collection. Handcrafted pieces like this aren\'t mass-produced. Only a select number of pieces are available in this colorway. Once they\'re gone, this exact combination will not be restocked.',
    'rating': 5.0,
    'reviewsCount': 560
}

# Append the new style products
products.extend([p1, p2, p3])

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print('Added 3 style products successfully')
