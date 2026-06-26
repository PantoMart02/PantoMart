with open(r'assets\js\product.js', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print('Line 802 repr:', repr(lines[801]))

# Check backtick balance in renderSpaceProduct
space_start = content.find('function renderSpaceProduct')
space_end = content.find('function renderPetProduct')
space_content = content[space_start:space_end]
bt_count = space_content.count('`')
print('Backtick count in renderSpaceProduct:', bt_count)

# Check backtick balance in renderFitProduct
fit_start = content.find('function renderFitProduct')
fit_end = content.find('function renderSpaceProduct')
fit_content = content[fit_start:fit_end]
bt_fit = fit_content.count('`')
print('Backtick count in renderFitProduct:', bt_fit)

# Check backtick balance in renderStyleProduct
style_start = content.find('function renderStyleProduct')
style_end = content.find('function renderFitProduct')
style_content = content[style_start:style_end]
bt_style = style_content.count('`')
print('Backtick count in renderStyleProduct:', bt_style)
