from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from ads.models import AdModel
from . import utils


class TestAdModel(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email="mmm@mmm.com", password="123456789"
        )

    def test_create_ad(self):
        ad_title = "title"
        ad_body = "body"
        ad = AdModel.objects.create(
            title=ad_title,
            body=ad_body,
            author=self.user
        )
        self.assertEqual(ad.title, ad_title)
        self.assertEqual(ad.body, ad_body)
        self.assertEqual(ad.author, self.user)
    
    @utils.mock_data_append(mocks=utils.get_mock_for_wrong_title_and_body())
    def test_wrong_credentials(self, mocks):
        for item in mocks:
            with self.assertRaises(ValidationError):
                ad = AdModel(
                    author=self.user,
                    **item
                )
                ad.save()
            