from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def dashboard(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token or role != 'recruiter':
        return redirect('/login')

    recruiter_id = None
    job_posts = []

    with connection.cursor() as cursor:
        query_recruiter = "SELECT recruiter_id FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter = cursor.fetchone()

        if recruiter:
            recruiter_id = recruiter[0]

    has_posts = False
    if recruiter_id:
        with connection.cursor() as cursor:
            query_jobs = "SELECT title, description, location, key_responsibilities, educational_requirement, year_of_experience, deadline, type, job_post_id FROM job_post WHERE recruiter_id = %s"
            cursor.execute(query_jobs, (recruiter_id,))
            job_posts = cursor.fetchall()
            has_posts = bool(job_posts)

    context = {'job_posts': job_posts, 'has_posts': has_posts, 'role':role}
    return render(request, 'dashboard.html', context)
