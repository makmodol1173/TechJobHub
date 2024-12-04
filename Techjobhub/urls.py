"""
URL configuration for Techjobhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path("signup/", include('signup.urls')),
    #path("login/", include('login.urls')),
    #path('myprofile/', include('myprofile.urls')),
    #path('jobs/', include('jobs.urls')),
    path('landings/', include('landing.urls')),
    # path('job-post/', include('job_post.urls')),
    path('new/', include('new.urls')),
    path('drop_resume', include('drop_resume.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)