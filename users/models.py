""" This file is used to create the models for the users app. """

from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """This class is used to create the user model."""

    image = models.ImageField(
        upload_to="users_images", null=True, blank=True, verbose_name="Аватар"
    )

    class Meta:
        """Meta class"""

        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.username)
