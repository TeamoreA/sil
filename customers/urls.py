from django.urls import path

from customers import views

app_name = "auth"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="google"),
]
