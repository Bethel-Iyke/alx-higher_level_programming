#!/usr/bin/node
/*
    Prints the two argument
    passed to it
*/
function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
