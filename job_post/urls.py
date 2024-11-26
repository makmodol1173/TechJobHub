from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.create_job_post, name='create_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
