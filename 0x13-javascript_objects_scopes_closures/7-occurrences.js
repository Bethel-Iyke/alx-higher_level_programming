#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const x = list.length;
  let count = 0;
  for (let i = 0; i < x; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
