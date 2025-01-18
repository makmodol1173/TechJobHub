from django.shortcuts import redirect
from django.shortcuts import render
from decouple import config

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def logout_view(request):
    response = redirect('/login') 
    response.delete_cookie(config('COOKIE_KEY_1')) 
    response.delete_cookie(config('COOKIE_KEY_2'))
    return response