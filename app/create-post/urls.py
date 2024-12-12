from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_post, name='company-details'),
]
