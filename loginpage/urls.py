
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('person/new/', views.person_form_view, name='person_form_view'),
]