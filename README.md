# Zip Info API

This is a Flask API developed by [𝐌𝐀𝐓𝐑𝐈𝐗] (@VZR7X) for retrieving information about post offices based on a given Indian zip code. The API scrapes data from an external website and provides responses in either JSON or plain text format.

## Features
- Retrieves post office information for a specified zip code.
- Provides responses in JSON and plain text formats.

## Endpoints

### `/zipinfo`
- **Method**: GET
- **Parameters**:
  - `zipcode` (required): The zip code for which you want to fetch post office details.
  - `format` (optional): Format of the response (`json` or `txt`). Defaults to `json`.

- **Example**:
  - `GET /zipinfo?zipcode=110001&format=json