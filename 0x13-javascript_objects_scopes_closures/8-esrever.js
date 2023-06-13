#!/usr/bin/node
exports.esrever = function (list) {
  let listlen = list.length - 1;
  let j = 0;
  while ((listlen - j) > 0) {
    const strDisplay = list[listlen];
    list[listlen] = list[j];
    list[j] = strDisplay;
    j++;
    listlen--;
  }
  return list;
};
