#!/usr/bin/node

exports.converter = function (base) {
  return function (newNumber) {
    return newNumber.toString(base);
  };
};
