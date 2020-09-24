# serializers for order model

from rest_framework import serializers

from orders.models import Order


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
        validated_data.update({"owner": self.context["request"].user})
        order = Order.objects.create(**validated_data)
        return order
