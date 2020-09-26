from customers.models import Customer
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthTestCase(APITestCase):
    def setUp(self):
        self.orders_url = reverse("orders:orders")
        self.user = Customer.objects.create(
            username="john",
            email="john@app.com",
            phone_number="0766554433",
            password="mypassword",
        )

    def test_authenticated_user_can_add_order_successfully(self):
        """test that an authenticated user can add an order successfully"""
        data = {
            "item_name": "john",
            "amount": "444",
        }
        self.client.force_authenticate(user=self.user)
        res = self.client.post(self.orders_url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_add_order(self):
        """test that an unauthenticated user cannot add an order"""
        data = {
            "item_name": "john",
            "amount": "444",
        }
        self.client.force_authenticate(user=None)
        res = self.client.post(self.orders_url, data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
