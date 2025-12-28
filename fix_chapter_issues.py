#!/usr/bin/env python3
"""
Fix three issues:
1. Remove the "ECHOFALL" header from each chapter page
2. Fix asterisk in chapter titles (Chapter 5 and Chapter 8)
3. Fix the index.html chapter list titles
"""
import re
from pathlib import Path

def fix_chapter_html(file_path):
    """Remove the Echofall header from chapter pages"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove the header section with "Echofall" title
    # Pattern: <header>...</header> block including newlines
    content = re.sub(
        r'\s*<header>.*?</header>\s*\n',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content, content != original_content

def fix_index_html():
    """Fix the asterisk in chapter titles in index.html"""
    index_path = Path('echofall-website/index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix Chapter 5 - The **Spyware -> Chapter 5 - The Spyware
    content = content.replace('Chapter 5 - The **Spyware', 'Chapter 5 - The Spyware')
    
    # Fix Chapter 8 - *Sky Market Traders -> Chapter 8 - Sky Market Traders
    content = content.replace('Chapter 8 - *Sky Market Traders', 'Chapter 8 - Sky Market Traders')
    
    if content != original_content:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Fixing chapter issues...\n")
    
    # Fix index.html chapter titles
    if fix_index_html():
        print("✓ Fixed asterisks in index.html chapter titles")
    
    # Fix all chapter HTML files
    website_dir = Path('echofall-website')
    chapter_files = list(website_dir.glob('chapter-*.html'))
    
    fixed_count = 0
    
    for chapter_file in chapter_files:
        new_content, was_changed = fix_chapter_html(chapter_file)
        
        if was_changed:
            with open(chapter_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1
    
    print(f"✓ Removed 'ECHOFALL' header from {fixed_count} chapter pages")
    
    # Also fix prologue and other pages
    other_pages = ['prologue.html', 'the-chronicles-of-evolution.html']
    for page_name in other_pages:
        page_path = website_dir / page_name
        if page_path.exists():
            new_content, was_changed = fix_chapter_html(page_path)
            if was_changed:
                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ Removed 'ECHOFALL' header from {page_name}")
    
    print("\n✅ All issues fixed!")
    print("Note: The purple button in the corner might be a browser rendering issue.")
    print("Try refreshing the page (Ctrl+F5) to clear the cache.")

if __name__ == '__main__':
    main()

