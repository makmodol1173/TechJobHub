from django.urls import include, path

from . import views



urlpatterns = [
   
    path("loginaction/", views.loginaction, name="loginaction"),
    
]