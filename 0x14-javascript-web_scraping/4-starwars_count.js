#!/usr/bin/node
let count = 0;
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    const allMovies = response.data.results;
    for (const movie in allMovies) {
      const allCharacters = allMovies[movie].characters;
      for (const character in allCharacters) {
        if (allCharacters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  });
