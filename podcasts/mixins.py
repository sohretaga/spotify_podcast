from rest_framework.response import Response
from urllib.parse import urlencode


class SpotifyViewMixin:
    """
    Manual pagination mixin for Spotify API endpoints.
    Provides 'page' and 'page_size' query params and constructs next/prev URLs
    """

    page_size_default = 20  # default page size

    def paginate_spotify(self, request, items, total, base_path, page_size=None, extra_params=None):
        page = int(request.query_params.get("page", 1))
        page_size = page_size or int(request.query_params.get("page_size", self.page_size_default))

        # next/previous URLs
        base_url = request.build_absolute_uri(base_path)

        def make_url(page_number):
            if page_number < 1:
                return None
            offset = (page_number - 1) * page_size
            if offset >= total:
                return None
            return f"{base_url}?{urlencode({**(extra_params or {}), 'page': page_number, 'page_size': page_size})}"

        return Response({
            "count": total,
            "next": make_url(page + 1),
            "previous": make_url(page - 1),
            "results": items
        })
