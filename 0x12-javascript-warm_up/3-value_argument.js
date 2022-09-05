#!/usr/bin/node
const myVar = process.argv[1];
const argLength = process.argv.length;
if (argLength < 3) {
  console.log ('No argument');
else {
  console.log (myVar)
