from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def create_post(request):
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
        
        query = "SELECT * FROM company WHERE recruiter_id= %s"
        cursor.execute(query, (recruiter_id,))
        company_details = cursor.fetchall()
        if not company_details:
            return redirect("/company-details")
        

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        key_responsibilities = request.POST.get('key_responsibilities')
        educational_requirement = request.POST.get('educational_requirement')
        year_of_experience = request.POST.get('year_of_experience')
        deadline = request.POST.get('deadline')
        job_type = request.POST.get('type')

        with connection.cursor() as cursor:
            insert_query = """
                INSERT INTO job_post (
                    recruiter_id, title, description,
                    location, key_responsibilities, educational_requirement, year_of_experience, deadline,
                    type
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                recruiter_id, title, description,
                location,  key_responsibilities, educational_requirement, year_of_experience, deadline,
                job_type
            ))
            
        messages.success(request, "Job post created successfully.")
        return redirect('/dashboard')

    return render(request, 'create-post.html')
