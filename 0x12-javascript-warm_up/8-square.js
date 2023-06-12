#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg) || arg === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('X'.repeat(arg));
  }
}
