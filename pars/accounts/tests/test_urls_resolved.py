from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views
from rest_framework_simplejwt.views import TokenObtainPairView



class TestUrls(TestCase):
    def test_register_url_resolved(self):
        register_url = reverse('accounts:register')
        self.assertEqual(
            resolve(register_url).func.view_class,
            views.RegisterUserApiView
        )

    def test_token_pair_url_resolved(self):
        token_pair_url = reverse('accounts:token_pair')
        self.assertEqual(
            resolve(token_pair_url).func.view_class,
            TokenObtainPairView
        )
