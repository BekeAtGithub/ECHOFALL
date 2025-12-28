#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Dramatic sound effects to wrap in red
DRAMATIC_SOUNDS = ['BANG', 'CLANG', 'WHOOSH', 'CRASH', 'BOOM', 'CHIK-CHAK', 'SLAM', 'THUD', 'CRACK']

def wrap_sound_effects(content):
    """Wrap dramatic sound effects in span tags if not already wrapped"""
    changes = 0

    for sound in DRAMATIC_SOUNDS:
        wrapped_version = f'<span class="sound-effect">{sound}</span>'

        # Pattern: Match sound as a WHOLE WORD only (not part of another word)
        # Use word boundaries but also check for HTML context
        pattern = r'\b' + re.escape(sound) + r'\b'
        matches = re.finditer(pattern, content, re.IGNORECASE)

        # Track positions to replace (in reverse order to maintain indices)
        positions_to_wrap = []

        for match in matches:
            start = match.start()
            end = match.end()
            matched_text = match.group()

            # Only wrap if it's the exact uppercase version (not "cracked", "cracker", etc.)
            if matched_text != sound:
                continue

            # Check if this occurrence is already wrapped
            lookback_start = max(0, start - 25)
            lookback = content[lookback_start:start]
            lookforward = content[end:end+7]

            # Skip if already wrapped
            if 'sound-effect">' in lookback or lookforward == '</span>':
                continue

            # Skip if inside a heading tag (h1, h2, h3, title, etc.)
            # Look back further to check for heading tags
            lookback_far = content[max(0, start - 100):start]
            lookforward_far = content[end:min(len(content), end + 100)]

            # Check if we're inside a heading or title
            in_heading = False
            for tag in ['<h1', '<h2', '<h3', '<h4', '<title']:
                if tag in lookback_far and '</h' not in lookback_far[lookback_far.rfind(tag):]:
                    in_heading = True
                    break
                if tag in lookback_far and 'title>' not in lookback_far[lookback_far.rfind(tag):]:
                    in_heading = True
                    break

            if not in_heading:
                positions_to_wrap.append((start, end))

        # Replace in reverse order to maintain indices
        for start, end in reversed(positions_to_wrap):
            content = content[:start] + wrapped_version + content[end:]
            changes += 1

    return content, changes

def main():
    website_dir = Path('echofall-website')
    html_files = list(website_dir.glob('*.html'))  # Check ALL HTML files

    total_changes = 0
    files_modified = 0
    files_checked = 0

    for html_file in html_files:
        files_checked += 1
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = wrap_sound_effects(content)

        if changes > 0:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"{html_file.name}: {changes} sound effects wrapped")
            total_changes += changes
            files_modified += 1

    print(f"\n✓ Checked {files_checked} files")
    print(f"✓ Total: {total_changes} dramatic sound effects wrapped in {files_modified} files!")
    print("All dramatic sounds (BANG, CLANG, WHOOSH, CRASH, BOOM, CHIK-CHAK, SLAM, THUD, CRACK) now appear in RED!")

if __name__ == '__main__':
    main()

