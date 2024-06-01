from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewCreate, ReviewList, ReviewDetail, WatchListAV,
                                    WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-platform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    # should create review of movie with id
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    # should return all review of movie with id
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    # should return review with particular id
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),    
    
]
