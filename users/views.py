'''This file contains the views for the users app.'''

from django.shortcuts import render
from django.template import context


def login(request):
    '''This function is used to render the login page.'''
    login_context = {
        "tile": "Home - Авторизация"
        }
    return render(request, "users/login.html", login_context)

def registration(request):
    '''This function is used to render the registration page.'''
    registration_context = {
        "tile": "Home - Регистрация"
        }
    return render(request, "users/registration.html", registration_context)

def profile(request):
    '''This function is used to render the profile page.'''
    profile_context = {
        "tile": "Home - Кабинет"
        }
    return render(request, "users/profile.html", profile_context)

def logout(request):
    '''This function is used to render the logaut page.'''
    logout_context = {
        "tile": "Home - Выход"
        }
    return render(request, "users/logout.html", logout_context)