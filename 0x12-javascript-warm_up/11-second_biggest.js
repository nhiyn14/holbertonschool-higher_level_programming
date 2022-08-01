#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const liSt = process.argv.slice(2);
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  liSt.sort();
  console.log(liSt[liSt.length - 2]);
}
