from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.customers.permisions import IsOwnerOrReadOnly
from apps.orders.models import Order
from apps.orders.renders import DefaultRenderer
from apps.orders.serializers import OrderSerializer


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


class OrderDetail(RetrieveUpdateDestroyAPIView):
    """
    view for retrieving updating and deleting orders
    """

    name = "order"
    pluralized_name = "orders"
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = (DefaultRenderer,)
