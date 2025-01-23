from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', include('app.login.urls')),
    path('registration/', include('app.registration.urls')),
    path('profile/', include('app.profile.urls')),
    path('dashboard/', include('app.dashboard.urls')),
    path('company-details/', include('app.company-details.urls')),
    path('create-post/', include('app.create-post.urls')),
    path('all-post/', include('app.all-post.urls')),
    path('job-posts/', include('app.job-posts.urls')),
    path('application/', include('app.application.urls')),
    path('application-list/', include('app.application-list.urls')),
    path('drop-resume/', include('app.drop-resume.urls')),
    path('recommend-job/', include('app.recommend-job.urls')),
    path('bookmarks/', include('app.bookmarks.urls')),
    path('set-assessment/', include('app.set-assessment.urls')),
    path('assessment/', include('app.assessment.urls')),
    path('assessment-mark/', include('app.assessment-mark.urls')),
    path('rating/', include('app.rating.urls')),
    path('settings/', include('app.settings.urls')),
    path('applicant-list/', include('app.applicant-list.urls')),
    path('virtual-interview/', include('app.virtual-interview.urls')),
    path('logout/', views.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
