from rest_framework import serializers
from ads.models import AdModel
from accounts.serializers import ReadOnlyUserSerializer

class AdSerislizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=1024)
    body = serializers.CharField(max_length=16384)
    author = ReadOnlyUserSerializer(read_only=True)

    def create(self, validated_data):
        author = self.context.get("request").user
        ad = AdModel(author=author, **validated_data)
        ad.save()
        return ad


        
