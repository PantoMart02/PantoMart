file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and fix the bad reviewsHTML onmouseover in renderPetProduct
bad = """  const reviewsHTML = reviews.map(r =>
    '<div class="reveal-box" style="background:#fff;padding:45px 35px;border-radius:20px;border:1px solid #FDEAEA;transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">' +"""

good = """  const reviewsHTML = reviews.map(r =>
    '<div class="reveal-box" style="background:#fff;padding:45px 35px;border-radius:20px;border:1px solid #FDEAEA;transition:transform 0.3s;" onmouseover="this.style.transform=\\'translateY(-5px)\\'" onmouseout="this.style.transform=\\'translateY(0)\\'">' +"""

if bad in content:
    content = content.replace(bad, good, 1)
    print("Fixed reviewsHTML onmouseover quotes in renderPetProduct")
else:
    # Show what the actual line looks like
    idx = content.find("const reviewsHTML = reviews.map(r =>")
    # Find the one in renderPetProduct (second occurrence)
    idx2 = content.find("const reviewsHTML = reviews.map(r =>", idx+1)
    if idx2 != -1:
        print("Found second reviewsHTML at:", idx2)
        print(repr(content[idx2:idx2+300]))
    else:
        print("Only one reviewsHTML found at:", idx)
        print(repr(content[idx:idx+300]))

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
