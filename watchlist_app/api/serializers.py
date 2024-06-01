from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        exclude = ('watchList',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        fields = "__all__"

     
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=False, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
