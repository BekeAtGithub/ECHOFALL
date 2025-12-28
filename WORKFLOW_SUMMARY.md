# Echofall Website - Complete Workflow Summary

## 📝 How to Make Changes to Your Website

### The Simple 3-Step Process:

1. **Edit the Markdown files** in `notion-export/Echofall/`
   - Example: `Chapter 42 - Option 1 1ecfda674d698036a0b0edfb304478c8.md`

2. **Run the conversion script:**
   ```bash
   python convert_md_to_html.py
   ```

3. **Refresh your browser** (Ctrl+F5) to see the changes

That's it! ✅

---

## 📂 File Structure

```
Echofall/
│
├── notion-export/Echofall/          ← EDIT THESE FILES
│   ├── Prologue ....md
│   ├── Chapter 1 - A Frozen Generation ....md
│   ├── Chapter 2 - Slop Life ....md
│   └── ... (all 46 markdown files)
│
├── echofall-website/                ← GENERATED FILES (don't edit directly)
│   ├── index.html
│   ├── prologue.html
│   ├── chapter-1-a-frozen-generation.html
│   ├── chapter-2-slop-life.html
│   ├── ... (all 46 HTML files)
│   ├── styles.css
│   └── images/
│       ├── borealis.mp4 (background video)
│       ├── wifesmansion.mp4
│       └── ... (all images)
│
└── convert_md_to_html.py            ← RUN THIS TO UPDATE
```

---

## 🛠️ Available Scripts

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `convert_md_to_html.py` | **Main script** - Converts MD to HTML | After editing any .md file |
| `fix_control_chars.py` | Remove invisible characters (squares) | If you see squares in browser |
| `fix_all_encoding.py` | Fix UTF-8 encoding issues | If you see weird characters like "Ã©" |
| `fix_arrows.py` | Fix navigation arrows | If arrows show as weird symbols |
| `add_background_to_chapters.py` | Add video background to chapters | Already done ✅ |

---

## ✅ What's Already Set Up

Your website is fully configured with:

- ✅ **Aurora borealis video background** on all pages
- ✅ **Proper UTF-8 encoding** (no weird characters)
- ✅ **Navigation arrows** (← Previous | Home | Next →)
- ✅ **Responsive design** (works on mobile/tablet/desktop)
- ✅ **Purple gradient theme** with starry overlay
- ✅ **All 46 chapters** converted and linked
- ✅ **Video embeds** (like wifesmansion.mp4 in Chapter 42)
- ✅ **Custom fonts** (Fireside font)

---

## 🎯 Common Tasks

### Task: Update text in a chapter
1. Open the .md file in `notion-export/Echofall/`
2. Make your changes
3. Run: `python convert_md_to_html.py`
4. Refresh browser (Ctrl+F5)

### Task: Add an image
1. Copy image to `echofall-website/images/`
2. In your .md file, add: `![Description](imagename.jpg)`
3. Run: `python convert_md_to_html.py`
4. Refresh browser (Ctrl+F5)

### Task: Add a video
1. Copy video to `echofall-website/images/`
2. In your .md file, add HTML:
   ```html
   <video controls style="width: 100%; max-width: 800px; margin: 20px auto; display: block;">
       <source src="images/yourvideo.mp4" type="video/mp4">
   </video>
   ```
3. Run: `python convert_md_to_html.py`
4. Refresh browser (Ctrl+F5)

### Task: Fix encoding issues
If you see weird characters after conversion:
```bash
python fix_control_chars.py
python fix_all_encoding.py
```

---

## ⚠️ Important Rules

### ✅ DO:
- Edit the `.md` files in `notion-export/Echofall/`
- Run `convert_md_to_html.py` after making changes
- Add images/videos to `echofall-website/images/`
- Use Ctrl+F5 to hard refresh your browser

### ❌ DON'T:
- Edit HTML files directly (they'll be overwritten)
- Delete the `convert_md_to_html.py` script
- Move files out of their folders
- Edit `styles.css` without backing it up first

---

## 🌐 Publishing Your Website

Your website is ready to publish! You can:

1. **GitHub Pages** (Free)
   - Upload `echofall-website/` folder to GitHub
   - Enable GitHub Pages in settings
   - Get a free URL like `yourusername.github.io/echofall`

2. **Netlify** (Free)
   - Drag and drop `echofall-website/` folder
   - Get instant free hosting

3. **Share as ZIP**
   - Zip the `echofall-website/` folder
   - Share with friends/family
   - They can open `index.html` locally

---

## 📞 Quick Reference

**Main command to remember:**
```bash
python convert_md_to_html.py
```

**Browser refresh:**
```
Ctrl+F5 (Windows/Linux)
Cmd+Shift+R (Mac)
```

**View website:**
```
Open: echofall-website/index.html
```

---

That's everything you need to know! 🎉

