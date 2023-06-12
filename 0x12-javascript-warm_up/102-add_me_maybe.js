#!/usr/bin/node
const incrementAndCall = (number, theFunction) => {
  number++;
  theFunction(number);
};
module.exports = incrementAndCall;
