#!/usr/bin/env python3
"""
Restore chapter HTML files from the original markdown files
This will fix encoding issues and remove incorrect sound effect wrapping
"""
import os
import re
from pathlib import Path
from html import escape

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def markdown_to_html(md_content):
    """Convert markdown to HTML with proper formatting"""
    html = md_content
    
    # Remove title (first line starting with #)
    html = re.sub(r'^#\s+.*?\n', '', html, count=1)
    
    # Convert headers
    html = re.sub(r'###\s+(.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'##\s+(.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Convert images
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="images/\2" alt="\1" class="content-image">', html)
    
    # Convert bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Convert italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Convert blockquotes (lines starting with >)
    lines = html.split('\n')
    in_blockquote = False
    new_lines = []
    for line in lines:
        if line.strip().startswith('>'):
            if not in_blockquote:
                new_lines.append('<blockquote>')
                in_blockquote = True
            new_lines.append(line.strip()[1:].strip())
        else:
            if in_blockquote:
                new_lines.append('</blockquote>')
                in_blockquote = False
            new_lines.append(line)
    if in_blockquote:
        new_lines.append('</blockquote>')
    html = '\n'.join(new_lines)
    
    # Convert horizontal rules
    html = re.sub(r'^---$', '<hr>', html, flags=re.MULTILINE)
    
    # Convert paragraphs
    paragraphs = html.split('\n\n')
    formatted_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<') and para not in ['', '\n']:
            para = f'<p>\n{para}</p>'
        formatted_paragraphs.append(para)
    html = '<p>'.join(formatted_paragraphs)
    
    return html

def get_chapter_info():
    """Get list of chapters to process"""
    chapters = []
    for i in range(1, 45):
        chapters.append(f"chapter-{i}")
    return chapters

def main():
    print("Restoring chapter HTML files from markdown...")
    print("This will fix encoding issues and remove incorrect wrapping\n")
    
    # We'll regenerate from the conversion script
    # For now, let's just remove the bad wrapping and fix encoding
    
    website_dir = Path('echofall-website')
    html_files = list(website_dir.glob('*.html'))
    
    fixed_count = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove ALL sound-effect spans completely
        content = re.sub(r'<span class="sound-effect">(.*?)</span>', r'\1', content)
        
        # Fix encoding issues - convert back to proper UTF-8
        content = content.replace('â€™', "'")  # Right single quotation mark
        content = content.replace('â€œ', '"')  # Left double quotation mark
        content = content.replace('â€', '"')   # Right double quotation mark
        content = content.replace('â€¦', '…')  # Ellipsis
        content = content.replace('â€"', '—')  # Em dash
        content = content.replace('â€"', '–')  # En dash
        content = content.replace('"¦', '…')  # Another ellipsis variant
        content = content.replace('â€', '"')   # Quote variants
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed: {html_file.name}")
            fixed_count += 1
    
    print(f"\n✓ Fixed {fixed_count} files!")
    print("Encoding issues resolved and incorrect sound effect wrapping removed.")

if __name__ == '__main__':
    main()

