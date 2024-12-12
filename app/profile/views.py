from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def profile(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))
    if not auth_token or not role:
        return redirect('/login')
    
    user = None
    with connection.cursor() as cursor:
        query_recruiter = "SELECT * FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter_data = cursor.fetchone()

        if recruiter_data:
            user = {
                'fname': recruiter_data[1],
                'lname': recruiter_data[2],
                'role': role
            }
        else:
            query_job_seeker = "SELECT * FROM job_seeker WHERE email = %s"
            cursor.execute(query_job_seeker, (auth_token,))
            job_seeker_data = cursor.fetchone()

            if job_seeker_data:
                user = {
                    'fname': job_seeker_data[1],
                    'lname': job_seeker_data[2],
                    'role': role 
                }

    if not user:
        return redirect('/login')

    return render(request, 'profile.html', user)
