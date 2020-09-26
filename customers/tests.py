from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthTestCase(APITestCase):
    def setUp(self):
        self.auth_url = reverse("auth:login")

    def test_authenticate_user_with_an_expired_token(self):
        """test that an expired token cannot authenticate a user"""
        data = {
            "phone_number": "0733117744",
            "token": "ya29.a0AfH6SMB_DHlewDyGgGWoxys1kkLx8rtRnfvcJEVFroxFaOFry_\
                UNmguWX8oYkjKgACCpv_2qezgVILNMYc1i-bKntSmv5YZ32dybmF76jzXu8jiPc\
                    HpZv9Ev_ktFqJ40Z4fMbOQetr1t94t6V2b3kdXSPsJt6uOpa9A",
        }
        res = self.client.post(self.auth_url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["message"], "This token is already expired.")
