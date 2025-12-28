# -*- coding: utf-8 -*-
"""Fix navigation arrows in HTML files"""
import re
from pathlib import Path

def fix_arrows_in_file(file_path):
    """Fix the navigation arrows in a single HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Define the arrow characters
    left_arrow = '←'
    right_arrow = '→'

    # Fix pattern: "Next: ... ←" should be "Next: ... →"
    # Simple string replacement approach
    lines = content.split('\n')
    new_lines = []

    for line in lines:
        if 'nav-next' in line and 'Next:' in line:
            # This is a Next button line
            # Replace the arrow before </a>
            if left_arrow in line:
                # Find the last occurrence of left arrow in this line
                parts = line.rsplit(left_arrow, 1)
                if len(parts) == 2 and '</a>' in parts[1]:
                    # Replace this left arrow with right arrow
                    line = parts[0] + right_arrow + parts[1]
                    # Also remove any apostrophe that might be there
                    line = line.replace(right_arrow + '\'', right_arrow)
        new_lines.append(line)

    content = '\n'.join(new_lines)

    return content, content != original_content

def main():
    print("Fixing navigation arrows in all HTML files...")
    print()
    
    website_dir = Path('echofall-website')
    html_files = list(website_dir.glob('*.html'))
    
    fixed_count = 0
    
    for html_file in html_files:
        new_content, was_changed = fix_arrows_in_file(html_file)
        
        if was_changed:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed: {html_file.name}")
            fixed_count += 1
    
    print()
    print(f"Fixed {fixed_count} files!")
    print("Navigation arrows should now display correctly:")
    print("  ← Previous  |  Home  |  Next →")
    print()
    print("Please refresh your browser (Ctrl+F5)!")

if __name__ == '__main__':
    main()

