#!/usr/bin/node
const SquareSpace = require('./5-square');

class Square extends SquareSpace {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let strToDisplay = '';
      for (let k = 0; k < this.width; k++) {
        strToDisplay += c;
      }
      console.log(strToDisplay);
    }
  }
}

module.exports = Square;
