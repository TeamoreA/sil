from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """
    Overides the base user manager class
    """

    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError("Customer must have a username")
        user = self.model(username=username, **extra_fields)

        if password:
            user.set_password(password)

        user.save()

        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["code"]

    objects = UserManager()

    def __str__(self):
        """Return a customer instance"""
        return self.username

    @staticmethod
    def get_user(username):
        try:
            user = Customer.objects.get(username=username)
            return user

        except Exception:
            return False
