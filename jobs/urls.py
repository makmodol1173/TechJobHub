from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job_post, name='create_job_post'),
    # You can add other URL patterns here...
]

urlpatterns = [
    path('create-job/', views.create_job_post, name='create_job_post'),
    path('job-list/', views.job_list, name='job_list'),  # URL for job list
]