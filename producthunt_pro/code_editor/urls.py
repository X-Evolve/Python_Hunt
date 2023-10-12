from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('editor/', views.python_editor, name='editor'),
]
