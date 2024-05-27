from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformAV

urlpatterns = [
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformAV.as_view(), name='movie_list'),
]
