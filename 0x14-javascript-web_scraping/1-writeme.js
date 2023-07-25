#!/usr/bin/node
const fsFile = require('fs');
fsFile.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
