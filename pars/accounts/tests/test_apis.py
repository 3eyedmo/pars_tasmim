from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import utils



class TestRegisterApi(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model()\
                    .objects.create(
                        email="user@m.com",
                        password="123213Mhsjkdbasjb"
                    )
        self.client = Client()
        self.path = reverse("accounts:register")
    

    
    def test_unique_email_constrant(self):
        resp = self.client.post(
            path=self.path,
            data={
                'email': 'user@m.com', 
                'password1': '123KMSAkmsajkjsnadjk',
                'password2': '123KMSAkmsajkjsnadjk'
            }
        )
        self.assertEqual(
            resp.status_code,
            400
        )

    @utils.mock_data_append(mocks=utils.get_mock_for_wrong_password())
    def test_wrong_password(self, mocks):
        for user in mocks:
            resp = self.client.post(
                path=self.path,
                data=user
            )
            self.assertNotEqual(
                resp.status_code,
                201
            )

    def test_right_information(self):
        resp = self.client.post(
            path=self.path,
            data={
                'email': 'user111@msadsad.com', 
                'password1': '123KMSAkmsajkjsnadjk',
                'password2': '123KMSAkmsajkjsnadjk'
            }
        )
        print(resp.content)
        self.assertEqual(
            resp.status_code,
            201
        )