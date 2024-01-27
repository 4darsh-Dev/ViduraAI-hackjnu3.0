from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("api/", views.ask_vidura, name='ask_vidura'),
    
]
