from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Customer(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["code"]

    def __str__(self):
        """Return a customer instance"""
        return self.username
