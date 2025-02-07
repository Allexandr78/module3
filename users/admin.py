''' This file is used to register the models to the admin site. '''

from django.contrib import admin

from users.models import User

admin.site.register(User)

