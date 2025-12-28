# -*- coding: utf-8 -*-
"""Fix UTF-8 encoding issues in HTML files"""
import os
from pathlib import Path

def fix_encoding(content):
    """Fix common UTF-8 encoding issues"""

    # Fix arrows - MOST IMPORTANT
    # Fix the broken right arrow first (it's showing as left arrow + apostrophe)
    content = content.replace('\u2190\'', '\u2192')  # Fix broken right arrow
    content = content.replace('←\'', '\u2192')  # Fix broken right arrow variant

    # Then fix left arrows
    content = content.replace('â†', '\u2190')  # Left arrow

    # Fix quotes and apostrophes
    content = content.replace('â€™', "'")  # Right single quote
    content = content.replace('â€œ', '"')  # Left double quote
    content = content.replace('â€', '"')   # Right double quote

    # Fix ellipsis
    content = content.replace('â€¦', '\u2026')  # Ellipsis

    # Fix dashes
    content = content.replace('â€"', '\u2014')  # Em dash

    return content

def main():
    print("Fixing UTF-8 encoding issues in all HTML files...")
    print()
    
    website_dir = Path('echofall-website')
    html_files = list(website_dir.glob('*.html'))
    
    fixed_count = 0
    
    for html_file in html_files:
        # Read as bytes first
        with open(html_file, 'rb') as f:
            raw_bytes = f.read()
        
        # Decode as UTF-8
        try:
            content = raw_bytes.decode('utf-8')
        except:
            content = raw_bytes.decode('latin-1')
        
        original_content = content
        content = fix_encoding(content)
        
        if content != original_content:
            # Write back with UTF-8
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed: {html_file.name}")
            fixed_count += 1
    
    print()
    print(f"Fixed {fixed_count} files!")
    print()
    print("Common fixes:")
    print("  - Arrows: Fixed navigation arrows")
    print("  - Quotes: Fixed smart quotes")
    print("  - Other: Fixed ellipsis and dashes")
    print()
    print("Please refresh your browser (Ctrl+F5)!")

if __name__ == '__main__':
    main()

