from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from . import views
app_name = 'coffees'
urlpatterns = [
    path('', views.index, name='index'),
]