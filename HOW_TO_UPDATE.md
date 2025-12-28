# How to Update Your Echofall Website

## Workflow for Making Changes

### Step 1: Edit the Markdown Files
Edit your chapter content in the Markdown (.md) files located in:
```
notion-export/Echofall/
```

For example:
- `Chapter 42 - Option 1 1ecfda674d698036a0b0edfb304478c8.md`
- `Chapter 1 - A Frozen Generation 1e7fda674d69801c8e5bfb8e8e8e8e8e.md`
- etc.

### Step 2: Convert Markdown to HTML
After making changes to any .md files, run the conversion script:

```bash
python convert_md_to_html.py
```

This will:
- Read all your Markdown files from `notion-export/Echofall/`
- Convert them to HTML
- Update the files in `echofall-website/`
- Preserve all styling, navigation, and the video background

### Step 3: View Your Changes
1. Open `echofall-website/index.html` in your browser
2. Press `Ctrl+F5` to hard refresh and clear cache
3. Navigate to the chapter you edited to see your changes

## Important Notes

### ⚠️ Don't Edit HTML Files Directly
- Always edit the `.md` files in `notion-export/Echofall/`
- The HTML files in `echofall-website/` are generated from the Markdown
- If you edit HTML directly, your changes will be overwritten when you run the conversion script

### ✅ Exception: Special HTML Elements
If you need to add special HTML elements (like videos, custom styling, etc.) that can't be done in Markdown:
1. First run `python convert_md_to_html.py` to update from Markdown
2. Then manually add your special HTML elements to the generated HTML file
3. Document what you added so you can re-add it if you need to regenerate

### 📝 Example: Adding a Video
If you want to add a video in the middle of a chapter:

**Option 1: Add to Markdown (if supported)**
```markdown
<video controls style="width: 100%; max-width: 800px;">
    <source src="images/myvideo.mp4" type="video/mp4">
</video>
```

**Option 2: Add after conversion**
1. Run `python convert_md_to_html.py`
2. Open the generated HTML file
3. Find the location where you want the video
4. Add the video HTML code

## File Structure

```
Echofall/
├── notion-export/
│   └── Echofall/
│       ├── Chapter 1 - A Frozen Generation ....md
│       ├── Chapter 2 - Slop Life ....md
│       └── ... (all your source .md files)
│
├── echofall-website/
│   ├── index.html
│   ├── chapter-1-a-frozen-generation.html
│   ├── chapter-2-slop-life.html
│   ├── ... (all generated .html files)
│   ├── styles.css
│   └── images/
│
└── convert_md_to_html.py  ← Run this to update HTML from Markdown
```

## Quick Reference

| Task | Command |
|------|---------|
| Update HTML from Markdown | `python convert_md_to_html.py` |
| View website | Open `echofall-website/index.html` |
| Hard refresh browser | `Ctrl+F5` |

## Troubleshooting

### Changes not showing in browser?
- Make sure you ran `python convert_md_to_html.py`
- Press `Ctrl+F5` to hard refresh and clear cache
- Try opening in incognito/private mode

### Encoding issues (weird characters)?
- Run `python fix_control_chars.py` to remove control characters
- Run `python fix_all_encoding.py` to fix UTF-8 issues

### Navigation broken?
- Run `python fix_arrows.py` to fix navigation arrows

