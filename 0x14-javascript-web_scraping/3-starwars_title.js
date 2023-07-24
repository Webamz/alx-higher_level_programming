#!/usr/bin/node

const request = require('request');

const episode = process.argv[2];

if (parseInt(episode) < 8) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
