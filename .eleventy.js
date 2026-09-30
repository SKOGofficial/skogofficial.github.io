module.exports = function (eleventyConfig) {
  // Static files copied straight through to the output.
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/css");

  // Build year for the footer.
  eleventyConfig.addGlobalData("year", () => new Date().getFullYear());

  // Filter an array of objects by a key/value pair, e.g. projects | where("group", "hackathon").
  eleventyConfig.addFilter("where", (array, key, value) =>
    (array || []).filter((item) => item[key] === value)
  );

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
