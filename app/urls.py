from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', include('app.login.urls')),
    path('registration/', include('app.registration.urls')),
    path('profile/', include('app.profile.urls')),
]
