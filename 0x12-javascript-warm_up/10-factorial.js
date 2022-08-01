#!/usr/bin/node
// computes and prints a factorial

function factorialize (num) {
  if (isNaN(num) || num === 0) { return 1; }
  if (num < 0) { return; }
  return (num * factorialize(num - 1));
}

console.log(factorialize(parseInt(process.argv[2])));
