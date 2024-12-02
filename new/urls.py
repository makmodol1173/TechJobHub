# from django.urls import path, include

# urlpatterns = [
#     path('new/', include('new.urls')),
# ]
from django.urls import path,include
from . import views

urlpatterns = [
    #  path('new/', include('new.urls')),
    path('create-post/', views.create_job_post, name='create_job_post'),
]
