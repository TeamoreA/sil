from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.customers.models import Customer
from apps.orders.models import Order


class AuthTestCase(APITestCase):
    def setUp(self):
        self.orders_url = reverse("orders:orders")
        self.user = Customer.objects.create(
            username="john",
            email="john@app.com",
            phone_number="0766554433",
            password="mypassword",
        )
        self.user2 = Customer.objects.create(
            username="john1",
            email="john1@app.com",
            phone_number="0766554431",
            password="mypassword",
        )
        self.order = Order.objects.create(
            item_name="an item", amount=200, owner=self.user
        )
        self.order_url = reverse("orders:order", args=[self.order.id])

    def test_string_representation_of_order_model(self):
        """Tests that the string representation of Order model return the item_name"""
        order = Order.objects.create(
            item_name="Test item", amount="633", owner=self.user
        )
        self.assertEqual(str(order), "Test item")

    def test_authenticated_user_can_add_order_successfully(self):
        """test that an authenticated user can add an order successfully"""
        data = {
            "item_name": "An item",
            "amount": "444",
        }
        self.client.force_authenticate(user=self.user)
        res = self.client.post(self.orders_url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["item_name"], data["item_name"])

    def test_listing_of_orders(self):
        """test listing of orders successfully"""
        Order.objects.create(item_name="Test item", amount="633", owner=self.user)
        res = self.client.get(self.orders_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]["item_name"], "an item")

    def test_unauthenticated_user_cannot_add_order(self):
        """test that an unauthenticated user cannot add an order"""
        data = {
            "item_name": "john",
            "amount": "444",
        }
        self.client.force_authenticate(user=None)
        res = self.client.post(self.orders_url, data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieving_of_an_order_successfully(self):
        """test succesful retieving of an order by a authenticated user"""
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.order_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["item_name"], "an item")

    def test_updating_of_an_order_with_put_fails(self):
        """test succesful updating of an order allows only PATCH method"""
        self.client.force_authenticate(user=self.user)
        data = {
            "item_name": "updated item",
        }
        res = self.client.put(self.order_url, data)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res.data["message"], "To update order, use PATCH method")

    def test_updating_of_an_order_successfully(self):
        """test succesful updating of an order by a authenticated user"""
        self.client.force_authenticate(user=self.user)
        data = {
            "item_name": "updated item",
        }
        res = self.client.patch(self.order_url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["item_name"], "updated item")

    def test_deleting_of_an_order(self):
        """test deletion of an order successfully"""
        self.client.force_authenticate(user=self.user)
        res = self.client.delete(self.order_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {})

    def test_user_cannot_delete_other_users_orders(self):
        """test that a user cannot delete an order they didn't create"""
        self.client.force_authenticate(user=self.user2)
        res = self.client.delete(self.order_url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn(
            res.data["detail"], "You do not have permission to perform this action."
        )

    def test_user_cannot_update_other_users_orders(self):
        """test that a user cannot update an order they didn't create"""
        self.client.force_authenticate(user=self.user2)
        data = {
            "item_name": "updated item1",
        }
        res = self.client.patch(self.order_url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn(
            res.data["detail"], "You do not have permission to perform this action."
        )
