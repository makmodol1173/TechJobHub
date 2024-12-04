from django.urls import path
from . import views

urlpatterns = [
    path('drop_resume/', views.drop_resume, name='drop_resume'),
    path('save_question/', views.save_question, name='save_question'),
    # path('set-assessment/', views.set_assessment, name='set_assessment'),
    # path('dashboard/', views.dashboard, name='Dashboard')

]
