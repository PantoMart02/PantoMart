import re

file_path = 'c:/Users/yarra/OneDrive/Desktop/PantoMart/assets/js/product.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact start and end positions
start_marker = '// ======================\r\n// Fitness (Fit) Renderer'
end_marker = '\n// Home Decor (Space) Renderer'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    # try \n instead of \r\n
    start_marker = '// ======================\n// Fitness (Fit) Renderer'
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

print(f"Start idx: {start_idx}, End idx: {end_idx}")
if start_idx != -1 and end_idx != -1:
    old_block = content[start_idx:end_idx]
    print(f"Block length: {len(old_block)} chars")
    print("First 200 chars:", repr(old_block[:200]))
    print("Last 100 chars:", repr(old_block[-100:]))
