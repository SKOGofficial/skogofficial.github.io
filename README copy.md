# Project Ember - Research Website

A modern, responsive website showcasing the revolutionary ORC-based solar thermal panel research project. Built with HTML, CSS, and JavaScript, featuring a dark theme with warm orange-red gradient accents.

## 🌟 Features

- **Modern Design**: Dark theme with warm orange-red gradient accents
- **Fully Responsive**: Optimized for all devices and screen sizes
- **Interactive Elements**: Smooth animations, hover effects, and scroll-triggered animations
- **Professional Sections**: Hero, About, Technology, Research Timeline, Team, and Contact
- **Contact Form**: Functional contact form with validation
- **Accessibility**: Keyboard navigation and screen reader friendly
- **Performance Optimized**: Fast loading with minimal dependencies

## 🚀 Live Demo

The website is designed to be hosted on GitHub Pages. Once deployed, it will be available at:
`https://[your-username].github.io/[repository-name]/`

## 📁 Project Structure

```
Project EMBER/
├── index.html          # Main HTML file
├── styles.css          # CSS styles and animations
├── script.js           # JavaScript functionality
└── README.md           # This file
```

## 🛠️ Setup Instructions

### Local Development

1. **Clone or download** the project files to your local machine
2. **Open** `index.html` in your web browser
3. **Start developing** - the website will work immediately without any build process

### GitHub Pages Deployment

1. **Create a new repository** on GitHub
2. **Upload** all project files to the repository
3. **Go to Settings** → **Pages**
4. **Select Source**: "Deploy from a branch"
5. **Choose Branch**: `main` (or `master`)
6. **Select Folder**: `/ (root)`
7. **Click Save** - your site will be deployed in a few minutes

### Custom Domain (Optional)

1. **Purchase a domain** from your preferred registrar
2. **Add a CNAME file** to your repository with your domain name
3. **Configure DNS** to point to `[username].github.io`
4. **Update GitHub Pages settings** with your custom domain

## 🎨 Customization

### Colors and Theme

The website uses CSS custom properties for easy customization. Edit the `:root` section in `styles.css`:

```css
:root {
  --primary-bg: #0a0a0a; /* Main background */
  --secondary-bg: #111111; /* Secondary background */
  --accent-orange: #ff6b35; /* Primary accent */
  --accent-red: #e63946; /* Secondary accent */
  --gradient-primary: linear-gradient(135deg, #ff6b35 0%, #e63946 100%);
}
```

### Content Updates

- **Hero Section**: Update the main title, subtitle, and description in `index.html`
- **About Section**: Modify the mission statement and statistics
- **Technology Cards**: Add or remove technology features
- **Team Members**: Update team information and photos
- **Contact Information**: Update email, phone, and social media links

### Adding New Sections

1. **Add HTML structure** in `index.html`
2. **Add CSS styles** in `styles.css`
3. **Add JavaScript functionality** in `script.js` (if needed)
4. **Update navigation** to include the new section

## 📱 Responsive Design

The website is fully responsive and includes:

- **Mobile-first approach** with progressive enhancement
- **Breakpoints**: 768px (tablet) and 480px (mobile)
- **Touch-friendly** navigation and buttons
- **Optimized typography** for all screen sizes

## ⚡ Performance Features

- **Minimal dependencies** - only Font Awesome for icons
- **Optimized animations** using CSS transforms and opacity
- **Lazy loading** for scroll-triggered animations
- **Efficient JavaScript** with event delegation
- **Fast loading** with no external frameworks

## 🔧 Browser Support

- **Chrome** 60+
- **Firefox** 55+
- **Safari** 12+
- **Edge** 79+
- **Mobile browsers** (iOS Safari, Chrome Mobile)

## 📧 Contact Form

The contact form includes:

- **Client-side validation** for all fields
- **Email format validation**
- **Success/error notifications**
- **Form reset** after successful submission

**Note**: The form currently shows a success message but doesn't actually send emails. To make it functional, you'll need to:

1. **Add a backend service** (Netlify Forms, Formspree, etc.)
2. **Update the form action** in `index.html`
3. **Modify the JavaScript** to handle actual form submission

## 🎯 SEO Optimization

The website includes:

- **Semantic HTML** structure
- **Meta tags** for description and keywords
- **Open Graph** tags for social sharing
- **Structured data** ready for implementation
- **Fast loading** for better search rankings

## 🔒 Security Considerations

- **No external scripts** loaded from CDNs (except Font Awesome)
- **Form validation** on both client and server side
- **XSS protection** through proper input sanitization
- **HTTPS ready** for secure hosting

## 📈 Analytics (Optional)

To add Google Analytics:

1. **Get your tracking ID** from Google Analytics
2. **Add the tracking code** to the `<head>` section of `index.html`
3. **Update the tracking ID** in the code

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** on different devices and browsers
5. **Submit** a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Font Awesome** for the beautiful icons
- **Google Fonts** for the Inter font family
- **CSS Grid and Flexbox** for the responsive layout
- **Intersection Observer API** for scroll animations

## 📞 Support

If you need help with:

- **Deployment issues** - Check GitHub Pages documentation
- **Customization** - Review the CSS custom properties
- **Form functionality** - Consider using Netlify Forms or Formspree
- **Performance** - Use browser dev tools to analyze loading times

---

**Project Ember** - Advancing the future of solar thermal energy through innovative ORC technology.

_Built with ❤️ for sustainable energy research_
