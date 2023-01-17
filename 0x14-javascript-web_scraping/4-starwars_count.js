
#!/usr/bin/node
// script prints the number of movies where
// the character "Wedge Antilles" is present

const req = require('request');
const url = process.argv[2];

req.get(url,
  function (err, response, body) {
    if (err) console.error(err); else {
      const jsonBody = JSON.parse(body);
      const results = jsonBody.results;
      let count = 0;
      results.forEach(function (movie, idx) {
        const characters = movie.characters;
        characters.forEach(function (character, idx) {
          if (character.includes('18')) {
            count++;
          }
        });
      });
      console.log(count);
    }
  });
#!/usr/bin/node

'strict mode';

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
