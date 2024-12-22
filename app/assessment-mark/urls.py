from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessment_mark, name='assessment-mark'),
]
