#!/usr/bin/node
import * as fs from 'node:fs';
import * as fs from 'node:fs/promises';
// writing a script that reads & prints file contents.
const fs = require('fs').promises;

let filePath = 'file_path.txt';

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
            console.error(`Error reading the file: ${err}`);
    } else
    {
       console.log(data) 
        }
})
