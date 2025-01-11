''' This file is used to define the URL patterns for the main app. '''
from django.urls import path
import app
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]