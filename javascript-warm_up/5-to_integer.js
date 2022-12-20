#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!args[2]) {
  console.log('Not a number');
} else if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My nymber:', parseInt(args[2]));
}
