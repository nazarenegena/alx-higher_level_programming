#!/usr/bin/node
let myNumber = process.argv[0];

if (isNaN(Number(myNumber))) {

    console.log('Not a number')
}
