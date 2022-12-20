#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  a = parseInt(args[2]);
  b = parseInt(args[3]);
  return a + b;
}

console.log(add());
