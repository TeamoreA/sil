from rest_framework import serializers

from customers.models import Customer


class RegistrationSerializer(serializers.ModelSerializer):
    """
    serializers for the registrations  and customer request
    """

    def __init__(self, *args, **kwargs):
        super(RegistrationSerializer, self).__init__(*args, **kwargs)

        for field in self.fields:
            error_messages = self.fields[field].error_messages
            error_messages["null"] = error_messages["blank"] = error_messages[
                "required"
            ] = "Please fill in the {}.".format(field)

    phone_number = serializers.RegexField(
        regex=r"^[0-9]+$",
        min_length=10,
        max_length=20,
        error_messages={
            "min_length": "Phone number must have a minimum of 10 characters.",
            "max_length": "Phone number must have a maximum of 20 characters.",
            "invalid": "Phone number can only have numeric characters.",
        },
    )

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        return customer
