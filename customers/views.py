import json

import requests
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from customers.models import Customer as User
from customers.models import UserManager
from customers.serializers import RegistrationSerializer


class LoginView(APIView):
    """
    Login a new user
    """

    serializer_class = RegistrationSerializer

    def post(self, request):
        # validate the token
        payload = {"access_token": request.data.get("token")}
        phone_number = request.data.get("phone_number")
        r = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo", params=payload
        )
        data = json.loads(r.text)
        if "error" in data:
            content = {"message": "This token is already expired."}
            return Response(content)
        # create user if not exist
        email = data.get("email")
        name = data.get("name", email.split("@")[0])
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # provider random default password
            password = make_password(UserManager().make_random_password())
            user_data = {
                "email": email,
                "code": data["id"],
                "phone_number": phone_number,
                "username": name,
                "password": password,
                "last_login": now(),
            }
            serializer = self.serializer_class(data=user_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = User.objects.get(email=email)
        # generate token without username & password
        token = RefreshToken.for_user(user)
        response = {
            "status": "success",
            "message": "You have been authenticated succesfully",
            "data": {
                "username": name,
                "email": email,
                "access_token": str(token.access_token),
                "refresh_token": str(token),
            },
        }
        return Response(response, status=status.HTTP_200_OK)
