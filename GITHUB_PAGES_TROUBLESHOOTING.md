# GitHub Pages Deployment Troubleshooting

## Error: "Write access to repository not granted" (403)

This error occurs when the GitHub Actions workflow doesn't have the proper permissions to deploy to GitHub Pages.

## Solution Steps:

### 1. Enable GitHub Pages in Repository Settings

1. Go to your repository on GitHub: `https://github.com/SKOGofficial/skogofficial.github.io`
2. Click on **Settings** tab
3. Scroll down to **Pages** section (in the left sidebar)
4. Under **Source**, select **GitHub Actions**
5. Click **Save**

### 2. Check Repository Permissions

1. In the same **Settings** page
2. Go to **Actions** → **General** (in the left sidebar)
3. Under **Workflow permissions**, make sure:
   - ✅ **Read and write permissions** is selected
   - ✅ **Allow GitHub Actions to create and approve pull requests** is checked
4. Click **Save**

### 3. Verify Workflow File

Make sure you only have one workflow file: `.github/workflows/static.yml`

The workflow should use the modern GitHub Pages deployment method (not the old `peaceiris/actions-gh-pages`).

### 4. Check Branch Name

Make sure your main branch is named either `main` or `master`. The workflow is configured for both:

```yaml
on:
  push:
    branches: ["main", "master"]
```

### 5. Manual Trigger (if needed)

If the automatic deployment isn't working:

1. Go to **Actions** tab in your repository
2. Click on **Deploy static content to Pages**
3. Click **Run workflow**
4. Select your branch and click **Run workflow**

## Expected Workflow Output:

When working correctly, you should see:

```
✓ Checkout
✓ Setup Node.js
✓ Install dependencies
✓ Build with Eleventy
✓ Setup Pages
✓ Upload artifact
✓ Deploy to GitHub Pages
```

## Common Issues:

### Issue 1: Multiple Workflow Files

**Problem**: Having both old and new workflow files
**Solution**: Keep only `.github/workflows/static.yml`

### Issue 2: Wrong Permissions

**Problem**: Repository doesn't allow Actions to write
**Solution**: Enable "Read and write permissions" in Settings → Actions → General

### Issue 3: GitHub Pages Not Enabled

**Problem**: GitHub Pages source not set to "GitHub Actions"
**Solution**: Set source to "GitHub Actions" in Settings → Pages

### Issue 4: Branch Name Mismatch

**Problem**: Main branch has different name
**Solution**: Update workflow file to match your branch name

## Verification:

After fixing the issues:

1. **Push a small change** to trigger the workflow
2. **Check Actions tab** for successful deployment
3. **Visit your site** at `https://skogofficial.github.io/`
4. **Test the new pages**:
   - `https://skogofficial.github.io/projects/`
   - `https://skogofficial.github.io/projects/street-fighter-(vthacks-2023)/`

## If Still Having Issues:

1. Check the **Actions** tab for detailed error logs
2. Verify all files are committed and pushed
3. Try manually triggering the workflow
4. Check repository settings for any restrictions

The most common cause is not having GitHub Pages enabled with "GitHub Actions" as the source.
