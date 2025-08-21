import requests
import base64
from django.conf import settings
from django.core.cache import cache


class SpotifyClient:
    TOKEN_CACHE_KEY = "spotify_token"

    def __init__(self):
        self.client_id = settings.SPOTIFY_CLIENT_ID
        self.client_secret = settings.SPOTIFY_CLIENT_SECRET
        self.token_url = settings.SPOTIFY_TOKEN_URL
        self.api_base = settings.SPOTIFY_API_BASE_URL

    def _get_token_from_api(self) -> str:
        """Gets a new access token from the Spotify API"""
        auth_header = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode()

        response = requests.post(
            self.token_url,
            headers={"Authorization": f"Basic {auth_header}"},
            data={"grant_type": "client_credentials"}
        )
        response.raise_for_status()
        data = response.json()
        token = data.get("access_token")

        # Cache the token for future use
        cache.set(self.TOKEN_CACHE_KEY, token, timeout=data.get("expires_in", 3500))
        return token

    def get_token(self) -> str:
        """Retrieves the token from the cache, if not found, gets a new one"""
        token = cache.get(self.TOKEN_CACHE_KEY)
        if token:
            return token
        return self._get_token_from_api()

    def get(self, endpoint: str, params: dict = None) -> dict:
        """Spotify API GET requestSpotify API GET request"""
        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{self.api_base}/{endpoint}", headers=headers, params=params
        )
        response.raise_for_status()
        return response.json()
