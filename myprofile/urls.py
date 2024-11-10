from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
]
