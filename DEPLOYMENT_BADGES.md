# Deployment Status Badges

You can add these badges to your main README.md file to show deployment status:

## GitHub Pages Status

```markdown
![Deploy to GitHub Pages](https://github.com/[username]/[repository-name]/actions/workflows/static.yml/badge.svg)
```

Replace `[username]` and `[repository-name]` with your actual GitHub username and repository name.

## Example

For a repository named `skogofficial.github.io` owned by `skogofficial`:

```markdown
![Deploy to GitHub Pages](https://github.com/skogofficial/skogofficial.github.io/actions/workflows/static.yml/badge.svg)
```

## Other Useful Badges

### Node.js Version
```markdown
![Node.js](https://img.shields.io/badge/node-18.x-brightgreen)
```

### Eleventy Version
```markdown
![Eleventy](https://img.shields.io/badge/eleventy-3.1.2-blue)
```

### License
```markdown
![License](https://img.shields.io/badge/license-ISC-green)
```

## Complete Example

```markdown
# Your Project Name

![Deploy to GitHub Pages](https://github.com/[username]/[repository-name]/actions/workflows/static.yml/badge.svg)
![Node.js](https://img.shields.io/badge/node-18.x-brightgreen)
![Eleventy](https://img.shields.io/badge/eleventy-3.1.2-blue)
![License](https://img.shields.io/badge/license-ISC-green)

Your project description here...
```

## Badge Colors

- **Green**: Success/Passing
- **Red**: Failed/Error
- **Yellow**: Warning/Pending
- **Blue**: Information
- **Gray**: Unknown/Neutral 