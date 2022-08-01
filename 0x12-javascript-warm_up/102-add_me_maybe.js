#!/usr/bin/node
// increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  return theFunction(number + 1);
};
