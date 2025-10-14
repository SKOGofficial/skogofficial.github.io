# Rubber Duck Newsletter

**Tagline:** PUSHED TO MAIN

A modern, responsive newsletter website themed around programming, research, and tech-life storytelling. Built with Eleventy (11ty), combining humor, intellect, and personality.

## 🦆 What's Been Built

### Core Features

1. **Newsletter Homepage** (`src/index.njk`)
   - Yellow rubber duck logo in circular frame (masthead)
   - Subject line hook: "merge_conflict, NEED REVIEW"
   - Intro/pathos section explaining the newsletter
   - Featured image display
   - Recent issues grid (displays latest 3 posts)
   - CTA section for subscriptions and Discord

2. **Newsletter Post Layout** (`src/_layouts/newsletter.njk`)
   - Masthead with duck logo
   - Subject line display
   - Article headline (uppercase, bordered, red accent)
   - Publication date and author metadata
   - Formatted article content with proper typography
   - Footer with author bio and 4 CTAs:
     - Subscribe
     - Connect with me
     - Join Discord
     - Hire Me

3. **Newsletter Archive** (`src/newsletter-archive.njk`)
   - All past issues displayed in grid format
   - Numbered issues with excerpts
   - Links to full articles

4. **Sample Post** (`src/posts/issue-01.md`)
   - Complete example newsletter following the style guide
   - Demonstrates narrative flow, code snippets, and formatting

## 🎨 Design System

### Typography

- **Headlines/Section Titles:** Orbitron, bold, all caps, red #F11B0C
- **Subheadings:** Orbitron or Roboto Bold, dark gray #202020
- **Body Text:** Roboto Regular, dark gray #1A1A1A
- **Emphasis:** Roboto Bold, all caps, red #F11B0C

### Colors

- **Primary Red:** #F11B0C (accent, highlights)
- **Dark Gray:** #202020 (borders, text)
- **Body Text:** #1A1A1A
- **Shadow Gray:** #9A9A9A
- **Light Gray:** #C2C2C2
- **White:** #FFFFFF (background)

### Layout Principles

- Narrative flow over rigid structure
- High-quality full-width images as visual breaks
- Large vertical spacing between sections
- Maximum 3 sentences per paragraph (for readability)
- Clean borders with dark gray outlines

## 📁 File Structure

```
src/
├── _layouts/
│   ├── base.njk           # Main site layout
│   └── newsletter.njk     # Newsletter post layout
├── assets/
│   └── images/
│       └── rubber-duck-logo.svg  # Yellow duck logo
├── css/
│   ├── main.css          # Base brand styles
│   ├── index.css         # Homepage newsletter styles
│   └── newsletter.css    # Newsletter post styles
├── posts/
│   ├── issue-01.md       # Sample newsletter post
│   └── posts.json        # Post directory config
├── index.njk             # Newsletter homepage
└── newsletter-archive.njk # All issues archive
```

## 🚀 How to Use

### Creating New Newsletter Posts

1. Create a new Markdown file in `src/posts/`:

```markdown
---
layout: newsletter.njk
title: "Your Newsletter Title"
date: 2025-10-21
subjectLine: "Custom subject line (optional)"
excerpt: "Brief excerpt for the homepage preview"
---

## YOUR FIRST SECTION

Write your content here. Use **UPPERCASE BOLD** for emphasis.

![Alt text for image](/assets/images/your-image.jpg)

Remember: max 3 sentences per paragraph for readability!
```

2. Build and preview:

```bash
npm run serve
```

3. Deploy:

```bash
npm run build
```

### Customizing the Newsletter

#### Update the Duck Logo
Replace `src/assets/images/rubber-duck-logo.svg` with your custom logo (keep it 200x200px for best results).

#### Change the Tagline
Edit the tagline in both:
- `src/index.njk` (line 14)
- `src/_layouts/newsletter.njk` (line 14)

#### Modify CTAs
Edit the footer CTAs in `src/_layouts/newsletter.njk` (lines 43-58):
- Update links (replace `#subscribe`, `#connect`, etc.)
- Change button text
- Add/remove buttons

#### Update Author Bio
Edit `src/_layouts/newsletter.njk` (lines 37-42):
- Change the avatar image
- Update the bio text

## 🎯 Content Guidelines

### Writing Style

- **Tone:** Nerdy, witty, narrative-driven
- **Voice:** First-person, conversational
- **Format:** Half storytelling, half technical insights
- **Ethos:** Honest reflections + practical takeaways

### Content Structure

1. **Headline:** Quirky, intriguing hook
2. **Intro:** Personal story or insight (2-3 paragraphs)
3. **Featured Image:** Full-width, high-quality, relevant
4. **Narrative Sections:** Short modular paragraphs with H2 headers
5. **Demo/Code:** Optional interactive elements or snippets
6. **Visual Breaks:** Additional images throughout
7. **Wrap-up:** Key takeaways and next steps

### Formatting Tips

- Use `**UPPERCASE BOLD**` for key terms and emphasis
- Keep paragraphs to 3 sentences max
- Add images with ample white space (3rem margins)
- Use H2 for main sections (uppercase, red accent bar)
- Use H3 for subsections
- Code blocks automatically get borders and styling

## 📧 Future Integrations

The site is ready for these optional integrations:

1. **Email Subscription:**
   - Buttondown
   - ConvertKit
   - Mailchimp

2. **Community:**
   - Discord webhook
   - Comments system (optional)

3. **Analytics:**
   - Google Analytics
   - Plausible
   - Simple Analytics

## 🏗️ Technical Details

### Built With

- **Static Site Generator:** Eleventy 3.1.2
- **Template Engine:** Nunjucks
- **Styling:** Vanilla CSS (no frameworks)
- **Icons:** Font Awesome 6.0.0

### Eleventy Configuration

The `.eleventy.js` file includes:
- `readableDate` filter for formatting dates
- `limit` filter for truncating arrays
- `slugify` filter for URL generation
- `newsletter` collection for all posts

### Performance Features

- Lazy-load images (ready for implementation)
- Minimal CSS (no frameworks)
- Static HTML generation
- Fast page loads

## 📝 Quick Reference

### Key URLs

- Homepage: `/`
- Newsletter Archive: `/newsletter-archive/`
- Individual Post: `/posts/[post-slug]/`

### CSS Classes

- `.masthead` - Duck logo header
- `.article-headline` - Main post title (bordered, uppercase)
- `.article-content` - Post body wrapper
- `.cta-btn` - Call-to-action buttons
- `.issue-card` - Newsletter card on homepage
- `.featured-image` - Full-width images

### Frontmatter Fields

```yaml
layout: newsletter.njk    # Required
title: "Post Title"       # Required
date: YYYY-MM-DD         # Required
subjectLine: "Text"      # Optional (defaults to "merge_conflict, NEED REVIEW")
excerpt: "Brief text"    # Optional (for homepage preview)
```

## 🎨 Customization Examples

### Change Primary Color

Edit `src/css/main.css`:
```css
:root {
  --brand-red: #YOUR_COLOR;  /* Change this */
}
```

### Modify Homepage Layout

Edit `src/index.njk` to:
- Change intro text (lines 30-42)
- Update CTA buttons (lines 82-89)
- Modify subject line (line 20)

### Adjust Post Styling

Edit `src/css/newsletter.css`:
- Article headline size (line 44)
- Content font size (line 94)
- Image borders/shadows (lines 134-138)

## 🚀 Deployment

### GitHub Pages

Already configured! Just push to main branch:

```bash
git add .
git commit -m "Update newsletter"
git push origin main
```

### Manual Build

```bash
npm run build
```

Files will be in `_site/` directory.

## 🐛 Troubleshooting

### Build fails with "filter not found"
Make sure `.eleventy.js` has all custom filters defined.

### Images not showing
- Check image paths start with `/assets/`
- Verify images exist in `src/assets/images/`
- Run `npm run build` to copy assets

### Styles not applying
- Clear browser cache
- Check CSS file is imported in layout
- Verify class names match between HTML and CSS

## 📚 Next Steps

1. **Create More Posts:** Add more `.md` files to `src/posts/`
2. **Add Email Integration:** Connect Buttondown or ConvertKit
3. **Set Up Discord:** Create server and update link
4. **Add Analytics:** Track readership
5. **Customize Content:** Make it your own!

---

**Built with ☕ and 💻**

For questions or issues, refer to the Eleventy documentation: https://www.11ty.dev/docs/

