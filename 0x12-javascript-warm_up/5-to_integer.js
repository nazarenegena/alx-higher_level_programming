#!/usr/bin/node
let myNumber = Math.floor(Number(process.argv[0]));
if (isNaN(myNumber)) {
    console.log('Not a number');
}
else
{
    console.log(`My number: ${myNumber}`)
}
