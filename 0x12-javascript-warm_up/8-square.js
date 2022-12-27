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

if (process.argv.length <= 2 || checkArg(process.argv[2], 10) === 0) {
  console.log('Missing size');
  process.exit(1);
} else {
  const x = checkArg(process.argv[2], 10);
  let i = 0;
  let j = 0;
  let pattern = '';
  while (i < x) {
    while (j < x) {
      pattern += 'X';
      j++;
    }
    console.log(pattern);
    i++;
  }
}
