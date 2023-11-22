from django.contrib.sites import requests
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('', index, name='in_log_index'),
    path('', index, name='settings'),
]
