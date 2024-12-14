from django.urls import path
from . import views

urlpatterns = [
  path('', views.drop_resume, name='login'),
]
