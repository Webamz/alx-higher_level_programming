#!/usr/bin/node

const dataList = require('./100-data.js').list;
console.log(dataList);

const newList = dataList.map((x, i) => x * i);
console.log(newList);
