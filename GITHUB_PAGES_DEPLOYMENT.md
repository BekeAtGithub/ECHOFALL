# GitHub Pages Deployment Instructions

## Quick Start

Your Echofall website is ready to deploy! All files are in the `docs/` folder.

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., "echofall-story")
3. Make it **Public** (required for free GitHub Pages)
4. Don't initialize with README (we already have one)

## Step 2: Push Your Code

Open terminal in the Echofall project folder and run:

```bash
git init
git add .
git commit -m "Initial commit - Echofall interactive story"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` with your actual GitHub username and repository name.

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Source", select:
   - Branch: `main`
   - Folder: `/docs`
5. Click **Save**

## Step 4: Wait for Deployment

- GitHub will build your site (takes 1-2 minutes)
- Your site will be available at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`
- You'll see a green checkmark when it's ready

## What's Included

✅ 48 HTML files (Prologue, Chronicles, 44 Chapters, Index)
✅ 89 images and videos
✅ 1 CSS stylesheet
✅ Fully responsive design
✅ Interactive navigation
✅ Alternative endings system

## File Structure

```
docs/
├── index.html              # Main table of contents
├── prologue.html
├── the-chronicles-of-evolution.html
├── chapter-1-*.html        # Chapters 1-44
├── styles.css              # Global styles
├── images/                 # All media files
│   ├── borealis.mp4
│   ├── earthbeauty.mp4
│   ├── fireplacelivingroom.png
│   ├── wifesmansion.mp4
│   └── [85 more files]
└── README.md
```

## Updating Your Site

After making changes:

```bash
# Regenerate HTML from markdown
python convert_md_to_html.py

# Copy updated files to docs
Copy-Item echofall-website\*.html docs\ -Force
Copy-Item echofall-website\styles.css docs\ -Force

# Commit and push
git add .
git commit -m "Update content"
git push
```

GitHub Pages will automatically rebuild your site within 1-2 minutes.

## Custom Domain (Optional)

To use a custom domain like `echofall.com`:

1. Buy a domain from a registrar (Namecheap, Google Domains, etc.)
2. Add a `CNAME` file to `docs/` with your domain name
3. Configure DNS settings at your registrar
4. Enable custom domain in GitHub Pages settings

## Troubleshooting

**Site not loading?**
- Check that GitHub Pages is enabled in Settings → Pages
- Verify the source is set to `main` branch and `/docs` folder
- Wait 2-3 minutes for initial deployment

**Images not showing?**
- All image paths are relative, so they should work automatically
- Check browser console for 404 errors

**Videos not playing?**
- GitHub Pages supports MP4 videos
- Check file sizes (GitHub has a 100MB file limit)

## Support

For issues with:
- **GitHub Pages**: https://docs.github.com/en/pages
- **Git**: https://git-scm.com/doc
- **This project**: Check the repository issues

---

**Your site is ready to go live! 🚀**

