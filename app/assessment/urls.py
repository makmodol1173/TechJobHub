from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessment, name='assessment'),
]
