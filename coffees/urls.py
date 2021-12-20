from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from . import views


app_name = 'coffees'
urlpatterns = [
    # ex: /coffees/
    path('', views.index, name='index'),
    # ex: /coffees/1/
    path('<int:pk>/', views.show, name='show'),
]