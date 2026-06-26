file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the bad benefitsHTML block - single quotes inside single-quoted string onmouseover
bad = (
    "  const benefitsHTML = benefits.map(b =>\n"
    "    '<div style=\"background:#fff;padding:35px 25px;border-radius:16px;text-align:center;border:1px solid #FDEAEA;transition:box-shadow 0.3s;\" onmouseover=\"this.style.boxShadow='0 15px 40px rgba(0,0,0,0.05)'\" onmouseout=\"this.style.boxShadow='none'\">'"
)

good = (
    "  const benefitsHTML = benefits.map(b =>\n"
    "    '<div style=\"background:#fff;padding:35px 25px;border-radius:16px;text-align:center;border:1px solid #FDEAEA;transition:box-shadow 0.3s;\" onmouseover=\"this.style.boxShadow=\\'0 15px 40px rgba(0,0,0,0.05)\\'\" onmouseout=\"this.style.boxShadow=\\'none\\'\">'"
)

if bad in content:
    content = content.replace(bad, good, 1)
    print("Fixed benefitsHTML onmouseover quotes")
else:
    print("Pattern not found exactly — showing surrounding area for debug")
    idx = content.find("const benefitsHTML = benefits.map")
    if idx != -1:
        print(repr(content[idx:idx+400]))
    else:
        print("benefitsHTML not found at all")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
