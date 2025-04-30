""" URL Configuration for the carts app """

from django.urls import path

from carts import views

app_name = "carts"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]
