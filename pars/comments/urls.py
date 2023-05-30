from django.urls import path
from . import views

app_name="comments"
urlpatterns = [
    path("comments/<int:ad_id>/", views.CreateCommentApiView.as_view(), name="create_comments"),
    path("comments/<int:ad_id>/list/", views.CommentListApiView.as_view(), name="list_comments"),
]
