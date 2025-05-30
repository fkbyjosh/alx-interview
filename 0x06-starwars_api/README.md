# 0x06. Star Wars API

This project contains a Node.js script that fetches and displays characters from Star Wars movies using the Star Wars API (SWAPI).

## Description

The script `0-starwars_characters.js` takes a movie ID as a command-line argument and prints all characters from that specific Star Wars film. The characters are displayed in the same order as they appear in the API response.

## Requirements

- Ubuntu 20.04 LTS
- Node.js (version 10.14.x)
- npm (Node Package Manager)
- `request` module

## Installation

1. **Install Node.js and npm** (if not already installed):
   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install the request module**:
   ```bash
   npm install request
   ```

3. **Make the script executable**:
   ```bash
   chmod +x 0-starwars_characters.js
   ```

## Usage

```bash
./0-starwars_characters.js <movie_id>
```

### Parameters
- `movie_id`: The ID of the Star Wars movie (1-6)

### Movie IDs
- 1: A New Hope
- 2: The Empire Strikes Back
- 3: Return of the Jedi
- 4: The Phantom Menace
- 5: Attack of the Clones
- 6: Revenge of the Sith

## Example

```bash
./0-starwars_characters.js 3
```

**Output:**
```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## How it Works

1. The script accepts a movie ID as a command-line argument
2. Makes an HTTP request to the Star Wars API films endpoint: `https://swapi-api.alx-tools.com/api/films/{movie_id}/`
3. Extracts the character URLs from the film data
4. Fetches each character's information in the correct order
5. Displays each character's name on a separate line

## API Endpoint

The script uses the Star Wars API (SWAPI):
- Base URL: `https://swapi-api.alx-tools.com/api/`
- Films endpoint: `/films/{id}/`
- People endpoint: `/people/{id}/`

## Error Handling

The script includes error handling for:
- Missing command-line arguments
- HTTP request failures
- Invalid movie IDs
- Network connectivity issues

## Files

- `0-starwars_characters.js`: Main script file
- `README.md`: This documentation file

## Author

Joshua Baka

## Repository

- **GitHub repository**: `alx-interview`
- **Directory**: `0x06-starwars_api`
- **File**: `0-starwars_characters.js`
