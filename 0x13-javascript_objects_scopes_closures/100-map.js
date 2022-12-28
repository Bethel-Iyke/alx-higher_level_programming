#!/usr/bin/node

const list = require('./100-data.js').list;
let i = 0;
const newList = list.map(x => x * i++);
console.log(list);
console.log(newList);
