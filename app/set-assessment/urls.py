from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_assessment, name='set-assessment'),
]
