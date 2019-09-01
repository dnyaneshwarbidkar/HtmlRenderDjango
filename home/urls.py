from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/getdata',views.sendData),
    path('home/',views.index)
]
