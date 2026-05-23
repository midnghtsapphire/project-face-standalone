const fs = require('fs');
const path = require('path');

const requiredFiles = [
  'README.md',
  'CHANGELOG.md',
  'DEPLOYMENT_GUIDE.md',
  'GO_TO_MARKET.md',
  'BRAND_GUIDELINES.md',
  'SECURITY.md',
  'package.json',
  path.join('scripts', 'test-baseline.js'),
  path.join('scripts', 'build-baseline.js')
];

const missing = requiredFiles.filter((file) => !fs.existsSync(path.resolve(file)));

if (missing.length) {
  console.error('Missing revvel-standards baseline files:');
  for (const file of missing) console.error(`- ${file}`);
  process.exit(1);
}

console.log('Baseline test passed: required revvel-standards files are present.');
