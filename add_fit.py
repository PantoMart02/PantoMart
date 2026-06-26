import json

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Product 1: Boldfit Wrist Wraps
p1 = {
    'name': 'Boldfit Wrist Wraps',
    'price': 499,
    'category': 'fit',
    'mainImage': '/assets/images/products/fit/2.jpg',
    'tagline': 'Engineered for the athlete who doesn\'t make excuses.',
    'hook': {
        'headline': 'Your wrists are giving up before your muscles do.',
        'problem': 'You\'re mid-set. Weight is loaded. You\'re mentally locked in. Then your wrists buckle. The pain hits. You rack the bar early. Another rep lost. Another session cut short. You\'re not weak. You\'re unsupported.',
        'solution': 'You load the bar heavier than you ever have. Your grip is iron. Your wrists don\'t flinch. You push through your last rep — then do two more. That\'s what proper wrist support feels like.'
    },
    'benefits': [
        {'title': 'Zero Collapse', 'desc': 'Wraps lock the joint so wrists never bend or give out mid-lift.', 'icon': '🔒'},
        {'title': 'Reduce Fatigue', 'desc': 'Compression reduces strain and pain after heavy sessions.', 'icon': '⚡'},
        {'title': 'More Gains', 'desc': 'Supported wrists equal more load and heavier weights.', 'icon': '📈'},
        {'title': 'Secure Hold', 'desc': 'Velcro hold that stays put, set after set. No slipping.', 'icon': '🛡️'}
    ],
    'features': [
        {'title': 'Heavy-Duty Elastic', 'desc': 'Built to hold under serious load, session after session. Not cheap fabric.', 'icon': '💪'},
        {'title': 'Thumb Anchor System', 'desc': 'Wraps stay exactly where you place them. No sliding or distractions.', 'icon': '🎯'},
        {'title': 'Dual Reinforcement', 'desc': 'Targeted stiffness exactly where your wrist needs it most.', 'icon': '⚙️'}
    ],
    'howToUse': [
        {'step': '01', 'title': 'Anchor', 'desc': 'Loop over thumb to secure position.'},
        {'step': '02', 'title': 'Wrap', 'desc': 'Pull tight around wrist joint for compression.'},
        {'step': '03', 'title': 'Lock', 'desc': 'Secure velcro. Unshackle your true strength.'}
    ],
    'reviews': [
        {'name': 'Marcus T.', 'title': 'Powerlifter', 'q': 'Nothing else comes close. The grip alone changed how I lift. My PRs have gone up three weeks straight.'},
        {'name': 'Priya A.', 'title': 'CrossFit Athlete', 'q': 'Finally equipment that disappears during training. No adjustments, no distraction. Pure performance.'},
        {'name': 'Rahul S.', 'title': 'Gym Goer', 'q': 'Built for real workouts. Not just the aesthetic. Train with confidence.'}
    ],
    'urgency': 'Boldfit Wrist Wraps are what serious athletes reach for. Stop leaving reps behind.',
    'rating': 4.8,
    'reviewsCount': 1500
}

# Product 2: Carbamide Forte Cyclone Shaker
p2 = {
    'name': 'Carbamide Forte Cyclone Shaker',
    'price': 399,
    'category': 'fit',
    'mainImage': '/assets/images/products/fit/3.jpg',
    'tagline': 'This Isn\'t A Bottle. It\'s A Performance Tool.',
    'hook': {
        'headline': 'Your nutrition is premium. Your shaker shouldn\'t be an insult to it.',
        'problem': 'You\'re spending real money on premium supplements — and shaking them in a leaking, clumpy, cheap bottle. Lumps of protein still sitting at the bottom. Lid leaving wet rings. Plastic smell mixing with your shake.',
        'solution': 'Smooth shake. Zero lumps. Ice cold. A bottle that looks as serious as your workout. No leaks on your gym bag. No excuses. Just clean, perfectly mixed nutrition.'
    },
    'benefits': [
        {'title': 'Fully Smooth', 'desc': 'Cyclone Blender creates a vortex for perfect consistency.', 'icon': '🌪️'},
        {'title': '100% Leakproof', 'desc': 'Sealed, secure, confident. No more ruined gym bags.', 'icon': '💧'},
        {'title': 'Clean Nutrition', 'desc': '100% BPA-free build with zero plastic chemicals.', 'icon': '🍃'},
        {'title': 'Built To Be Seen', 'desc': 'Sleek smoked design with bold minimal branding.', 'icon': '✨'}
    ],
    'features': [
        {'title': 'Cyclone Blender', 'desc': 'Internal whirlpool effect mixes powders completely smooth. No lumps.', 'icon': '⚙️'},
        {'title': 'Smoked Transparent Body', 'desc': 'See your fill level at a glance. No guessing. Precision every pour.', 'icon': '👁️'},
        {'title': 'Wide Mouth Design', 'desc': 'Easy to fill, easy to clean, easy to add ice. Effortless basics.', 'icon': '🧊'}
    ],
    'howToUse': [
        {'step': '01', 'title': 'Pour', 'desc': 'Add water or milk first for best mixing.'},
        {'step': '02', 'title': 'Scoop', 'desc': 'Add your premium supplements.'},
        {'step': '03', 'title': 'Shake', 'desc': 'Twist the leakproof lid and shake for a perfect vortex.'}
    ],
    'reviews': [
        {'name': 'Arjun K.', 'title': 'Fitness Trainer', 'q': 'Designed for people who take what they put in their body seriously. No lumps ever.'},
        {'name': 'Neha P.', 'title': 'Nutritionist', 'q': 'The best shaker I have used. Clean, leakproof, and BPA-free.'},
        {'name': 'Vikram R.', 'title': 'Bodybuilder', 'q': 'Makes my routine seamless. No loose blender balls rusting inside.'}
    ],
    'urgency': 'Mix Smarter, Recover Harder. Upgrade your post-workout game today.',
    'rating': 4.9,
    'reviewsCount': 3200
}

# Product 3: Boldfit Speed Jump Rope
p3 = {
    'name': 'Boldfit Speed Jump Rope',
    'price': 299,
    'category': 'fit',
    'mainImage': '/assets/images/products/fit/4.jpg',
    'tagline': 'Engineered for Peak Performance.',
    'hook': {
        'headline': 'You\'re Putting in the Work. So Why Isn\'t Your Body Showing It?',
        'problem': 'You\'re training hard — but somewhere between inconsistency, wasted time, and underwhelming equipment, your progress has flatlined. The problem isn\'t your effort. It\'s what you\'re training with.',
        'solution': 'In 15 Minutes a Day, This Rope Will Reshape Everything. Leaner legs. A stronger core. Sharper endurance. This isn\'t cardio you dread. This is cardio that delivers.'
    },
    'benefits': [
        {'title': 'Intense Sessions', 'desc': 'Speed training keeps your mind sharp and heart rate high.', 'icon': '🔥'},
        {'title': 'Max Return', 'desc': '15 minutes of jump rope matches 30 minutes of jogging.', 'icon': '⏱️'},
        {'title': 'Anywhere Intensity', 'desc': 'Full-body gym-level conditioning, anywhere you stand.', 'icon': '🌍'},
        {'title': 'Unbroken Flow', 'desc': 'Aircraft-grade steel cable built for high-speed, high-rep performance.', 'icon': '⚡'}
    ],
    'features': [
        {'title': 'Adjustable Steel Cable', 'desc': 'Calibrated to your height and rhythm. No awkward jumping.', 'icon': '📏'},
        {'title': 'Ball Bearing Rotation', 'desc': 'Frictionless 360° spin moves with you, not against you.', 'icon': '🔄'},
        {'title': 'Ergonomic Handles', 'desc': 'Engineered non-slip grip that holds firm even mid-sweat.', 'icon': '✊'}
    ],
    'howToUse': [
        {'step': '01', 'title': 'Adjust', 'desc': 'Size the steel cable exactly to your height.'},
        {'step': '02', 'title': 'Grip', 'desc': 'Hold the ergonomic handles firmly.'},
        {'step': '03', 'title': 'Jump', 'desc': '15 minutes a day for total cardiovascular transformation.'}
    ],
    'reviews': [
        {'name': 'Karan M.', 'title': 'Boxer', 'q': 'Built for real results. Smooth rotation and zero drag.'},
        {'name': 'Sneha D.', 'title': 'Home Workout Enthusiast', 'q': 'The only piece of equipment I need. Incredible calorie burn in 15 mins.'},
        {'name': 'Rohit V.', 'title': 'Athlete', 'q': 'Elite performance doesn\'t happen by accident. This rope is precise.'}
    ],
    'urgency': 'Trusted by Over 500,000 Fitness Athletes. Add to Cart for total transformation.',
    'rating': 4.7,
    'reviewsCount': 8500
}

# Append the new fit products
products.extend([p1, p2, p3])

with open('c:/Users/yarra/OneDrive/Desktop/backend/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print('Added 3 fit products successfully')
