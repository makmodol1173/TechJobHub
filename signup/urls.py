from django.urls import include, path

from . import views




urlpatterns = [
    
   path("signaction/", views.signaction, name="signaction"),

    
]