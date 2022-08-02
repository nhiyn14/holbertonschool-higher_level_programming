#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const liSt = [];
  let x = 0;
  for (let i = list.length - 1; i > -1; i--) {
    liSt[x] = list[i];
    x += 1;
  }
  list = liSt;
  return list;
};
