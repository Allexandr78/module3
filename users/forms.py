""" This module is used to create forms for the users application. """

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    """This class is used to create a form for the user login."""

    class Meta:
        """This class is used to create a form for the user login."""

        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите имя пользователя",
                }
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Введите пароль"}
            ),
        }
