# GitHub Pages Deployment Setup

This repository is configured to automatically deploy to GitHub Pages using GitHub Actions.

## How it works

1. **Automatic Deployment**: When you push to the `main` or `master` branch, GitHub Actions automatically:
   - Installs Node.js and dependencies
   - Builds the Eleventy site
   - Deploys to GitHub Pages

2. **Workflow File**: `.github/workflows/static.yml` contains the deployment configuration

## Setup Instructions

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. Save the changes

### 2. Repository Settings

Make sure your repository has the following settings:

- **Repository name**: `skogofficial.github.io` (for custom domain) or any name
- **Branch**: `main` or `master` (whichever you're using)
- **GitHub Pages source**: GitHub Actions

### 3. Permissions

The workflow automatically requests the necessary permissions:
- `contents: read` - to read repository content
- `pages: write` - to deploy to GitHub Pages
- `id-token: write` - for authentication

## Deployment Process

### What happens on each push:

1. **Checkout**: Clones your repository
2. **Setup Node.js**: Installs Node.js 18 with npm caching
3. **Install Dependencies**: Runs `npm ci` to install packages
4. **Build Site**: Runs `npm run build` to generate the site
5. **Upload Artifact**: Uploads the `_site` directory as a Pages artifact
6. **Deploy**: Deploys the site to GitHub Pages

### Build Output

The workflow builds your Eleventy site and deploys:
- **Main site**: Your homepage and existing pages
- **Project pages**: All 19 individual project pages
- **Projects index**: The main projects listing page
- **Assets**: CSS, JavaScript, and images

## Custom Domain (Optional)

If you have a custom domain:

1. Add your domain to the workflow file:
   ```yaml
   - name: Deploy to GitHub Pages
     uses: actions/deploy-pages@v4
     with:
       cname: yourdomain.com
   ```

2. Configure DNS settings in your domain provider
3. Add the domain in GitHub repository settings

## Troubleshooting

### Common Issues:

1. **Build fails**: Check the Actions tab for error logs
2. **Site not updating**: Wait a few minutes for deployment to complete
3. **404 errors**: Ensure all file paths are correct
4. **Styling issues**: Check that CSS files are being copied correctly

### Manual Deployment:

You can manually trigger deployment:
1. Go to **Actions** tab
2. Select **Deploy static content to Pages**
3. Click **Run workflow**

## File Structure

```
.github/
└── workflows/
    └── static.yml          # GitHub Actions workflow

src/
├── _layouts/              # Eleventy layouts
├── _data/                 # Data files
├── projects.json          # Project data
└── *.njk                  # Templates

_site/                     # Built site (excluded from git)
├── projects/              # Individual project pages
├── projects/              # Projects listing
├── css/                   # Stylesheets
├── js/                    # JavaScript
└── assets/                # Images and other assets
```

## URLs

After deployment, your site will be available at:
- **Main site**: `https://[username].github.io/[repository-name]/`
- **Projects**: `https://[username].github.io/[repository-name]/projects/[project-name]/`
- **Projects index**: `https://[username].github.io/[repository-name]/projects/`

For a repository named `skogofficial.github.io`, the site will be at:
- `https://skogofficial.github.io/`

## Monitoring

- **Actions tab**: View deployment status and logs
- **Pages tab**: Check deployment history and settings
- **Repository insights**: Monitor deployment frequency

The site will automatically rebuild and deploy whenever you push changes to the main branch! 