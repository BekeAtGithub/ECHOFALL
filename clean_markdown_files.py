#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean up markdown files:
1. Remove all triple dashes (---)
2. Remove Notion links at the bottom (like [**Chapter 3 - The Living World**](...))
"""
import re
from pathlib import Path

def clean_markdown(content):
    """Clean markdown content"""
    original_content = content

    # Remove all lines with just triple dashes
    content = re.sub(r'^---\s*$', '', content, flags=re.MULTILINE)

    # Remove Notion chapter links - multiple patterns:
    # Pattern 1: [**Chapter X - Title**](Chapter%20...)
    content = re.sub(r'\[\*\*Chapter \d+[^\]]*\*\*\]\(Chapter%20[^\)]+\.md\)', '', content)

    # Pattern 2: [Chapter X - Title](Chapter%20...)
    content = re.sub(r'\[Chapter \d+[^\]]*\]\(Chapter%20[^\)]+\.md\)', '', content)

    # Pattern 3: Any link with Chapter%20 in it
    content = re.sub(r'\[[^\]]+\]\([^\)]*Chapter%20[^\)]+\.md\)', '', content)

    # Pattern 4: Links to other pages like Prologue, etc.
    content = re.sub(r'\[[^\]]+\]\([^\)]*%20[^\)]+\.md\)', '', content)

    # Remove excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Clean up trailing whitespace
    content = content.rstrip() + '\n'

    return content, content != original_content

def main():
    print("=" * 70)
    print("CLEANING MARKDOWN FILES")
    print("=" * 70)
    print()
    print("Removing:")
    print("  - Triple dashes (---)")
    print("  - Notion chapter links at the bottom")
    print()
    
    notion_dir = Path('notion-export/Echofall')
    md_files = sorted(notion_dir.glob('*.md'))
    
    cleaned_count = 0
    total_files = 0
    
    for md_file in md_files:
        total_files += 1
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned_content, was_changed = clean_markdown(content)
        
        if was_changed:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            print(f"✓ Cleaned: {md_file.name}")
            cleaned_count += 1
    
    print()
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   Cleaned {cleaned_count} out of {total_files} files")
    print("=" * 70)
    print()
    print("Next step: Run 'python convert_md_to_html.py' to update the website")

if __name__ == '__main__':
    main()

