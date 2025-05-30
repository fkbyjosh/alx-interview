#!/usr/bin/node

const request = require('request');

// Get movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Star Wars API endpoint for films
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to make HTTP request and return a promise
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`HTTP ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Main function to fetch and display characters
async function getCharacters () {
  try {
    // Get film data
    const filmData = await makeRequest(filmUrl);

    // Get character URLs from the film
    const characterUrls = filmData.characters;

    // Fetch each character's data in order and print names
    for (const characterUrl of characterUrls) {
      try {
        const characterData = await makeRequest(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        console.error(`Error fetching character: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching film data: ${error.message}`);
    process.exit(1);
  }
}

// Run the script
getCharacters();
