from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def settings(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token:
        return redirect('/login')

    # if role != 'job_seeker':
    #     return redirect('/login')

  

    return render(request, 'settings.html', { 'role': role })
