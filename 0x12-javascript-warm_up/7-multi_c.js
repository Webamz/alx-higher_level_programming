#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg) || arg === undefined) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('C is fun');
  }
}
