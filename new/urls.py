from django.urls import path, include

urlpatterns = [
    path('new/', include('new.urls')),
]
