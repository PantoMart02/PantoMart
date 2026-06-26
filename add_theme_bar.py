files = ['category.html', 'product.html']
bar = (
    '\n    <!-- Announcement Bar -->\n'
    '    <div class="w-full bg-primary text-on-primary text-center py-2.5 text-[11px] uppercase tracking-[0.2em] font-body-md">\n'
    '        PantoMart &nbsp;&mdash;&nbsp; <span class="opacity-70">Smart products for intentional everyday life</span>\n'
    '    </div>\n'
)
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'Announcement Bar' not in c:
        c = c.replace(
            '<body class="bg-background text-on-surface font-body-md overflow-x-hidden">',
            '<body class="bg-background text-on-surface font-body-md overflow-x-hidden">' + bar,
            1
        )
    if 'theme.js' not in c:
        c = c.replace('</head>', '    <script src="./assets/js/theme.js"></script>\n</head>', 1)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{fname}: updated')
