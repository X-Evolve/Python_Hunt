from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('basicpy/',views.basicpy,name='basicpy' ),
    path('installpy/',views.installpy,name='installpy'),
    path('aboutpython/',views.aboutpython,name='aboutpython'),
]
