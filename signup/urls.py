from django.urls import include, path

from . import views

urlpatterns = [
    
   path("signaction/", views.signaction, name="signaction"),
   path("loginaction/", views.loginaction, name="loginaction"),
   # path('logout/', views.logout, name='Logout'),
   #path('profile/', views.profile_view, name="profile"),
   path('createcompany/', views.create_company, name='create_company'),
   path('profile/', views.profile_view, name="profile"),
   path('create-post/', views.create_post, name='create-post'),
   # path('create_post/', views.create_post, name="create_post"),
    
]