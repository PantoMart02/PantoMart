import os

categories = ['care', 'style', 'fit', 'space', 'pet']
base_dir = r'c:\Users\yarra\OneDrive\Desktop\PantoMart'

for cat in categories:
    filepath = os.path.join(base_dir, cat, 'index.html')
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to inject the button right after the <p> inside the category-hero text-center block
    # Look for </p>\n    </div>\n  </section>
    
    # In care/index.html, it's:
    #       <p style="font-size:1.2rem; color:#f8f8f8;">PantoCare Essential Luxury Collection</p>
    #     </div>
    #   </section>
    
    search_str = '</p>\n    </div>\n  </section>'
    replace_str = '</p>\n      <div style="margin-top: 24px;"><a href="../" class="btn btn-outline" style="color: #fff; border-color: rgba(255,255,255,0.5); border-width: 2px;">Back to Home</a></div>\n    </div>\n  </section>'
    
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {cat}/index.html")
    else:
        print(f"Could not find injection point in {cat}/index.html")
