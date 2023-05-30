from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from ads.serializers import AdSerislizer
from rest_framework.permissions import IsAuthenticated
from ads.models import AdModel


class CreateAdApiView(
    CreateModelMixin,
    GenericAPIView
):
    serializer_class=AdSerislizer
    permission_classes=(IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ListAdApiView(
    ListModelMixin,
    GenericAPIView
):
    serializer_class=AdSerislizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return AdModel.objects.select_related("author").all()