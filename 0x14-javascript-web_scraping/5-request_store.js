#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.error(err);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', function (error, result) { if (error) console.log(error); });
  } catch (error) {
    console.log(error);
  }
});
