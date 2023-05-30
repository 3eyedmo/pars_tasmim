from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model
from rest_framework.status import is_success
from . import utils
from ads.models import AdModel
from comments.models import CommentModel


class TestCreateAdApi(TestCase):
    def setUp(self) -> None:
        user_credential = {
            "email": "mo@mo.com", "password": "123456"
        }
        self.user = get_user_model().objects.create(**user_credential)
        self.client = Client()
        token_pair_url = reverse("accounts:token_pair")
        access_token = self.client.post(
            path=token_pair_url,
            data=user_credential
        ).json().get("access")
        self.headers = {"HTTP_AUTHORIZATION": f"Bearer {access_token}"}
        self.ad = AdModel.objects.create(
            author=self.user,
            **{"title": "title", "body": "body"}
        )
    
    def test_authentication(self):
        resp = self.client.post(
            path=reverse("comments:create_comments", kwargs={"ad_id": self.ad.id}),
            data={"text": "title"}
        )
        self.assertEqual(
            is_success(resp.status_code), False
        )

    def test_not_found(self):
        resp = self.client.post(
            path=reverse("comments:create_comments", kwargs={"ad_id": 155000000000}),
            data={"text": "title"}
        )
        self.assertEqual(
            is_success(resp.status_code), False
        )
    
    @utils.mock_data_append(mocks=[{"text": "text"*100000}])
    def test_wrong_data_for_comment(self, mocks):
        
        for item in mocks:
            resp = self.client.post(
                path=reverse("comments:create_comments", kwargs={"ad_id": self.ad.id}),
                data=item,
                **self.headers
            )
            self.assertEqual(
                is_success(resp.status_code), False
            )
    
    def test_proper_data(self):
        resp = self.client.post(
            path=reverse("comments:create_comments", kwargs={"ad_id": self.ad.id}),
            data={"text": "text"},
            **self.headers
        )
        self.assertEqual(
            is_success(resp.status_code), True
        )


class TestListComments(TestCase):
    def setUp(self) -> None:
        self.client=Client()
        user_credential = {
            "email": "mo@mo.com", "password": "123456"
        }
        self.user = get_user_model().objects.create(**user_credential)
        self.ad = AdModel.objects.create(
            author=self.user,
            **{"title": "title", "body": "body"}
        )
        comments = [
            {"text": "text1"},
            {"text": "text2"},
            {"text": "text3"},
            {"text": "text4"},
            {"text": "text5"},
        ]
        for item in comments:
            CommentModel.objects.create(author=self.user, ad=self.ad, **item)
        
        self.path = reverse("comments:list_comments", kwargs={"ad_id": self.ad.id})

    def test_get_list_api(self):
        resp = self.client.get(
            path=self.path
        )
        self.assertEqual(is_success(resp.status_code), True)
        self.assertEqual(len(resp.json().get("results")), 5)
