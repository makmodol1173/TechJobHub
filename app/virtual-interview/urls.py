from django.urls import path
from . import views

urlpatterns = [
    path('', views.virtual_interview, name='virtual-interview'),
]
