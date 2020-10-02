from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from helpers.model_wrapper import RetrieveUpdateDestroyAPIViewWrapper
from helpers.permissions import IsOwnerOrReadOnly
from utils.renderers import DefaultRenderer


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


class OrderDetail(RetrieveUpdateDestroyAPIViewWrapper):
    """
    view for retrieving updating and deleting orders
    """

    name = "order"
    pluralized_name = "orders"
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = (DefaultRenderer,)

    def update(self, request, *args, **kwargs):
        self.operation = "Update order"
        return super(RetrieveUpdateDestroyAPIViewWrapper, self).update(
            request, *args, **kwargs
        )
