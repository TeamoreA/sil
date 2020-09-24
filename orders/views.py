from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from orders.models import Order
from orders.renders import DefaultRenderer
from orders.serializers import OrderSerializer


class OrderList(ListCreateAPIView):
    """
    view for list and creating orders
    """

    name = "order"
    pluralized_name = "orders"
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = (DefaultRenderer,)
