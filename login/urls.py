from django.urls import include, path

from login import views



urlpatterns = [
   
    path("loginaction/", views.loginaction, name="loginaction"),
    
]