# serializers for order model

import africastalking
import environ
from rest_framework import serializers

from apps.orders.models import Order

env = environ.Env()
environ.Env.read_env()

api_key = env.str("AF_API_KEY")
username = env.str("AF_USERNAME")
# Initialize SDK
africastalking.initialize(username, api_key)
sms = africastalking.SMS


class OrderSerializer(serializers.ModelSerializer):
    """
    serializer class for the order model
    """

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("owner", "created_at")

    def create(self, validated_data):
        """
        Add customer to the owner
        """
        user = self.context["request"].user
        validated_data.update({"owner": user})
        order = Order.objects.create(**validated_data)
        # Initialize SDK
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        message = "Order '{}' has\
             been created successfully".format(
            order.item_name
        )
        sms.send(message, ["+254" + user.phone_number])
        return order
