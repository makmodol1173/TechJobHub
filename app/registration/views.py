from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import connection
from decouple import config
import bcrypt

def registration(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    user_role = request.COOKIES.get(config('COOKIE_KEY_2'))
    if auth_token and user_role:
        return redirect('/profile') 

    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not fname or not lname or not email or not password or not role:
            messages.error(request, "All fields are required")
            return render(request, 'registration.html')

        if role not in ["recruiter", "job_seeker"]:
            messages.error(request, "Invalid role selected")
            return render(request, 'registration.html')

        with connection.cursor() as cursor:
            recruiter_query = "SELECT * FROM recruiter WHERE email = %s"
            cursor.execute(recruiter_query, (email,))
            recruiter_data = cursor.fetchone()

            job_seeker_query = "SELECT * FROM job_seeker WHERE email = %s"
            cursor.execute(job_seeker_query, (email,))
            job_seeker_data = cursor.fetchone()

            if recruiter_data or job_seeker_data:
                messages.error(request, "Email already exists")
                return render(request, 'registration.html')

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if role == "recruiter":
                recruiter_insert_query = """
                    INSERT INTO recruiter (fname, lname, email, password) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(recruiter_insert_query, (fname, lname, email, hashed_password))
            elif role == "job_seeker":
                job_seeker_insert_query = """INSERT INTO job_seeker (fname, lname, email, password) VALUES (%s, %s, %s, %s)"""
                cursor.execute(job_seeker_insert_query, (fname, lname, email, hashed_password))

            connection.commit() 

            response = redirect("/profile")
            response.set_cookie(config('COOKIE_KEY_1'), email, max_age=3600, httponly=True, secure=True)
            response.set_cookie(config('COOKIE_KEY_2'), role, max_age=3600, httponly=True, secure=True)
            return response

    return render(request, 'registration.html')
