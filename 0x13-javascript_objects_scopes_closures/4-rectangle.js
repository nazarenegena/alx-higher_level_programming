#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // creates empty object if width / height is not positive int
      this.width = 0;
      this.height = 0;
    }
  }

    print() {
        for (let i = 0; i < this.height; i++) {
            let stringToDisplay = '';
            for (let j = 0; j < this.width; j++) {
                stringToDisplay += 'X'
            }

            console.log(stringToDisplay);
        }

    }

    rotate() {
        const tempWidth = this.width;
        this.width = this.height;
        this.height = tempWidth;
  }

    double() {
        this.width *= 2;
        this.height *= 2;
  }
}

module.exports = Rectangle;

