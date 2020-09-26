from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.customers.models import Customer as User
from apps.customers.serializers import RegistrationSerializer


class AuthTestCase(APITestCase):
    def setUp(self):
        self.auth_url = reverse("auth:login")
        self.user_data = {
            "username": "thedon",
            "email": "thedon@app.com",
            "phone_number": "0766554433",
            "code": "828392367983",
            "password": "7387jddkdc",
        }

    def test_add_user_successfully(self):
        """Tests that only valid data creates a user successfully"""
        serializer = RegistrationSerializer(data=self.user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=self.user_data["email"])
        self.assertEqual(str(user), self.user_data["username"])

    def test_authenticate_user_with_an_expired_token(self):
        """test that an expired or a bad token cannot authenticate a user"""
        data = {
            "phone_number": "0733117744",
            "token": "badtoken",
        }
        res = self.client.post(self.auth_url, data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            res.data["message"], "This token is incorrect or already expired."
        )
