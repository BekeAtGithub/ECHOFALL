# -*- coding: utf-8 -*-
"""Remove stray apostrophes after navigation arrows"""
from pathlib import Path

def fix_apostrophes_in_file(file_path):
    """Remove apostrophes after right arrows in navigation"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove right single quotation mark (U+2019) after right arrow
    content = content.replace('→\u2019', '→')
    # Also try regular apostrophe just in case
    content = content.replace('→\'', '→')

    return content, content != original_content

def main():
    print("Removing stray apostrophes after arrows...")
    print()
    
    website_dir = Path('echofall-website')
    html_files = list(website_dir.glob('*.html'))
    
    fixed_count = 0
    
    for html_file in html_files:
        new_content, was_changed = fix_apostrophes_in_file(html_file)
        
        if was_changed:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed: {html_file.name}")
            fixed_count += 1
    
    print()
    print(f"Fixed {fixed_count} files!")
    print("Please refresh your browser (Ctrl+F5)!")

if __name__ == '__main__':
    main()

