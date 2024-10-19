from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
    path('forget-pass/', views.Forget_pass, name='forget_pass'),
    path('landing-page/', views.Landing_page, name='landing_page'),
    path('create-post/', views.Create_post, name='create_post'),
    path('menu-options/', views.Menu_options, name='menu_options'),
    path('bookmarks/', views.Bookmarks, name='bookmarks'),
    path('drop-resume/', views.Drop_resume, name='drop_resume'),
    path('profile/', views.Profile, name='profile'),
    path('post/', views.Post, name='post'),
    path('applicant-list/', views.Applicant_list, name='applicant_list'),
    path('apply-list/', views.Apply_list, name='apply_list'),
    path('assessment/', views.Assessment, name='assessment'),
    path('company-details/', views.Company_details, name='company_details'),
    path('rating/', views.Rating, name='rating'),
    path('rec-job/', views.Rec_Job, name='rec_job'),
    path('set-interview/', views.Set_Interview, name='set_interview'),
    path('virtual-int/', views.Virtual_int, name='virtual_int'),
]