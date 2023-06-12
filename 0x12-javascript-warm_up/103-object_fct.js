#!/usr/bin/node
const inc = (number) => {
  return number + 1;
};
const incrementAndCall = (number, theFunction) => {
  const incrementedNumber = inc(number);
  theFunction(incrementedNumber);
};
module.exports = { incrementAndCall, inc };
