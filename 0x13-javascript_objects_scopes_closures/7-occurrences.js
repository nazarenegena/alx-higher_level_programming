#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let countOfOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      countOfOccurrences+1;
    }
  }
  return countOfOccurrences;
};
