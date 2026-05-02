import os

for root, _, files in os.walk('.'):
    if 'assets' in root or '.git' in root:
        continue
    
    # Calculate depth to root
    # root is something like '.', '.\care', '.\care\radiant-glow-serum'
    depth = 0
    if root != '.':
        depth = len(root.split(os.sep)) - 1
    
    prefix = '../' * depth if depth > 0 else './'
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace absolute paths with relative paths
            # This is a bit tricky, we need to be careful not to replace external URLs like https://
            # We want to replace href="/ and src="/ and data-url="/
            content = content.replace('href="/', f'href="{prefix}')
            content = content.replace('src="/', f'src="{prefix}')
            content = content.replace('data-url="/', f'data-url="{prefix}')
            content = content.replace('data-search-url="/', f'data-search-url="{prefix}')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed paths in {filepath} (depth {depth})")
