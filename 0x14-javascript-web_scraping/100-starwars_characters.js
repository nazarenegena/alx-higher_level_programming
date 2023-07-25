#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const dataFile = JSON.parse(body);
  const dd = dataFile.characters;
  for (const i of dd) {
    request.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dataFile1 = JSON.parse(body1);
      console.log(dataFile1.name);
    });
  }
});
