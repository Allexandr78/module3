"""This file contains the views for the users app."""

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.forms import UserLoginForm


def login(request):
    """This function is used to render the login page."""
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
        else:
            form = UserLoginForm()

    login_context = {"tile": "Home - Авторизация", "form": form}

    return render(request, "users/login.html", login_context)


def registration(request):
    """This function is used to render the registration page."""
    registration_context = {"tile": "Home - Регистрация"}
    return render(request, "users/registration.html", registration_context)


def profile(request):
    """This function is used to render the profile page."""
    profile_context = {"tile": "Home - Кабинет"}
    return render(request, "users/profile.html", profile_context)


def logout(request):
    """This function is used to render the logaut page."""
    logout_context = {"tile": "Home - Выход"}
    return render(request, "users/logout.html", logout_context)
