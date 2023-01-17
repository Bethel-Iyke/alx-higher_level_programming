#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url, function (err, response, body) {
  if (err) console.error(err); else {
    const jsonbody = JSON.parse(body);
    console.log(jsonbody.title);
  }
});
