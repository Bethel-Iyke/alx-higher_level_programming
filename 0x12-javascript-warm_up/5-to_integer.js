#!/usr/bin/node
/*
    Prints the two argument
    passed to it
*/
function checkArg (x, base) {
  const number = parseInt(x, base);
  if (isNaN(number)) { return 0; }
  return number;
}

if (process.argv.length <= 2) {
  console.log('Not a number');
  process.exit(1);
}

if (checkArg(process.argv[2], 10) === 0) {
  console.log('Not a number');
  process.exit(1);
} else {
  console.log('My number:', checkArg(process.argv[2], 10));
}
