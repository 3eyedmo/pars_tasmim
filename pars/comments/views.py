from rest_framework.generics import CreateAPIView, ListAPIView
from comments.serializers import CommentSerializer
from comments.models import CommentModel
from rest_framework.permissions import IsAuthenticated



class CreateCommentApiView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentListApiView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_id")
        return CommentModel.objects.select_related("author").filter(ad__id=ad_id)
