import sys

with open('build_all_products.py', 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('category_template = """<!DOCTYPE html>')
prod_tmpl = parts[0]
cat_tmpl = 'category_template = """<!DOCTYPE html>' + parts[1]

prod_tmpl = prod_tmpl.replace('href="/assets/css/', 'href="../../assets/css/')
prod_tmpl = prod_tmpl.replace('src="/assets/js/', 'src="../../assets/js/')
prod_tmpl = prod_tmpl.replace('href="/" class="brand-logo"', 'href="../../" class="brand-logo"')
prod_tmpl = prod_tmpl.replace('href="/profile/', 'href="../../profile/')
prod_tmpl = prod_tmpl.replace('href="/login/"', 'href="../../login/"')
prod_tmpl = prod_tmpl.replace('href="/about/"', 'href="../../about/"')
prod_tmpl = prod_tmpl.replace('href="/contact/"', 'href="../../contact/"')
prod_tmpl = prod_tmpl.replace('href="/terms/"', 'href="../../terms/"')
prod_tmpl = prod_tmpl.replace('href="/privacy-policy/"', 'href="../../privacy-policy/"')

cat_tmpl = cat_tmpl.replace('href="/assets/css/', 'href="../assets/css/')
cat_tmpl = cat_tmpl.replace('src="/assets/js/', 'src="../assets/js/')
cat_tmpl = cat_tmpl.replace('href="/" class="brand-logo"', 'href="../" class="brand-logo"')
cat_tmpl = cat_tmpl.replace('href="/profile/', 'href="../profile/')
cat_tmpl = cat_tmpl.replace('href="/login/"', 'href="../login/"')
cat_tmpl = cat_tmpl.replace('href="/about/"', 'href="../about/"')
cat_tmpl = cat_tmpl.replace('href="/contact/"', 'href="../contact/"')
cat_tmpl = cat_tmpl.replace('href="/terms/"', 'href="../terms/"')
cat_tmpl = cat_tmpl.replace('href="/privacy-policy/"', 'href="../privacy-policy/"')

content = prod_tmpl + cat_tmpl

content = content.replace('data-search-url="/{rel[\'cat\']}/{rel[\'slug\']}/"', 'data-search-url="../../{rel[\'cat\']}/{rel[\'slug\']}/"')
content = content.replace('href="/{rel[\'cat\']}/{rel[\'slug\']}/"', 'href="../../{rel[\'cat\']}/{rel[\'slug\']}/"')
content = content.replace('data-url="/{cat_id}/{slug}/"', 'data-url="../../{cat_id}/{slug}/"')
content = content.replace('href="/{cat_id}/{slug}/"', 'href="../../{cat_id}/{slug}/"')

content = content.replace('web_path = "/" + img_path.replace("\\\\", "/")', 'web_path = "../../" + img_path.replace("\\\\", "/")')

with open('build_all_products.py', 'w', encoding='utf-8') as f:
    f.write(content)
