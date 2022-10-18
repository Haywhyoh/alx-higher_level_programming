#!/usr/bin/node
/*
reads a file and prints the contents
*/
const fs = require('fs')
const file = process.argv[2]
fs.readFile(file, 'uf8', (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  console.log(data)
})
