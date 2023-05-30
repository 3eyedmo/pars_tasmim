from rest_framework.generics import CreateAPIView
from accounts.serializers import UserRegisterSerializer

class RegisterUserApiView(CreateAPIView):
    serializer_class = UserRegisterSerializer
