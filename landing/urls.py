from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.Login, name='Login'),
    path('signup/', views.Signup, name='Signup'),
    path('forget-pass/', views.Forget_pass, name='Forget_pass'),
    path('dashboard/', views.Dashboard, name='Dashboard'),
    path('create-post/', views.Create_post, name='Create_post'),
    path('menu-options/', views.Menu_options, name='Menu_options'),
    path('bookmarks/', views.Bookmarks, name='Bookmarks'),
    path('drop-resume/', views.Drop_resume, name='Drop_resume'),
    path('profile/', views.Profile, name='profile'),
    path('post/', views.Post, name='post'),
    path('applicant-list/', views.Applicant_list, name='applicant_list'),
    path('apply-list/', views.Apply_list, name='apply_list'),
    path('assessment/', views.Assessment, name='assessment'),
    path('set-assessment/', views.Set_assessment, name='set_assessment'),
    path('assessment-mark/', views.Assessment_mark, name='assessment_mark'),
    path('company-details/', views.Company_details, name='company_details'),
    path('rating/', views.Rating, name='rating'),
    path('rec-job/', views.Rec_Job, name='rec_job'),
    path('set-interview/', views.Set_Interview, name='set_interview'),
    path('virtual-int/', views.Virtual_int, name='virtual_int'),
    # path('', views.job_list, name='job_list'),
    path('logout/', views.logout, name='logout'),
]


