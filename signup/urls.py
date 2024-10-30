from django.urls import include, path

from signup import views




urlpatterns = [
    
   path("signaction/", views.signaction, name="signaction"),

    
]