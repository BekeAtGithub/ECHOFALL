#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert Markdown files from notion-export to HTML files in echofall-website
Run this script whenever you make changes to the .md files
"""
import os
import re
from pathlib import Path

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
    
    # Convert blockquotes and lists
    lines = html.split('\n')
    new_lines = []
    in_blockquote = False
    in_list = False

    for line in lines:
        # Handle blockquotes
        if line.startswith('> '):
            if not in_blockquote:
                new_lines.append('<blockquote>')
                in_blockquote = True
            new_lines.append(line[2:])
        else:
            if in_blockquote:
                new_lines.append('</blockquote>')
                in_blockquote = False

            # Handle unordered lists
            if line.strip().startswith('- '):
                if not in_list:
                    new_lines.append('<ul>')
                    in_list = True
                # Remove the "- " and wrap in <li>
                list_item = line.strip()[2:]
                new_lines.append(f'<li>{list_item}</li>')
            else:
                if in_list:
                    new_lines.append('</ul>')
                    in_list = False
                new_lines.append(line)

    if in_blockquote:
        new_lines.append('</blockquote>')
    if in_list:
        new_lines.append('</ul>')

    html = '\n'.join(new_lines)
    
    # Convert horizontal rules
    html = re.sub(r'^---$', '<hr>', html, flags=re.MULTILINE)
    
    # Convert paragraphs - wrap text in <p> tags
    paragraphs = html.split('\n\n')
    formatted_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<') and para not in ['', '\n']:
            para = f'{para}</p><p>'
        formatted_paragraphs.append(para)
    html = '<p>'.join(formatted_paragraphs)
    
    return html

def get_html_template(title, content, prev_link=None, next_link=None):
    """Generate HTML template for a chapter"""
    
    # Navigation
    nav_prev = f'<a href="{prev_link[1]}" class="nav-prev">← Previous: {prev_link[0]}</a>' if prev_link else ''
    nav_next = f'<a href="{next_link[1]}" class="nav-next">Next: {next_link[0]} →</a>' if next_link else ''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Echofall</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <video autoplay muted loop playsinline class="video-background">
        <source src="images/borealis.mp4" type="video/mp4">
    </video>
<div class="container">

        <main>

            <nav class="chapter-nav">{nav_prev}<a href="index.html" class="nav-home">Home</a>{nav_next}</nav>

            <article class="content">
                <h1>{title}</h1>{content}
            </article>

            <nav class="chapter-nav">{nav_prev}<a href="index.html" class="nav-home">Home</a>{nav_next}</nav>

        </main>

    </div>

</body>

</html>
'''

def get_chapter_mapping():
    """Map markdown files to their HTML equivalents and navigation"""
    chapters = []
    
    # Add prologue and chronicles
    chapters.append({
        'md': 'notion-export/Echofall/Prologue 1e7fda674d69801c87d0dcd3c11e3787.md',
        'html': 'prologue.html',
        'title': 'Prologue'
    })
    
    chapters.append({
        'md': 'notion-export/Echofall/The Chronicles of Evolution 1ecfda674d698086ab3dfcd2147ad2d8.md',
        'html': 'the-chronicles-of-evolution.html',
        'title': 'The Chronicles of Evolution'
    })
    
    # Add all 44 chapters
    chapter_files = list(Path('notion-export/Echofall').glob('Chapter *.md'))

    # Sort by chapter number (not alphabetically)
    def get_chapter_number(filepath):
        match = re.match(r'Chapter (\d+) - ', filepath.name)
        return int(match.group(1)) if match else 999

    chapter_files = sorted(chapter_files, key=get_chapter_number)

    for chapter_file in chapter_files:
        # Extract chapter number and title from filename
        match = re.match(r'Chapter (\d+) - (.+?) [a-f0-9]+\.md', chapter_file.name)
        if match:
            num, title = match.groups()
            slug = slugify(f'chapter-{num}-{title}')
            chapters.append({
                'md': str(chapter_file),
                'html': f'{slug}.html',
                'title': f'Chapter {num} - {title}'
            })

    return chapters

def main():
    print("=" * 70)
    print("CONVERTING MARKDOWN TO HTML")
    print("=" * 70)
    print()
    print("This will update all HTML files from the Markdown sources...")
    print()

    chapters = get_chapter_mapping()
    converted = 0

    for i, chapter in enumerate(chapters):
        md_path = Path(chapter['md'])

        if not md_path.exists():
            print(f"⚠ Skipping {chapter['title']} - MD file not found")
            continue

        # Read markdown content
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert to HTML
        html_content = markdown_to_html(md_content)

        # Determine prev/next links
        prev_link = None
        next_link = None

        # Special handling for alternative endings (chapters 42, 43, 44)
        # These are standalone endings and should have no navigation buttons
        is_alternative_ending = chapter['html'] in ['chapter-42-option-1.html', 'chapter-43-option-2.html', 'chapter-44-option-3.html']

        # Chapter 41 is the last main chapter before alternative endings
        is_chapter_41 = 'chapter-41' in chapter['html']

        if not is_alternative_ending:
            if i > 0:
                prev_link = (chapters[i-1]['title'], chapters[i-1]['html'])
            # Chapter 41 should not have a next button (branches to alternative endings)
            if i < len(chapters) - 1 and not is_chapter_41:
                next_link = (chapters[i+1]['title'], chapters[i+1]['html'])

        # Generate full HTML page
        full_html = get_html_template(
            chapter['title'],
            html_content,
            prev_link,
            next_link
        )

        # Write to file
        output_path = Path('echofall-website') / chapter['html']
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

        print(f"✓ Converted: {chapter['title']}")
        converted += 1

    print()
    print("=" * 70)
    print(f"✅ COMPLETE!")
    print(f"   Converted {converted} files")
    print("=" * 70)
    print()
    print("Your HTML files have been updated from the Markdown sources!")
    print("Refresh your browser (Ctrl+F5) to see the changes.")

if __name__ == '__main__':
    main()

