#!/usr/bin/node
const dict = {};
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    for (const each in response.data) {
      if (response.data[each].completed === true) {
        if (dict[response.data[each].userId] === undefined) {
          dict[response.data[each].userId] = 1;
        } else {
          dict[response.data[each].userId] += 1;
        }
      }
    }
    console.log(dict);
  });
