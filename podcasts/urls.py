from django.urls import path
from podcasts import views


urlpatterns = [
    path('search/', views.PodcastSearchView.as_view(), name='podcast-search'),
    path('shows/<str:show_id>/', views.PodcastDetailView.as_view(), name='podcast-detail'),
    path('shows/<str:show_id>/episodes/', views.PodcastEpisodesView.as_view(), name='podcast-episodes'),
]
