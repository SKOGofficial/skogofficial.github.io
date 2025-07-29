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
  
  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts"
    }
  };
}; 