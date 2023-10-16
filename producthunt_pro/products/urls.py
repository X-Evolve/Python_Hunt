from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('basicpy/',views.basicpy,name='basicpy' ),
    path('installpy/',views.installpy,name='installpy'),
    path('aboutpython/',views.aboutpython,name='aboutpython'),
    path('keywords/',views.keywords, name='keywords'),
    path('variables/', views.variables, name='variables'),
    path('datatypes/',views.datatypes, name='datatypes'),
    path('sets/',views.sets, name='sets'),
    path('statements/',views.statements, name='statements'),
    path('tuples/', views.tuples, name='tuples'),
    path('string/',views.string,name='string'),
    path('lists/', views.lists, name='lists'),
    path('dicts/', views.dicts, name='dicts'),
]
