import requests
import base64
from django.conf import settings
from django.core.cache import cache


def get_spotify_token():
    token = cache.get("spotify_token")
    if token:
        return token

    auth_header = base64.b64encode(
        f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}".encode()
    ).decode()

    response = requests.post(
        settings.SPOTIFY_TOKEN_URL,
        headers={"Authorization": f"Basic {auth_header}"},
        data={"grant_type": "client_credentials"}
    )

    response.raise_for_status()
    data = response.json()
    token = data.get("access_token")

    # Cache the token for future use
    cache.set("spotify_token", token, timeout=data.get("expires_in", 3600))

    return token


def spotify_get(endpoint, params=None):
    token = get_spotify_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{settings.SPOTIFY_API_BASE_URL}/{endpoint}", headers=headers, params=params
    )

    response.raise_for_status()
    return response.json()
