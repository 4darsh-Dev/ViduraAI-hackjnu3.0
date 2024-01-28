from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("vidura/", views.vidura, name='vidura'),
    path("learn/", views.learn, name='learn'),
    path("learn/fundamental_rights/", views.fundamental_rights, name='fundamental_rights'),
    path("login/", views.loginUser, name='login'),
    path("signup/", views.signupUser, name='signup'),
    path("logout/", views.logoutUser, name='logout'),

]
