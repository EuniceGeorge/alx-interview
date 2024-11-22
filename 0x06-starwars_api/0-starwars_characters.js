#!/usr/bin/node
// script that prints all the characters of a Star Wars movie:

const request = require('request');

const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const getMovieCharacters = (movieId) => {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characters = JSON.parse(body).characters;
        resolve(characters);
      }
    });
  });
};

const printCharacters = async (movieId) => {
  try {
    const characters = await getMovieCharacters(movieId);

    for (const character of characters) {
      const characterName = await getCharacterName(character);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
};

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command line argument.');
} else {
  printCharacters(movieId);
}
