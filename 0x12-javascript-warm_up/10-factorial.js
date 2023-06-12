#!/usr/bin/node
function factorial(val) {
  if (isNaN(val)) {
    return 1;
  } 
  if (val === 0 || val === 1) {
    return 1;
  } 
  return val * factorial(val - 1);
}
const number = parseInt(process.argv[2]);

console.log(factorial(number));
