import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

pet_products = [
    {
        'name': 'Snuggle Pig Plush Squeaky Toy',
        'price': 349,
        'category': 'pet',
        'mainImage': '/assets/images/products/pet/1.jpg',
        'tagline': 'Soft enough to cuddle. Durable enough to survive. Squeaky enough to keep them obsessed.',
        'hook': {
            'headline': "They Can't Tell You What Makes Them Happy. But Their Tail Does.",
            'problem': "The restless pacing when you leave for work. The chewed-up corner of the sofa. The way they look at you with those eyes when they're bored or anxious. Most toys last three days before they're shredded into a pile of plastic and regret. You've wasted money on toys that weren't worth it. Your dog deserved better.",
            'solution': "The Snuggle Pig isn't just a toy — it's a companion for every nap, every play session, and every moment you can't be right beside them. It gives anxious dogs something safe to hold onto. It gives playful dogs a worthy opponent. Watch them pick it up the moment it arrives. Watch them refuse to put it down."
        },
        'benefits': [
            {'title': 'Reduces Anxiety', 'desc': 'The soft, huggable shape gives dogs something comforting to hold — especially when alone. Less whining. Less destruction. More calm.', 'icon': '🧸'},
            {'title': 'Mentally Stimulating', 'desc': 'The squeaker triggers natural play instincts — fetch, shake, pounce. An occupied dog is a happy dog.', 'icon': '🎯'},
            {'title': 'Gentle on Teeth', 'desc': 'Plush material is soft enough for puppies and senior dogs alike. No hard edges. Just safe, joyful play.', 'icon': '🦷'},
            {'title': 'Built to Last', 'desc': 'Double-stitched seams mean this toy survives the kind of play most toys don\'t. Weeks of use, not days.', 'icon': '💪'}
        ],
        'ingredients': [
            {'name': 'Ultra-Soft Plush Fabric', 'desc': 'Gentle on sensitive gums, soft against their nose and paws — the kind of texture dogs instinctively nuzzle and carry like a security blanket.', 'icon': '🧶'},
            {'name': 'Non-Toxic Stuffing', 'desc': 'No harmful chemicals. No sharp interiors. Just clean, safe filling that stays soft and forgiving — even after the hundredth squeeze.', 'icon': '🌿'},
            {'name': 'Reinforced Double Stitching', 'desc': 'Built to handle shaking, tossing, tugging, and everything in between. Because dogs are enthusiastic.', 'icon': '✂️'},
            {'name': 'Embedded Squeaker', 'desc': 'The satisfying squeak that activates your dog\'s natural instinct to play — keeping them mentally stimulated and genuinely entertained.', 'icon': '🔊'}
        ],
        'howToUse': [
            {'step': 'Unbox Together', 'desc': 'Let your dog sniff it first. Dogs explore with their nose — this is them saying hello.'},
            {'step': 'Activate the Squeak', 'desc': 'Give it one squeeze in front of them. Watch their ears perk up. That\'s the moment it becomes theirs.'},
            {'step': 'Play Together First', 'desc': 'Toss it gently. Let them fetch, shake, and carry it. The first few minutes of play together will make this their favourite toy for months.'},
            {'step': 'Leave It With Them', 'desc': 'Leave it in their bed or favourite resting spot. They\'ll find it. They always do.'}
        ],
        'reviews': [
            {'name': 'Meera D., Mumbai', 'quote': 'My golden retriever has been carrying this pig everywhere for 3 weeks. It has survived more play than any toy we\'ve bought. Absolutely worth it.', 'stars': 5},
            {'name': 'Arjun S., Delhi', 'quote': 'I bought this for my anxious rescue dog. Within an hour she had claimed it as her own. She sleeps with it now. The peace of mind this gives me is priceless.', 'stars': 5},
            {'name': 'Priya R., Bangalore', 'quote': 'My dog is a power chewer and this has held up remarkably well. The squeaker still works after weeks of play. Genuinely impressed.', 'stars': 5}
        ],
        'riskReversal': ['Non-Toxic Pet-Safe Materials', 'No Loose Parts or Choking Hazards', '30-Day Happiness Guarantee'],
        'urgency': 'Free Delivery · Gift-Wrapping Available · 30-Day Happiness Guarantee. Because the wag of a tail is worth everything.',
        'rating': 4.9,
        'reviewsCount': 3400
    },
    {
        'name': 'Plush Pig Squeaky Dog Toy',
        'price': 299,
        'category': 'pet',
        'mainImage': '/assets/images/products/pet/2.jpg',
        'tagline': 'Your dog\'s companion for the quiet hours.',
        'hook': {
            'headline': 'Because the way your dog looks at their favourite toy is one of the purest things in the world.',
            'problem': "You leave for work. Your dog is alone. No one to play with. No one to cuddle. You come home to chewed furniture, restless energy, or a dog that just seems sad. Or maybe you've bought toys before — only to watch them fall apart in twenty minutes. Stuffing everywhere. Squeaker gone. Another trip to the bin.",
            'solution': "Watch your dog carry this little pig everywhere. To their bed. To greet you at the door. To show off to every guest. The squeaky sound triggers their natural play instinct — keeping them mentally engaged, physically active, and emotionally content even when you can't be right beside them."
        },
        'benefits': [
            {'title': 'Relieves Loneliness', 'desc': 'Gives them a comfort object they bond with, especially during hours alone. Less anxiety, more calm.', 'icon': '🧸'},
            {'title': 'Stimulates Play', 'desc': 'The squeaker activates their instinct to interact, keeping boredom and destructive behaviour away.', 'icon': '🎯'},
            {'title': 'Gentle on Mouths', 'desc': 'Soft plush is kind on mouths, especially for puppies still developing their bite.', 'icon': '🦷'},
            {'title': 'Versatile Play', 'desc': 'Fetch, tug, cuddle — versatile enough for every kind of play your dog loves.', 'icon': '🐾'}
        ],
        'ingredients': [
            {'name': 'Ultra-Soft Plush Exterior', 'desc': 'Gentle on gums, safe for enthusiastic chewers who love to mouth and carry their toys everywhere.', 'icon': '🧶'},
            {'name': 'Non-Toxic Pet-Safe Materials', 'desc': 'No harmful dyes, no sharp edges, no parts that compromise safety during play.', 'icon': '🌿'},
            {'name': 'Securely Stitched Seams', 'desc': 'Reinforced construction that holds up to shaking, tossing, and enthusiastic play.', 'icon': '✂️'},
            {'name': 'Compact Huggable Shape', 'desc': 'Sized perfectly for small to medium breeds to carry, cuddle, and play with comfortably.', 'icon': '🐷'}
        ],
        'howToUse': [
            {'step': 'Introduce', 'desc': 'Let your dog sniff the toy first. Let them come to it naturally.'},
            {'step': 'Activate', 'desc': 'Squeak it gently to activate their curiosity and play instinct.'},
            {'step': 'Play', 'desc': 'Toss it lightly or encourage a gentle game of fetch to build the bond with the toy.'},
            {'step': 'Bond', 'desc': 'Let them carry it, cuddle it, squeak it — on their terms.'}
        ],
        'reviews': [
            {'name': 'Sneha T., Pune', 'quote': 'This little pig has become my dog\'s most treasured possession. She brings it to greet every visitor. It\'s been two months and it\'s still in perfect condition.', 'stars': 5},
            {'name': 'Rohan K., Hyderabad', 'quote': 'I was sceptical after going through so many toys. This one is genuinely different. My puppy is obsessed and I haven\'t had to worry about safety at all.', 'stars': 5},
            {'name': 'Fatima N., Chennai', 'quote': 'The quality is so much better than expected at this price. Soft, safe, and my dog absolutely loves it. Will be buying more as gifts.', 'stars': 5}
        ],
        'riskReversal': ['Non-Toxic Pet-Safe Build', 'Reinforced Stitching', 'Suitable for Puppies and Adults'],
        'urgency': 'Your dog doesn\'t need much. A warm place. Food. You. And one toy they love more than anything else.',
        'rating': 4.8,
        'reviewsCount': 2800
    },
    {
        'name': 'Paw Kare Soft Cleansing Pet Wipes',
        'price': 399,
        'category': 'pet',
        'mainImage': '/assets/images/products/pet/3.jpg',
        'tagline': 'Clean, comfortable, and cared for — every single day.',
        'hook': {
            'headline': 'Your pet trusts you completely. The least they deserve is the gentlest touch.',
            'problem': "After a walk, their paws carry everything from the outside world in — bacteria, dust, allergens. Between baths, their coat picks up odour and germs silently. You want to help — but you're not always sure what's safe near their eyes or on their sensitive skin. The wrong wipe can sting, dry out, or irritate. Your pet can't tell you it hurts. But you can see it.",
            'solution': "Paw Kare wipes make daily hygiene gentle, fast, and completely safe. After every walk, every meal, every muddy moment — a soft, single wipe and your pet is clean, fresh, and comfortable. No stress. No bath-time battle. No guilt about what's on the wipe. Just quick, caring cleanliness that fits into your daily routine effortlessly."
        },
        'benefits': [
            {'title': 'Removes Bacteria', 'desc': 'Removes bacteria, allergens, and outdoor contaminants — from paws to coat, after every walk.', 'icon': '🛡️'},
            {'title': 'Soothes Sensitive Skin', 'desc': 'The Aloe and Jojoba combination calms redness and dryness without any harsh reaction.', 'icon': '🌿'},
            {'title': 'Safe for Face & Eyes', 'desc': 'Specifically formulated to be safe near the face, around the eyes, and on sensitive areas.', 'icon': '👁️'},
            {'title': 'Daily Use Safe', 'desc': 'No dryness, no stripping of natural oils, no skin barrier damage even with regular use.', 'icon': '♻️'}
        ],
        'ingredients': [
            {'name': 'Aloe Vera', 'desc': 'Nature\'s most trusted skin soother. Calms irritation, hydrates without greasiness, and leaves skin and coat feeling soft after every wipe.', 'icon': '🌿'},
            {'name': 'Jojoba Oil', 'desc': 'Closely mirrors your pet\'s natural skin oils, making it deeply moisturising without clogging pores or causing sensitivity.', 'icon': '💧'},
            {'name': 'Vitamin E', 'desc': 'A powerful antioxidant that protects skin from environmental damage and supports long-term skin health. Gentle enough for daily use.', 'icon': '✨'},
            {'name': 'Antibacterial Formula', 'desc': 'Actively helps remove disease-causing bacteria from paws, fur, and skin — the invisible threat after every outdoor exposure.', 'icon': '🔬'}
        ],
        'howToUse': [
            {'step': 'Pull One Wipe', 'desc': 'Pull one wipe gently from the resealable pack.'},
            {'step': 'Clean Paws First', 'desc': 'Start with paws after outdoor walks — wipe thoroughly between toe pads and around the paw.'},
            {'step': 'Wipe the Coat', 'desc': 'Wipe down the coat, underbelly, and any areas that came into contact with outdoor surfaces.'},
            {'step': 'Clean the Face', 'desc': 'Use a fresh wipe around eyes and muzzle in a soft outward motion. Reseal pack when done.'}
        ],
        'reviews': [
            {'name': 'Kavitha M., Bangalore', 'quote': 'These wipes have made our daily post-walk routine so much easier. My dog doesn\'t resist at all — they\'re so gentle. The aloe smell is subtle and lovely.', 'stars': 5},
            {'name': 'Deepak R., Mumbai', 'quote': 'My vet recommended these specifically for my dog\'s sensitive skin. Two months in and his coat looks healthier than ever. Absolutely will repurchase.', 'stars': 5},
            {'name': 'Anita S., Delhi', 'quote': 'I use these on my cat too — she tolerates them better than anything else I\'ve tried. The face-safe formula is a game changer for cleaning around her eyes.', 'stars': 5}
        ],
        'riskReversal': ['Vet Recommended Formula', 'Non-Irritant to Eyes', 'Free from Harsh Alcohol'],
        'urgency': '80 wipes per pack — generous, resealable, and ready when you need them. Free Delivery on orders above ₹499.',
        'rating': 4.9,
        'reviewsCount': 1650
    }
]

products.extend(pet_products)

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f'Added {len(pet_products)} pet products. Total now: {len(products)}')
