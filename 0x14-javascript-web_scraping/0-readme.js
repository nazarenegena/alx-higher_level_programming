#!/usr/bin/node
const fsFile = require('fs');
fsFile.readFile(process.argv[2], 'utf8', function (error, data) {
  console.log(error || data);
});
