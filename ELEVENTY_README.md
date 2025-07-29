# Eleventy Project Pages Generator

This project uses Eleventy (11ty) to automatically generate individual web pages for each project from a JSON data file.

## What was accomplished:

1. **Installed Eleventy**: Set up Eleventy as a static site generator
2. **Created JSON Data**: Extracted all projects from `projects.html` into `src/projects.json`
3. **Generated Individual Pages**: Created 19 individual project pages, one for each project
4. **Created Project Index**: Built a main projects page that lists all projects by category
5. **Added Styling**: Enhanced the CSS with modern, responsive design for project pages

## Project Structure:

```
src/
├── _layouts/
│   ├── base.njk          # Base layout template
│   └── project.njk       # Project-specific layout
├── _data/
│   └── projects.js       # Data loader for projects.json
├── projects.json         # All project data
├── project-pages.njk     # Template for individual project pages
└── projects.html         # Static projects listing page
```

## Generated Pages:

### Individual Project Pages (19 total):

- `/projects/street-fighter-(vthacks-2023)/`
- `/projects/musical-stocks-(hack-violet-2023)/`
- `/projects/safewalk-(patriot-hacks-2024)/`
- `/projects/roi-bot-(hoo-hacks-2023)/`
- `/projects/hokie-feast-(hackviolet-2024)/`
- `/projects/water-4-chad-(hoohacks-2025)/`
- `/projects/personal-server-(systems-fall-2024)/`
- `/projects/threadpool-(systems-fall-2024)/`
- `/projects/memory-allocator-(systems-fall-2024)/`
- `/projects/night-island-(mixed-reality-2025)/`
- `/projects/escape-room-(mixed-reality-2025)/`
- `/projects/ar-basketball-(mixed-reality-2025)/`
- `/projects/ar-golf-(mixed-reality-2025)/`
- `/projects/moodmuse-(apple-sd-2025)/`
- `/projects/neural-network-(dec-2022-jan-2023)/`
- `/projects/signlink-(mar-2024-present)/`
- `/projects/hogback-(mar-2023-jan-2024)/`
- `/projects/private-tutor-(jun-2024-present)/`
- `/projects/online-furniture-sales-(2020-2022)/`

### Projects Index Page:

- `/projects/` - Lists all projects organized by category

## Categories:

1. **Hackathon Projects** (6 projects)
2. **School Projects** (8 projects)
3. **Personal Projects** (5 projects)

## Features:

- **Responsive Design**: Works on desktop and mobile
- **Modern UI**: Clean, professional styling with hover effects
- **Skill Tags**: Each project displays its skills as interactive tags
- **Navigation**: Easy navigation between projects and back to index
- **Clickable Project Titles**: All project titles in `projects.html` are now clickable links that lead to their detailed Eleventy-generated pages
- **SEO Friendly**: Each page has proper titles and meta tags

## Commands:

```bash
# Build the site
npm run build

# Start development server
npm run serve
```

## Data Structure:

Each project in the JSON file contains:

- `project category`: The category (Hackathon/School/Personal Projects)
- `project title`: The name of the project
- `project description`: Detailed description of the project
- `project skills`: Comma-separated list of skills and technologies

## Technologies Used:

- **Eleventy (11ty)**: Static site generator
- **Nunjucks**: Templating engine
- **CSS3**: Modern styling with CSS Grid and Flexbox
- **Font Awesome**: Icons
- **JavaScript**: For data processing and interactivity

## Files Added:

- **`.gitignore`**: Excludes `node_modules/`, `_site/`, and other common files from version control
- **Updated `projects.html`**: All project titles are now clickable links to their detailed pages
- **Enhanced CSS**: Added styling for project title links with hover effects
- **GitHub Actions**: Automated deployment to GitHub Pages (see `GITHUB_PAGES_README.md`)

## Deployment

The site is configured for automatic deployment to GitHub Pages:

1. **Local Development**: `npm run serve` (runs on http://localhost:8080)
2. **Production Build**: `npm run build` (creates `_site/` directory)
3. **GitHub Pages**: Automatically deploys when you push to main/master branch

See `GITHUB_PAGES_README.md` for detailed deployment instructions.

The site is now ready to be deployed and provides a professional showcase for all your projects!
