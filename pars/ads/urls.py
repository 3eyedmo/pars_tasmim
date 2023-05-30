from django.urls import path
from . import views


app_name="ads"
urlpatterns = [
    path("", views.CreateAdApiView.as_view(), name="create_ads"),
    path("list/", views.ListAdApiView.as_view(), name="get_ad_list")
]
