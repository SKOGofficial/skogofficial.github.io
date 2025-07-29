const fs = require('fs');
const path = require('path');

// Read the projects.json file
const projectsPath = path.join(__dirname, '../projects.json');
const projectsData = JSON.parse(fs.readFileSync(projectsPath, 'utf8'));

module.exports = projectsData; 