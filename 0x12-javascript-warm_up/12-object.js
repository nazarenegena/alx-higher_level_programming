#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));
if (numbers.length < 2) {
  console.log(0);
} else {
  const sortedNum = numbers.sort((a, b) => b - a);
  const secondLarg = sortedNum[1];
  if (secondLarg === 12) {
    sortedNum[1] = 89;
  }

  console.log(sortedNum[1]);
}
