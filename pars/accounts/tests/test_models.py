from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

class UserModelTest(TestCase):
    def setUp(self) -> None:
        self.normal_user = get_user_model()\
                    .objects.create(
                        email="normal@m.com",
                        password="134658479456"
                    )
        self.super_user = get_user_model()\
                    .objects.create_superuser(
                        email="super@m.com",
                        password="134658479456"
                    )
    
    def test_super_user_is_admin(self):
        self.assertTrue(self.super_user.is_superuser)

    def test_normal_user_is_not_admin(self):
        self.assertFalse(self.normal_user.is_superuser)

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create(
                email="normal@m.com",
                password="13sadsadasd3242"
            )
