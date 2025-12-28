# -*- coding: utf-8 -*-
"""
Comprehensive fix for ALL UTF-8 encoding issues in HTML files
This will fix the double-encoded UTF-8 characters
"""
from pathlib import Path

def fix_all_encoding_issues(content):
    """Fix all UTF-8 encoding issues comprehensively"""
    
    # The issue is double-encoding: UTF-8 bytes interpreted as Latin-1, then re-encoded as UTF-8
    # We need to fix these specific patterns
    
    # Fix café -> café (C3 A9 shown as Ã©)
    content = content.replace('Ã©', 'é')
    content = content.replace('Ã¨', 'è')
    content = content.replace('Ã«', 'ë')
    content = content.replace('Ãª', 'ê')
    
    # Fix other accented characters
    content = content.replace('Ã¡', 'á')
    content = content.replace('Ã ', 'à')
    content = content.replace('Ã¢', 'â')
    content = content.replace('Ã£', 'ã')
    content = content.replace('Ã¤', 'ä')
    content = content.replace('Ã¥', 'å')
    
    content = content.replace('Ã­', 'í')
    content = content.replace('Ã¬', 'ì')
    content = content.replace('Ã®', 'î')
    content = content.replace('Ã¯', 'ï')
    
    content = content.replace('Ã³', 'ó')
    content = content.replace('Ã²', 'ò')
    content = content.replace('Ã´', 'ô')
    content = content.replace('Ãµ', 'õ')
    content = content.replace('Ã¶', 'ö')
    
    content = content.replace('Ãº', 'ú')
    content = content.replace('Ã¹', 'ù')
    content = content.replace('Ã»', 'û')
    content = content.replace('Ã¼', 'ü')
    
    content = content.replace('Ã±', 'ñ')
    content = content.replace('Ã§', 'ç')
    
    # Fix quotes - the three-byte sequences
    content = content.replace('â€œ', '"')  # Left double quote
    content = content.replace('â€', '"')   # Right double quote
    content = content.replace('â€™', "'")  # Right single quote
    content = content.replace('â€˜', "'")  # Left single quote
    
    # Fix ellipsis
    content = content.replace('â€¦', '…')
    
    # Fix dashes
    content = content.replace('â€"', '—')  # Em dash
    content = content.replace('â€"', '–')  # En dash
    
    # Fix any remaining Â characters (non-breaking space artifacts)
    content = content.replace('Â ', ' ')
    content = content.replace('Â', '')
    
    return content

def main():
    print("=" * 60)
    print("COMPREHENSIVE UTF-8 ENCODING FIX")
    print("=" * 60)
    print()
    print("Fixing ALL encoding issues in every HTML file...")
    print()
    
    website_dir = Path('echofall-website')
    html_files = sorted(website_dir.glob('*.html'))
    
    fixed_count = 0
    total_replacements = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = fix_all_encoding_issues(content)
        
        if content != original_content:
            # Count how many characters changed
            changes = sum(1 for a, b in zip(original_content, content) if a != b)
            changes += abs(len(original_content) - len(content))
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed: {html_file.name} ({changes} characters changed)")
            fixed_count += 1
            total_replacements += changes
    
    print()
    print("=" * 60)
    print(f"✅ COMPLETE!")
    print(f"   Fixed {fixed_count} files")
    print(f"   Total characters corrected: {total_replacements}")
    print("=" * 60)
    print()
    print("Common fixes applied:")
    print("  - Accented characters (Cafe -> Cafe)")
    print("  - Smart quotes")
    print("  - Apostrophes")
    print("  - Ellipsis")
    print("  - Em dashes")
    print()
    print("Please refresh your browser (Ctrl+F5) to see the changes!")

if __name__ == '__main__':
    main()

