from django.db import models

from customers.models import Customer


class Order(models.Model):
    """
    Model for creating orders table
    """

    item_name = models.CharField(unique=True, max_length=300)
    amount = models.FloatField(null=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return an order instance"""
        return self.item_name
