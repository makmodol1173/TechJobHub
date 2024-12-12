from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config
import bcrypt

def login(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    user_role = request.COOKIES.get(config('COOKIE_KEY_2'))
    if auth_token and user_role:
        return redirect('/profile')

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "All fields are required")
            return render(request, 'login.html')

        with connection.cursor() as cursor:
            recruiter_query = "SELECT * FROM recruiter WHERE email = %s"
            cursor.execute(recruiter_query, (email,))
            recruiter_data = cursor.fetchone()

            job_seeker_query = "SELECT * FROM job_seeker WHERE email = %s"
            cursor.execute(job_seeker_query, (email,))
            job_seeker_data = cursor.fetchone()

            if not recruiter_data and not job_seeker_data:
                messages.error(request, "No user found with that email address.")
                return render(request, 'login.html')

            if recruiter_data:
                user_data = recruiter_data
                role = "recruiter"
            else:
                user_data = job_seeker_data
                role = "job_seeker"

            check_password = bcrypt.checkpw(password.encode('utf-8'), user_data[4].encode('utf-8'))  

            if check_password:
                response = redirect("/profile")
                response.set_cookie(config('COOKIE_KEY_1'), email, max_age=3600, httponly=True, secure=True)
                response.set_cookie(config('COOKIE_KEY_2'), role, max_age=3600, httponly=True, secure=True)
                return response
            else:
                messages.error(request, "Invalid password. Please try again.")

    return render(request, 'login.html')
