#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const h = this.height;
    const w = this.width;
    this.height = w;
    this.width = h;
  }

  double () {
    const h = this.height * 2;
    const w = this.width * 2;
    this.height = h;
    this.width = w;
  }
};
