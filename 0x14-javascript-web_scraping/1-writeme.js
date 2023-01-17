#!/usr/bin/node
'use strict';

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
