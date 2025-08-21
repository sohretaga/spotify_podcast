from rest_framework.views import APIView
from rest_framework.response import Response

from .services import SpotifyClient
from .serializers import ShowSerializer, EpisodeSerializer
from .mixins import SpotifyViewMixin


spotify = SpotifyClient()


class PodcastSearchView(SpotifyViewMixin, APIView):
    def get(self, request):
        query = request.query_params.get("q")
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=400)

        page = int(request.query_params.get("page", 1))
        page_size = int(request.query_params.get("page_size", self.page_size_default))
        offset = (page - 1) * page_size

        data = spotify.get("search", params={"q": query, "type": "show", "limit": page_size, "offset": offset})
        shows_data = data.get("shows", {})
        shows = shows_data.get("items", [])
        total = shows_data.get("total", 0)

        serializer = ShowSerializer(shows, many=True)
        return self.paginate_spotify(request, serializer.data, total, request.path, page_size, {"q": query})


class PodcastDetailView(APIView):
    def get(self, request, show_id):
        show = spotify.get(f"shows/{show_id}")
        serializer = ShowSerializer(show)
        return Response(serializer.data)


class PodcastEpisodesView(SpotifyViewMixin, APIView):
    def get(self, request, show_id):
        page = int(request.query_params.get("page", 1))
        page_size = int(request.query_params.get("page_size", self.page_size_default))
        offset = (page - 1) * page_size

        data = spotify.get(f"shows/{show_id}/episodes", params={"limit": page_size, "offset": offset})
        episodes = data.get("items", [])
        total = data.get("total", 0)

        serializer = EpisodeSerializer(episodes, many=True)
        return self.paginate_spotify(request, serializer.data, total, request.path, page_size)
