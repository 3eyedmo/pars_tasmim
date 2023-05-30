from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model
from rest_framework.status import is_success
from . import utils
from ads.models import AdModel


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
    
    def test_authentication(self):
        resp = self.client.post(
            path=reverse("ads:create_ads"),
            data={"title": "title", "body": "body"}
        )
        self.assertEqual(
            is_success(resp.status_code), False
        )
    
    @utils.mock_data_append(mocks=utils.get_mock_for_wrong_title_and_body())
    def test_wrong_data_for_ad(self, mocks):
        
        for item in mocks:
            resp = self.client.post(
                path=reverse("ads:create_ads"),
                data=item,
                **self.headers
            )
            self.assertEqual(
                is_success(resp.status_code), False
            )
    
    def test_proper_data(self):
        resp = self.client.post(
            path=reverse("ads:create_ads"),
            data={"title": "some title", "body": "some body"},
            **self.headers
        )
        self.assertEqual(
            is_success(resp.status_code), True
        )


class TestListAds(TestCase):
    def setUp(self) -> None:
        self.client=Client()
        user_credential = {
            "email": "mo@mo.com", "password": "123456"
        }
        self.user = get_user_model().objects.create(**user_credential)
        ads = [
            {"title": "title1", "body": "body1"},
            {"title": "title2", "body": "body2"},
            {"title": "title3", "body": "body3"},
            {"title": "title4", "body": "body4"},
            {"title": "title5", "body": "body5"},
        ]
        for item in ads:
            AdModel.objects.create(author=self.user, **item)
        
        self.path = reverse("ads:get_ad_list")

    def test_get_list_api(self):
        resp = self.client.get(
            path=self.path
        )
        self.assertEqual(is_success(resp.status_code), True)
        self.assertEqual(len(resp.json().get("results")), 5)
