from django.urls import path
from . import views

urlpatterns = [
    path('<int:job_post_id>', views.job_posts, name='job-posts'),
]
