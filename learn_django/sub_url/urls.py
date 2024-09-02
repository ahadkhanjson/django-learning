from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_sub_url, name='home_sub_url'),
   
]
