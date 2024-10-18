from django.urls import path
from . import views

urlpatterns = [
    path('F1/', views.F1, name='F1'),
    path('F2/', views.F2, name='F2'),
    path('F3/', views.F3, name='F3'),
    path('F4/', views.F4, name='F4'),
    path('F6/', views.F6, name='F6'),
    path('F7/', views.F7, name='F7'),
    path('F11/', views.F11, name='F11'),
    path('F11_1/', views.F11_1, name='F11_1'),
    path('F12/', views.F12, name='F12'),
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

