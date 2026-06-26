import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

space_products = [
    {
        'name': 'LED Gooseneck Desk Lamp with Organiser',
        'price': 1299,
        'category': 'space',
        'mainImage': '/assets/images/products/space/1.jpg',
        'tagline': 'One lamp. Three light moods. A complete transformation in how your space feels.',
        'hook': {
            'headline': 'Your Space Deserves to Look Like It Was Designed on Purpose.',
            'problem': "A bare overhead light that flattens everything it touches. A desk that looks functional but never beautiful. Pens scattered in a mug you've been meaning to replace since last year. Guests come over and your study gets a polite glance — not a second look. You've spent money on your wardrobe. On your phone. But the space where you spend hours every day still looks unfinished.",
            'solution': "Close your eyes and picture this. It's 9pm. Your workspace is calm. A warm, amber glow curves softly over your desk — not harsh, not cold, but exactly right. Your pens stand neatly in the base. The whole corner of the room looks curated, considered, and completely yours. Your desk isn't just a desk anymore. It's a space that reflects who you are."
        },
        'benefits': [
            {'title': 'Three Light Moods', 'desc': 'Warm for evenings. Cool for focus. Neutral for everything between. Three genuine moods, each dialled in for how you actually live.', 'icon': '💡'},
            {'title': 'Integrated Organiser', 'desc': 'Transforms a single object into two. Your desk instantly looks tidier, more curated — without any extra effort.', 'icon': '✏️'},
            {'title': 'Flexible Gooseneck', 'desc': 'Bends to exactly where you need the light, holds its position without drooping. Quiet reliability that lasts for years.', 'icon': '🔄'},
            {'title': 'Touch Controls', 'desc': 'No switches. No cords to fumble with. Just a fingertip — because luxury is simplicity.', 'icon': '✨'}
        ],
        'ingredients': [
            {'name': 'Silicone Gooseneck Neck', 'desc': 'Bends to exactly where you need the light, holds its position without drooping. Quiet reliability that lasts for years, not months.', 'icon': '🔄'},
            {'name': 'Matte White Ceramic Base', 'desc': 'The kind of clean, architectural finish that makes inexpensive things look expensive and premium things look exceptional.', 'icon': '🏺'},
            {'name': 'Warm / Neutral / Cool Modes', 'desc': 'Three genuine moods, each one dialled in for how you actually live — rest, work, and everything between.', 'icon': '💡'},
            {'name': 'USB Rechargeable', 'desc': 'Plug into any USB port. No proprietary chargers. Works everywhere your life takes you.', 'icon': '🔌'}
        ],
        'howToUse': [
            {'step': 'Place', 'desc': 'Position the lamp on your desk, bedside table, or study shelf.'},
            {'step': 'Organise', 'desc': 'Place your pens, markers and stationery in the integrated base organiser.'},
            {'step': 'Set Your Mood', 'desc': 'Tap the touch control to cycle through Warm, Neutral, or Cool light modes.'}
        ],
        'reviews': [
            {'name': 'Sneha A., Pune', 'quote': 'I moved this to three different spots in my apartment because every corner looked better with it. My clients on video calls keep commenting on how "put-together" my background looks.', 'stars': 5},
            {'name': 'Rahul M., Bengaluru', 'quote': "I didn't expect a lamp to change how I feel about my workspace. But I genuinely look forward to sitting at my desk now. The warm light in the evening is something else.", 'stars': 5},
            {'name': 'Priya K., Mumbai', 'quote': "Bought this for my sister's new flat. She called me the same day it arrived to say it was the most thoughtful gift she'd ever received.", 'stars': 5}
        ],
        'riskReversal': ['Free Delivery', 'Gift-Ready Packaging', 'Limited Stock Available'],
        'urgency': 'Limited Stock Available — The desk corner you walk past every day deserves to make you feel something.',
        'rating': 4.8,
        'reviewsCount': 2100
    },
    {
        'name': 'White & Gold Deer Figurine Set',
        'price': 899,
        'category': 'space',
        'mainImage': '/assets/images/products/space/2.jpg',
        'tagline': 'One set. Two sculptures. A room that never looks the same again.',
        'hook': {
            'headline': 'Some spaces are lived in. Others are admired. Yours deserves to be both.',
            'problem': "Your furniture is good. Your walls are painted. But something is still missing. The room feels flat. Generic. Like it could belong to anyone. Guests walk in and it doesn't make them pause. You've scrolled through Pinterest boards wondering why your space doesn't look like that. The answer isn't a renovation.",
            'solution': "Late evening. Warm light fills the room. On your console or shelf — two sculpted deer, white as porcelain, antlers gleaming in brushed gold. The space feels still. Intentional. Quietly luxurious. Your home no longer looks decorated. It looks designed."
        },
        'benefits': [
            {'title': 'The Room Gets a Soul', 'desc': 'Decorative sculptures signal taste, intention, and personality that furniture alone can never communicate.', 'icon': '✨'},
            {'title': 'Guests Notice Immediately', 'desc': 'And they ask about it. Every single time.', 'icon': '👀'},
            {'title': 'Curated, Not Just Furnished', 'desc': 'The difference between a house and a home that means something.', 'icon': '🏡'},
            {'title': 'Elevates Everything Around It', 'desc': 'Walls look warmer, furniture looks more expensive, the whole room levels up.', 'icon': '⬆️'}
        ],
        'ingredients': [
            {'name': 'Premium Resin Construction', 'desc': 'Gives each sculpture the weight and solidity of fine art, not the hollowness of mass-produced décor.', 'icon': '🏺'},
            {'name': 'Hand-Applied Gold Finish', 'desc': 'Carefully applied to create that rich, gallery-worthy contrast against the matte white body.', 'icon': '✨'},
            {'name': 'Textured Saddle Detailing', 'desc': 'Subtle woven-effect accents break the surface beautifully, adding dimension that catches light at every angle.', 'icon': '🦌'},
            {'name': 'Wooden Display Base', 'desc': 'Grounds the set in warmth, creating a complete vignette straight out of the box. No styling needed.', 'icon': '🪵'}
        ],
        'howToUse': [
            {'step': 'Unbox', 'desc': 'Each sculpture arrives protected. No assembly required.'},
            {'step': 'Place', 'desc': 'Set on your console, shelf, dresser or coffee table.'},
            {'step': 'Admire', 'desc': 'Watch your room transform. Watch your guests react.'}
        ],
        'reviews': [
            {'name': 'Rhea S., Mumbai', 'quote': 'Every person who visits my apartment asks about these. I have sent the link to four different people already.', 'stars': 5},
            {'name': 'Aditya K., Bangalore', 'quote': "I kept feeling like my living room was missing something for months. The moment I placed these on my console, I stopped feeling that way.", 'stars': 5},
            {'name': 'Sneha M., Delhi', 'quote': 'These look like they are from a high-end interior store. The gold detailing is stunning in person. Absolutely worth it.', 'stars': 5},
            {'name': 'Priya T., Hyderabad', 'quote': 'Gifted this for a housewarming. The reaction was priceless. They thought I spent a fortune.', 'stars': 5}
        ],
        'riskReversal': ['Premium Resin Build', 'Hand-Applied Gold Finish', 'Gift-Ready Packaging'],
        'urgency': 'Limited home décor pieces like this move fast. When you see a piece that speaks to you, you do not wait.',
        'rating': 4.9,
        'reviewsCount': 870
    },
    {
        'name': 'White & Gold Ceramic Vase Collection',
        'price': 1099,
        'category': 'space',
        'mainImage': '/assets/images/products/space/3.jpg',
        'tagline': 'Three vases. One collection. A room that finally feels like it belongs in a magazine.',
        'hook': {
            'headline': 'Luxury is not bought in one piece. It is built — one beautiful detail at a time.',
            'problem': "Surfaces that are technically decorated — but don't feel finished. A bedroom that's comfortable but not inspiring. You've bought candles, throws, frames. But the space still doesn't have that look. That cohesive, intentional, effortlessly elegant look that you see in interiors you admire. The missing piece is almost always one right object in one right place.",
            'solution': "Morning light filters through the curtains. On your dresser or bedside table — three white ceramic vases, graduated in size, each banded with delicate gold. Soft pampas grass spills from the tallest one, catching the light. The room feels unhurried. Elevated. Like a boutique hotel — except it's your home."
        },
        'benefits': [
            {'title': 'Instant Vignette', 'desc': 'The trio format is a designer\'s secret. Three objects, varied in height, create visual rhythm that a single piece never can.', 'icon': '🎨'},
            {'title': 'Gold Elevates Everything', 'desc': 'The warm metallic accent adds a richness that transforms ordinary surfaces into styled moments.', 'icon': '✨'},
            {'title': 'No Maintenance', 'desc': 'Dried botanicals included — permanent beauty with zero upkeep. The organic texture of pampas grass against clean ceramic is timeless.', 'icon': '🌾'},
            {'title': 'Photographs Beautifully', 'desc': 'Your space starts looking like the life you actually want to be living.', 'icon': '📸'}
        ],
        'ingredients': [
            {'name': 'Hand-Finished Ceramic Body', 'desc': 'The matte white finish has depth and texture that cheap alternatives can\'t replicate. Substantial. Premium. Considered.', 'icon': '🏺'},
            {'name': 'Precision Gold Banding', 'desc': 'Applied with clean lines that don\'t smudge or blur. The kind of detail that separates artisanal craft from mass production.', 'icon': '✨'},
            {'name': 'Graduated Sizing', 'desc': 'Small, medium, and large heights create a layered composition straight out of the box. No arrangement skills required.', 'icon': '📐'},
            {'name': 'Curated Pampas Grass', 'desc': 'Soft, neutral, and proportioned to complement each vase size. Everything arrives styled.', 'icon': '🌾'}
        ],
        'howToUse': [
            {'step': 'Unbox', 'desc': 'Three vases and curated pampas grass included — ready to display immediately.'},
            {'step': 'Arrange', 'desc': 'Place from tallest to shortest on any surface — dresser, console, shelf, or table.'},
            {'step': 'Style', 'desc': 'Insert the included pampas grass. Your space is instantly transformed.'}
        ],
        'reviews': [
            {'name': 'Ananya R., Bangalore', 'quote': 'My bedroom looks like a Pinterest board now. I genuinely did not believe three vases could change a room this much until I saw it for myself.', 'stars': 5},
            {'name': 'Kavya M., Mumbai', 'quote': 'The gold detailing is so refined. My guests assumed I ordered these from a luxury home store abroad. I smiled and said nothing.', 'stars': 5},
            {'name': 'Ishita D., Delhi', 'quote': 'I bought these for my dresser and ended up buying a second set for my living room. That is how good they look in person.', 'stars': 5},
            {'name': 'Meera S., Hyderabad', 'quote': 'Finally found vases that look expensive and do not cost a fortune. The pampas grass included makes it a complete, ready-to-display set.', 'stars': 5}
        ],
        'riskReversal': ['Premium Ceramic Construction', 'Pampas Grass Included', 'Limited Quantities'],
        'urgency': 'This exact collection is available in limited quantities. When this batch is gone, it\'s gone.',
        'rating': 4.9,
        'reviewsCount': 1340
    }
]

products.extend(space_products)

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f'Added {len(space_products)} space products. Total now: {len(products)}')
