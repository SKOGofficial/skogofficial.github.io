module.exports = function(eleventyConfig) {
  // Copy static assets (relative to input directory)
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/js");
  
  // Add data files
  eleventyConfig.addDataExtension("json", function(contents) {
    return JSON.parse(contents);
  });
  
  // Add custom filter for grouping
  eleventyConfig.addFilter("groupBy", function(array, key) {
    const groups = {};
    array.forEach(item => {
      const groupKey = item[key];
      if (!groups[groupKey]) {
        groups[groupKey] = [];
      }
      groups[groupKey].push(item);
    });
    return groups;
  });
  
  // Add date filter for newsletter posts
  eleventyConfig.addFilter("readableDate", function(dateObj) {
    return new Date(dateObj).toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    });
  });
  
  // Add limit filter for truncating arrays
  eleventyConfig.addFilter("limit", function(array, limit) {
    return array.slice(0, limit);
  });
  
  // Add slugify filter for URLs
  eleventyConfig.addFilter("slugify", function(str) {
    return str
      .toLowerCase()
      .replace(/[^\w\s-]/g, '')
      .replace(/[\s_-]+/g, '-')
      .replace(/^-+|-+$/g, '');
  });
  
  // Create newsletter posts collection
  eleventyConfig.addCollection("newsletter", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/posts/*.md").reverse();
  });
  
  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts"
    },
    markdownTemplateEngine: "njk"
  };
}; 