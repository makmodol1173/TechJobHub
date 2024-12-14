from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def dashboard(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    # if not auth_token or role != 'recruiter':
    if not auth_token:
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
            # query_jobs = "SELECT title, description, location, key_responsibilities, educational_requirement, year_of_experience, deadline, type, job_post_id FROM job_post WHERE recruiter_id = %s"
            query_jobs = """SELECT 
                jp.job_post_id,
                jp.title,
                jp.description,
                jp.key_responsibilities,
                jp.location,
                jp.educational_requirement,
                jp.deadline,
                jp.year_of_experience,
                jp.type AS job_type,
                jp.keywords,
                c.company_id,
                c.name AS company_name,
                c.address AS company_address,
                c.description AS company_description,
                c.trade_license_number,
                c.website_url
            FROM 
                job_post jp
            LEFT JOIN 
                company c ON jp.recruiter_id = c.recruiter_id
            WHERE 
                jp.recruiter_id = %s"""
            cursor.execute(query_jobs, (recruiter_id,))
            job_posts = cursor.fetchall()

    context = {'job_posts': job_posts,  'role':role}
    return render(request, 'dashboard.html', context)
