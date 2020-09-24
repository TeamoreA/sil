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


class LoginView(APIView):
    def post(self, request):
        # validate the token
        payload = {"access_token": request.data.get("token")}
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
            if data.get("name"):
                user = User.objects.get(username=name)
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User()
            user.username = name
            # provider random default password
            user.password = make_password(UserManager().make_random_password())
            user.email = email
            user.code = data["id"]
            user.last_login = now()
            user.save()

        token = RefreshToken.for_user(
            user
        )  # generate token without username & password
        response = {}
        response["username"] = user.username
        response["email"] = user.email
        response["access_token"] = str(token.access_token)
        response["refresh_token"] = str(token)
        return Response(response, status=status.HTTP_200_OK)
