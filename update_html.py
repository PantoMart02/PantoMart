import os
import glob

font_link = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">\n  <link href="https://fonts.googleapis.com/css2?family=Inter'

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Playfair+Display' not in content:
        content = content.replace('<link href="https://fonts.googleapis.com/css2?family=Inter', font_link)
    
    # Add animate-on-scroll to cards and sections where appropriate
    content = content.replace('class="card"', 'class="card animate-on-scroll"')
    content = content.replace('class="container section"', 'class="container section animate-on-scroll"')
    # Prevent double adding if script is run twice
    content = content.replace('animate-on-scroll animate-on-scroll', 'animate-on-scroll')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('**/*.html', recursive=True):
    update_file(file)

print("Updated HTML files.")
