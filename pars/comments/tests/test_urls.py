from django.test import TestCase
from django.urls import reverse, resolve
from comments import views



class TestCommentsUrls(TestCase):
    def test_create_comment_url(self):
        url = reverse("comments:create_comments", kwargs={"ad_id": 50})
        resolved = resolve(url)
        self.assertEqual(
            resolved.func.view_class, views.CreateCommentApiView
        )

    def test_list_comments_url(self):
        url = reverse("comments:list_comments", kwargs={"ad_id": 50})
        resolved = resolve(url)
        self.assertEqual(
            resolved.func.view_class, views.CommentListApiView
        )
    