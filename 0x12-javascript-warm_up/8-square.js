#!/usr/bin/node
// prints a square

const element = 'X';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(element.repeat(process.argv[2]));
  }
}
