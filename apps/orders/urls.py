from django.urls import path

from apps.orders import views

app_name = "orders"

urlpatterns = [
    path("order/", views.OrderList.as_view(), name="orders"),
    path("order/<int:pk>", views.OrderDetail.as_view(), name="order"),
]
