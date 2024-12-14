from django.urls import path
from . import views

urlpatterns = [
  path('', views.recommend_job, name='login'),
]
