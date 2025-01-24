from django.db import connection
from django.shortcuts import render, redirect
from decouple import config
from django.conf import settings

def applicant_list(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token or role != 'recruiter':
        return redirect('/login')
      
    with connection.cursor() as cursor:
        query_recruiter = "SELECT recruiter_id FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter = cursor.fetchone()

        if not recruiter:
            return redirect('/login')

        recruiter_id = recruiter[0]

        query_job_seekers = """
            SELECT DISTINCT
                js.job_seeker_id,
                js.fname AS first_name,
                js.lname AS last_name,
                js.email AS email,
                # js.resume AS resume,  -- Added a comma here
                jp.title AS title,
                ass.mark
            FROM 
                job_post jp
            JOIN 
                application a ON jp.job_post_id = a.job_post_id
            JOIN 
                answers ans ON a.application_id = ans.application_id
            JOIN 
                assessment ass ON ans.answer_id = ass.answer_id
            JOIN
                job_seeker js ON a.job_seeker_id = js.job_seeker_id
            WHERE 
                jp.recruiter_id = %s AND ass.mark>=7;
        """

        cursor.execute(query_job_seekers, recruiter_id)
        job_seekers = cursor.fetchall()

    context = {
        'job_seekers': [
            {
                'job_seeker_id': seeker[0],
                'first_name': seeker[1],
                'last_name': seeker[2],
                'email': seeker[3],
                'title': seeker[4],
                'mark': seeker[5]
            }
            for seeker in job_seekers
        ],
    }
    
    return render(request, 'applicant-list.html', {'context':context, 'role':role})
