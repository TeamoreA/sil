from django.urls import path

from apps.orders import views

app_name = "orders"

urlpatterns = [
    path("orders/", views.OrderList.as_view(), name="orders"),
]
