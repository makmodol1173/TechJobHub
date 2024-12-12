from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', include('app.login.urls')),
    path('registration/', include('app.registration.urls')),
    path('profile/', include('app.profile.urls')),
    path('dashboard/', include('app.dashboard.urls')),
    path('company-details/', include('app.company-details.urls')),
    path('create-post/', include('app.create-post.urls')),
]
