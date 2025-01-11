from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def menu_options(request):
    return render(request, 'menu-options.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')