from rest_framework import serializers
from comments.models import CommentModel
from accounts.serializers import ReadOnlyUserSerializer
from ads.models import AdModel


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=255)
    author = ReadOnlyUserSerializer(read_only=True)

    def validate(self, attrs):
        ad_id = self.context.get("view").kwargs.get("ad_id")
        try:
            self.ad = AdModel.objects.get(id=ad_id)
        except:
            raise serializers.ValidationError({
                "ad_id": "ad with this ad_id does not exists"
            })
        return attrs

    def create(self, validated_data):
        user = self.context.get("request").user
        print(user)
        comment = CommentModel(
            author=user,
            ad = self.ad,
            **validated_data
        )
        comment.save()
        return comment