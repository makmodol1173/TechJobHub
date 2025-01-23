from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def all_post(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token or not role == 'recruiter':
      return redirect('/login')

    with connection.cursor() as cursor:
        query_recruiter = "SELECT recruiter_id FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter = cursor.fetchone()
        
        if not recruiter:
          return redirect('/login')
        recruiter_id = recruiter[0]
        # print(recruiter_id)
        
        query = """
            SELECT DISTINCT 
                            jp.job_post_id, 
                            jp.title, 
                            jp.description, 
                            jp.key_responsibilities, 
                            jp.deadline, 
                            c.name AS company_name
                FROM job_post jp
                JOIN company c ON jp.recruiter_id = c.recruiter_id
                WHERE jp.recruiter_id = %s
        """
        cursor.execute(query, ( recruiter_id))
        posts = cursor.fetchall()
        # print(posts)


    return render(request, 'all-post.html', { 'jobs': posts, 'role': role })
