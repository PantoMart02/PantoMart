import os, json, re
base_dir = r'c:\Users\yarra\OneDrive\Desktop\PantoMart'
catalog = []
for cat in ['care', 'style', 'fit', 'space', 'pet']:
    cat_dir = os.path.join(base_dir, cat)
    if not os.path.exists(cat_dir): continue
    for root, dirs, files in os.walk(cat_dir):
        if 'index.html' in files and root != cat_dir:
            content = open(os.path.join(root, 'index.html'), 'r', encoding='utf-8').read()
            tm = re.search(r'<h1 class="product-title">(.*?)</h1>', content)
            if tm:
                rel = os.path.relpath(root, base_dir).replace('\\', '/')
                catalog.append({'name': tm.group(1).strip(), 'url': f'/{rel}/', 'cat': cat.capitalize()})

search_js = os.path.join(base_dir, 'assets', 'js', 'search.js')
content = open(search_js, 'r', encoding='utf-8').read()

c1 = content.split('let allItems =')[0]
if 'let allItems =' not in content:
    c1 = content.split('const getRootPath')[0]
    
c2 = content.split('}));')[1] if '}));' in content else ''

new_logic = "const getRootPath = () => window.location.pathname.includes('/PantoMart/') ? '/PantoMart' : '';\n"
new_logic += "    const catalogData = " + json.dumps(catalog) + ";\n"
new_logic += "    let allItems = catalogData.map(i => ({ name: i.name, url: getRootPath() + i.url, cat: i.cat }));\n"

open(search_js, 'w', encoding='utf-8').write(c1 + new_logic + c2)
print('Injected catalog length:', len(catalog))
