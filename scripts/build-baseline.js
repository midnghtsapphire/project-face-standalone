const fs = require('fs');

const checks = [
  ['frontend/package.json', fs.existsSync('frontend/package.json')],
  ['backend/requirements.txt', fs.existsSync('backend/requirements.txt')],
  ['docker-compose.yml', fs.existsSync('docker-compose.yml')]
];

const failed = checks.filter(([, ok]) => !ok).map(([name]) => name);

if (failed.length) {
  console.error('Baseline build check failed. Missing:');
  for (const name of failed) console.error(`- ${name}`);
  process.exit(1);
}

console.log('Baseline build check passed: core project manifests exist.');
