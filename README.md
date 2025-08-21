# Spotify Podcast API

A lightweight Django REST Framework API that interfaces with the Spotify Web API to fetch podcast data without using a database.

## Features

- Search podcasts by query
- Get detailed information about specific podcasts
- Retrieve episodes for any podcast
- OAuth 2.0 authentication with Spotify API
- Token caching for improved performance
- No database required - purely acts as a proxy to Spotify API

## Technologies Used

- Python 3.10
- Django 5
- Django REST Framework
- Poetry for dependency management
- Requests library for API calls
- Spotify Web API

## Prerequisites

- Python 3.10
- Poetry installed globally
- Spotify Developer account

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sohretaga/spotify_podcast.git
cd spotify_podcast_api
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the Poetry shell:
```bash
poetry shell
```

4. Set up environment variables:
Create a `.env` file in the project root with the following variables:
```env
SECRET_KEY=your_django_secret_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### 1. Search Podcasts
**GET** `/podcasts/search?q={query}&page={page}&page_size={page_size}`

Search for podcasts by query string with pagination support.

### 2. Get Podcast Details
**GET** `/podcasts/{showId}`

Get detailed information about a specific podcast.

### 3. Get Podcast Episodes
**GET** `/podcasts/{showId}/episodes?page={page}&page_size={page_size}`

Retrieve paginated episodes for a specific podcast.

## Pagination

All list endpoints support pagination using the following query parameters:

- `page`: Page number (default: 1)

- `page_size`: Number of items per page (default: 20, max: 50)

## Configuration

### Spotify Developer Setup

1. Create a Spotify Developer account at [developer.spotify.com](https://developer.spotify.com)
2. Create a new app in the Dashboard
3. Note your Client ID and Client Secret

### Environment Variables

All configuration is handled through environment variables:

- `SECRET_KEY`: Django secret key (required)
- `SPOTIFY_CLIENT_ID`: Your Spotify app client ID (required)
- `SPOTIFY_CLIENT_SECRET`: Your Spotify app client secret (required)

## Project Structure

```
podcasts/
    ├── migrations/
        └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── mixins.py
    ├── models.py
    ├── serializers.py
    ├── services.py
    ├── tests.py
    ├── urls.py
    └── views.py
spotify_podcast_api/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
.env.example
.gitignore
LICENSE
manage.py
poetry.lock
pyproject.toml
```

## Development

Since this project doesn't use a database:
- No migrations are needed
- No database setup is required
- All data is fetched directly from Spotify API

## Testing with Postman

1. Start the development server
2. Open Postman and test the endpoints:

```
GET http://localhost:8000/podcasts/search?q=tech
GET http://localhost:8000/podcasts/{show_id}
GET http://localhost:8000/podcasts/{show_id}/episodes
```
