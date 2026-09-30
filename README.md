# skogofficial.github.io

Personal site for Soham Nawthale, built with [Eleventy](https://www.11ty.dev/) and deployed to GitHub Pages.

## Develop

```bash
npm install
npm run serve
```

The site is served at <http://localhost:8080>. `npm run build` writes the static output to `_site/`.

## Structure

- `src/_layouts/` — `base.njk` (header, footer, metadata) and `page.njk` (narrow prose pages).
- `src/_data/` — `site.json` for name and links, `projects.json` for the projects list, `redirects.json` for old URLs.
- `src/*.njk` — one file per page. `src/research/` holds the research write-ups.
- `src/css/site.css` — the only stylesheet. No JavaScript is shipped.

## Deploy

Pushes to `main` run `.github/workflows/static.yml`, which builds the site and publishes `_site/` to GitHub Pages.
