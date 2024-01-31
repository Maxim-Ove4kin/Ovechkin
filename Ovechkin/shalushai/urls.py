from django.contrib.sites import requests
from django.urls import path, include
from .views import *
urlpatterns = [
    path('not_log/', index, name='index'),
    path('in_log/', in_log, name='in_log_index'),
    path('', settings, name='settings'),
]
