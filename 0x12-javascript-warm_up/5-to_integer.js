#!/usr/bin/node
const inputInt = parseInt(process.argv[2]);
if (isNaN(inputInt)) {
  console.log('Not a number');
} else {
  console.log(inputInt);
}
