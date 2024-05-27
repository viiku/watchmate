from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        fields = "__all__"

     
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
