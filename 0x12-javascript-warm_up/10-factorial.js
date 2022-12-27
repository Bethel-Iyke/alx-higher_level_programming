#!/usr/bin/node
/*
    Prints the two argument
    passed to it
*/
function factorial (a) {
  if (isNaN(a)) {
    console.log(1);
    process.exit(1);
  }
  if (a === 0) { return 1; }
  return (a * factorial(a - 1));
}
console.log(factorial(parseInt(process.argv[2])));
