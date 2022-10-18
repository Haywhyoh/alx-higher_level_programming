#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');
let id = process.argv[2];
const url =  'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let json_file = JSON.parse(body);
    console.log(json_file.title);
  }
});
