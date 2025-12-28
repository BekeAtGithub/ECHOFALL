# -*- coding: utf-8 -*-
"""
Add video background to all chapter HTML files
"""
from pathlib import Path
import re

def add_video_background(content):
    """Add video background element after <body> tag if not present"""
    
    # Check if video background already exists
    if 'video-background' in content:
        return content, False
    
    # Find the <body> tag and add video background right after it
    video_element = '''    <video autoplay muted loop playsinline class="video-background">
        <source src="images/borealis.mp4" type="video/mp4">
    </video>
'''
    
    # Replace <body> with <body> + video element
    pattern = r'(<body>\s*)'
    replacement = r'\1' + video_element
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    return new_content, new_content != content

def main():
    print("=" * 70)
    print("ADDING VIDEO BACKGROUND TO ALL CHAPTERS")
    print("=" * 70)
    print()
    
    website_dir = Path('echofall-website')
    html_files = sorted(website_dir.glob('chapter-*.html'))
    
    fixed_count = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changed = add_video_background(content)
        
        if changed:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Added background to: {html_file.name}")
            fixed_count += 1
    
    print()
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   Added video background to {fixed_count} chapter files")
    print("=" * 70)
    print()
    print("The aurora borealis background will now persist across all chapters!")
    print("Please refresh your browser (Ctrl+F5) to see the changes!")

if __name__ == '__main__':
    main()

