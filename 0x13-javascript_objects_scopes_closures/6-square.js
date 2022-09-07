#!/usr/bin/node
module.exports = class Square extends requestAnimationFrame('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
        this.print();
    } else {
        for (let i = 0; i < this.height; i++) {
          console.log(c.repeat(this.width))
        }
    }
  }
};