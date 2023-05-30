from django.urls import reverse, resolve
from django.test import TestCase
from ads import views



class TestAdsUrlsResolved(TestCase):
    def test_create_ad_url_resolved(self):
        create_ad_url = reverse("ads:create_ads")
        resolved_url = resolve(create_ad_url)
        self.assertEqual(
            resolved_url.func.view_class,
            views.CreateAdApiView
        )

    def test_list_ad_url_resolved(self):
        list_ad_url = reverse("ads:get_ad_list")
        resolved_url = resolve(list_ad_url)
        self.assertEqual(
            resolved_url.func.view_class,
            views.ListAdApiView
        )