from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-platform-detail'),
]
