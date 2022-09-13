#!/usr/bin/node
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    const content = response.data;
    const fs = require('fs');
    fs.writeFileSync(process.argv[3], content, err => {
      if (err) {
        console.log(err);
      }
    });
  });
