file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '\nfunction renderPetProduct'
end_marker = '\n// ======================\n// 🧱 DEFAULT RENDERER'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

print(f"Start: {start_idx}, End: {end_idx}, Block: {end_idx - start_idx} chars")

new_block = '''
function renderPetProduct(product, container) {
  const name = product.name || "Nurture Pet Wellness Kit";
  const price = Number(product.price) || 0;
  const image = getImageUrl(product.mainImage || product.image);
  const tagline = product.tagline || "Because your companion deserves nothing less than perfection.";

  const hook = product.hook || {
    headline: "They Can't Tell You What Makes Them Happy. But Their Tail Does.",
    problem: "The restless pacing when you leave. The chewed-up sofa. Most toys last three days. You've wasted money on toys that weren't worth it.",
    solution: "A companion for every nap, every play session, and every moment you can't be right beside them."
  };

  const benefits = product.benefits || [
    {icon:'🧸', title:'Reduces Anxiety', desc:'Gives dogs something comforting to hold when alone.'},
    {icon:'🎯', title:'Mentally Stimulating', desc:'Keeps them engaged and prevents destructive behaviour.'},
    {icon:'🦷', title:'Gentle on Teeth', desc:'Safe for puppies and senior dogs alike.'},
    {icon:'💪', title:'Built to Last', desc:'Double-stitched seams survive serious play.'}
  ];

  const ingredients = product.ingredients || [
    {icon:'🧶', name:'Ultra-Soft Plush', desc:'Gentle on gums, soft against their nose and paws.'},
    {icon:'🌿', name:'Non-Toxic Stuffing', desc:'No harmful chemicals. Clean, safe filling.'},
    {icon:'✂️', name:'Reinforced Stitching', desc:'Built to handle shaking, tossing, and tugging.'},
    {icon:'🔊', name:'Embedded Squeaker', desc:'Activates natural play instincts and keeps them entertained.'}
  ];

  const howToUse = product.howToUse || [
    {step:'Introduce', desc:'Let your pet sniff it first. Let them come to it naturally.'},
    {step:'Activate', desc:'Squeak it gently to trigger their curiosity and play instinct.'},
    {step:'Play', desc:'Toss it lightly to build the bond with the toy.'},
    {step:'Bond', desc:'Let them carry it, cuddle it — on their terms.'}
  ];

  const reviews = product.reviews || [
    {name:'Meera D.', quote:"My dog has been carrying this everywhere for 3 weeks. Absolutely worth it.", stars:5},
    {name:'Arjun S.', quote:"My anxious rescue dog claimed this as her own within an hour. She sleeps with it now.", stars:5},
    {name:'Priya R.', quote:"My power chewer and this has held up remarkably well. Genuinely impressed.", stars:5}
  ];

  const riskReversal = product.riskReversal || ['Non-Toxic Pet-Safe Materials', 'No Choking Hazards', '30-Day Happiness Guarantee'];
  const urgency = product.urgency || 'Free Delivery · Gift-Wrapping Available · 30-Day Happiness Guarantee';

  const benefitsHTML = benefits.map(b =>
    '<div style="background:#fff;padding:35px 25px;border-radius:16px;text-align:center;border:1px solid #FDEAEA;transition:box-shadow 0.3s;" onmouseover="this.style.boxShadow=\'0 15px 40px rgba(0,0,0,0.05)\'" onmouseout="this.style.boxShadow=\'none\'">' +
    '<div style="font-size:2rem;margin-bottom:14px;">' + b.icon + '</div>' +
    '<h4 style="font-size:1.05rem;font-weight:700;margin-bottom:10px;color:#3D2B2B;">' + b.title + '</h4>' +
    '<p style="font-size:0.88rem;color:#7A5A5A;line-height:1.7;">' + b.desc + '</p>' +
    '</div>'
  ).join('');

  const ingredientsHTML = ingredients.map(ing =>
    '<div style="background:#FFF5F5;padding:30px;border-radius:12px;display:flex;gap:18px;align-items:flex-start;">' +
    '<div style="width:56px;height:56px;background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.5rem;flex-shrink:0;border:1px solid #FDEAEA;">' + ing.icon + '</div>' +
    '<div><h4 style="font-size:1.05rem;font-weight:700;margin-bottom:8px;color:#3D2B2B;">' + ing.name + '</h4>' +
    '<p style="font-size:0.88rem;color:#7A5A5A;line-height:1.7;">' + ing.desc + '</p></div>' +
    '</div>'
  ).join('');

  const stepsHTML = howToUse.map(function(s, i) {
    return '<div style="text-align:center;">' +
    '<div style="font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;color:#E8847A;margin-bottom:12px;font-weight:700;">STEP 0' + (i+1) + '</div>' +
    '<h4 style="font-size:1.15rem;font-weight:700;margin-bottom:10px;color:#3D2B2B;">' + s.step + '</h4>' +
    '<p style="font-size:0.88rem;color:#7A5A5A;line-height:1.7;">' + s.desc + '</p>' +
    '</div>';
  }).join('');

  const reviewsHTML = reviews.map(r =>
    '<div class="reveal-box" style="background:#fff;padding:45px 35px;border-radius:20px;border:1px solid #FDEAEA;transition:transform 0.3s;" onmouseover="this.style.transform=\'translateY(-5px)\'" onmouseout="this.style.transform=\'translateY(0)\'">' +
    '<div style="font-size:1.1rem;color:#E8847A;letter-spacing:3px;margin-bottom:18px;">' + '★'.repeat(r.stars) + '</div>' +
    '<p style="font-style:italic;font-size:1.05rem;color:#4A3A3A;line-height:1.8;margin-bottom:20px;">"' + r.quote + '"</p>' +
    '<div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;color:#7A5A5A;font-weight:600;">— ' + r.name + '</div>' +
    '</div>'
  ).join('');

  const riskHTML = riskReversal.map(r =>
    '<div style="display:flex;align-items:center;gap:10px;"><span style="color:#E8847A;font-size:1rem;">✔</span><span style="font-size:0.85rem;color:#4A3A3A;font-weight:500;">' + r + '</span></div>'
  ).join('');

  const numBenefits = benefits.length;
  const numIngredients = ingredients.length;
  const numSteps = howToUse.length;
  const numReviews = reviews.length;

  container.innerHTML = `
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <div style="font-family:'Inter',sans-serif;color:#3D2B2B;background:transparent;overflow-x:hidden;">

      <!-- 1. HERO -->
      <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:0;min-height:88vh;margin-bottom:80px;">
        <div style="background:#FFF5F5;display:flex;align-items:center;justify-content:center;padding:60px;overflow:hidden;">
          <img src="${image}" alt="${name}"
            style="max-width:100%;max-height:600px;object-fit:contain;transition:transform 0.8s ease;"
            onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"
            onerror="this.src='./assets/images/placeholder.jpg'">
        </div>
        <div style="background:#fff;display:flex;flex-direction:column;justify-content:center;padding:70px 55px;">
          <div style="font-size:0.7rem;letter-spacing:4px;text-transform:uppercase;color:#E8847A;margin-bottom:18px;">🐾 Pet Collection</div>
          <h1 style="font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:500;line-height:1.2;margin:0 0 18px;color:#3D2B2B;">${name}</h1>
          <p style="font-size:1.05rem;color:#7A5A5A;margin-bottom:28px;line-height:1.7;font-style:italic;">"${tagline}"</p>
          <div style="font-family:'Playfair Display',serif;font-size:2.4rem;font-weight:400;margin-bottom:30px;color:#3D2B2B;">&#8377;${price.toLocaleString('en-IN')}</div>
          <div style="margin-bottom:28px;padding:18px;background:#FFF5F5;border-radius:8px;border-left:3px solid #E8847A;display:flex;flex-direction:column;gap:10px;">
            ${riskHTML}
          </div>
          <div style="display:flex;flex-direction:column;gap:12px;">
            <button class="buy-btn"
              style="width:100%;padding:20px;background:#3D2B2B;color:#fff;border:none;cursor:pointer;font-size:0.85rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;transition:background 0.3s;border-radius:50px;"
              onmouseover="this.style.background='#E8847A'" onmouseout="this.style.background='#3D2B2B'"
              data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
              🐾 Add to Cart
            </button>
            <button id="buy-now"
              style="width:100%;padding:20px;background:transparent;color:#3D2B2B;border:2px solid #3D2B2B;cursor:pointer;font-size:0.85rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;transition:all 0.3s;border-radius:50px;"
              onmouseover="this.style.background='#FFF5F5'" onmouseout="this.style.background='transparent'">
              Buy Now
            </button>
          </div>
          <div style="margin-top:18px;font-size:0.85rem;color:#E8847A;font-weight:600;line-height:1.5;">${urgency}</div>
        </div>
      </div>

      <!-- 2. HOOK -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:80px 60px;background:#3D2B2B;border-radius:20px;text-align:center;">
        <div style="color:#E8847A;font-size:1.4rem;letter-spacing:5px;margin-bottom:25px;">🐾  🐾  🐾</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3rem);font-weight:400;color:#fff;line-height:1.3;margin-bottom:30px;">${hook.headline}</h2>
        <p style="font-size:1.05rem;color:#B8998A;line-height:1.9;margin-bottom:25px;max-width:750px;margin-left:auto;margin-right:auto;">${hook.problem}</p>
        <div style="width:40px;height:2px;background:#E8847A;margin:30px auto;border-radius:2px;"></div>
        <p style="font-size:1.1rem;color:#fff;line-height:1.9;font-style:italic;max-width:700px;margin:0 auto;">${hook.solution}</p>
      </div>

      <!-- 3. BENEFITS -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:0 40px;">
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);text-align:center;margin-bottom:50px;font-weight:500;color:#3D2B2B;">What This Does For Your Pet, Every Day</h2>
        <div style="display:grid;grid-template-columns:repeat(${numBenefits},1fr);gap:20px;">
          ${benefitsHTML}
        </div>
      </div>

      <!-- 4. INGREDIENTS / MATERIALS -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:0 40px;">
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);text-align:center;margin-bottom:50px;font-weight:500;color:#3D2B2B;">Made With Your Pet's Safety First</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
          ${ingredientsHTML}
        </div>
      </div>

      <!-- 5. HOW TO USE -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:80px 60px;background:#FFF5F5;border-radius:20px;">
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);text-align:center;margin-bottom:60px;font-weight:500;color:#3D2B2B;">Simple Steps to Happy Pet</h2>
        <div style="display:grid;grid-template-columns:repeat(${numSteps},1fr);gap:40px;max-width:1000px;margin:0 auto;">
          ${stepsHTML}
        </div>
      </div>

      <!-- 6. REVIEWS -->
      <div style="max-width:1200px;margin:0 auto 80px;padding:0 40px;">
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);text-align:center;margin-bottom:50px;font-weight:500;color:#3D2B2B;">From Pet Parents Who Know</h2>
        <div style="display:grid;grid-template-columns:repeat(${numReviews},1fr);gap:25px;">
          ${reviewsHTML}
        </div>
      </div>

      <!-- 7. FINAL CTA -->
      <div class="reveal-box premium-cta-box" style="max-width:1200px;margin:0 auto;background:#3D2B2B;color:#fff;border-radius:20px;">
        <div style="color:#E8847A;font-size:1.5rem;margin-bottom:20px;">🐾</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;margin-bottom:20px;">They give you everything. Give them this.</h2>
        <p style="color:#B8998A;margin-bottom:35px;font-size:1.05rem;line-height:1.7;">Every day they show up for you without being asked. This is one small, beautiful way to give it back.</p>
        <button class="buy-btn"
          style="background:#E8847A;color:#fff;border:none;padding:20px 50px;border-radius:50px;font-size:1rem;font-weight:700;cursor:pointer;letter-spacing:1px;transition:all 0.3s;"
          onmouseover="this.style.background='#d4726a'" onmouseout="this.style.background='#E8847A'"
          data-id="${product._id}" data-name="${name}" data-price="${price}" data-img="${image}">
          🐾 Give Your Pet the Joy They Deserve — &#8377;${price.toLocaleString('en-IN')}
        </button>
      </div>

    </div>
  `;

  setupProductButtons(product, name, price, image);
}
'''

before = content[:start_idx]
after = content[end_idx:]
new_content = before + new_block + after

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully patched renderPetProduct!")
