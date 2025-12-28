# -*- coding: utf-8 -*-
"""
Remove all control characters and invisible characters that show as squares
"""
import re
from pathlib import Path

def remove_control_characters(content):
    """Remove control characters and other problematic invisible characters"""
    
    # Remove specific control characters that commonly appear as squares
    # U+009D - Operating System Command
    content = content.replace('\u009d', '')
    content = content.replace('\u009c', '')
    content = content.replace('\u009e', '')
    content = content.replace('\u009f', '')
    
    # Remove other common control characters (except newline, tab, carriage return)
    # Control characters are U+0000 to U+001F and U+007F to U+009F
    control_chars = ''.join(chr(i) for i in range(0, 32) if i not in [9, 10, 13])
    control_chars += ''.join(chr(i) for i in range(127, 160))
    
    for char in control_chars:
        content = content.replace(char, '')
    
    # Also remove zero-width characters that might show as squares
    content = content.replace('\u200b', '')  # Zero-width space
    content = content.replace('\u200c', '')  # Zero-width non-joiner
    content = content.replace('\u200d', '')  # Zero-width joiner
    content = content.replace('\ufeff', '')  # Zero-width no-break space (BOM)
    
    return content

def main():
    print("=" * 70)
    print("REMOVING CONTROL CHARACTERS (SQUARES)")
    print("=" * 70)
    print()
    
    website_dir = Path('echofall-website')
    html_files = sorted(website_dir.glob('*.html'))
    
    fixed_count = 0
    total_removed = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = remove_control_characters(content)
        
        if content != original_content:
            removed = len(original_content) - len(content)
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed: {html_file.name} (removed {removed} control characters)")
            fixed_count += 1
            total_removed += removed
    
    print()
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   Fixed {fixed_count} files")
    print(f"   Removed {total_removed} invisible/control characters")
    print("=" * 70)
    print()
    print("These characters were showing as squares in your browser.")
    print("Please refresh (Ctrl+F5) to see the changes!")

if __name__ == '__main__':
    main()

