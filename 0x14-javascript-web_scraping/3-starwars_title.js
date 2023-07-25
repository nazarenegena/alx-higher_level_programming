#!/usr/bin/node
const req = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const episodeNum = process.argv[2];

req(API_URL + episodeNum, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
