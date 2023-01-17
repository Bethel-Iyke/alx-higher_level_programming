#!/usr/bin/node

const fs = require('fs')
const file = process.argv[2];
const finput = process.argv[3];

fs.writeFile(file, finput, 'utf-8', function(err) {
	if (err) console.log(err);
});
