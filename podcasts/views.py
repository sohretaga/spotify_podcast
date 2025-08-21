from rest_framework.views import APIView
from rest_framework.response import Response
from .services import SpotifyClient
from .serializers import ShowSerializer, EpisodeSerializer

spotify = SpotifyClient()


class PodcastSearchView(APIView):
    def get(self, request):
        query = request.query_params.get("q")
        data = spotify.get("search", params={"q": query, "type": "show"})
        shows = data.get("shows", {}).get("items", [])
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)


class PodcastDetailView(APIView):
    def get(self, request, show_id):
        show = spotify.get(f"shows/{show_id}")
        serializer = ShowSerializer(show)
        return Response(serializer.data)


class PodcastEpisodesView(APIView):
    def get(self, request, show_id):
        data = spotify.get(f"shows/{show_id}/episodes")
        episodes = data.get("items", [])
        serializer = EpisodeSerializer(episodes, many=True)
        return Response(serializer.data)
