from django.urls import path
from . import views

urlpatterns = [
    path('Drop_resume/', views.drop_resume, name='Drop_resume'),
]
