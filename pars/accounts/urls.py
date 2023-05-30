from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views


app_name = "accounts"
urlpatterns = [
    path("register/", views.RegisterUserApiView.as_view(), name="register"),
    path("token_pair/", TokenObtainPairView.as_view(), name="token_pair")
]
