from django.shortcuts import render, redirect
from django.db import connection
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from decouple import config
import os

def profile(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))
    
    if not auth_token or not role:
        return redirect('/login')

    user = None
    skills = []

    with connection.cursor() as cursor:
        if role == 'recruiter':
            query = "SELECT * FROM recruiter WHERE email = %s"
            cursor.execute(query, (auth_token,))
            user_data = cursor.fetchone()
            if user_data:
                user = {
                    'fname': user_data[1],
                    'lname': user_data[2],
                    'role': role,
                    'profile_picture': user_data[5]  # Profile picture filename in DB
                }
        elif role == 'job_seeker':
            query = "SELECT * FROM job_seeker WHERE email = %s"
            cursor.execute(query, (auth_token,))
            user_data = cursor.fetchone()
            if user_data:
                user = {
                    'fname': user_data[1],
                    'lname': user_data[2],
                    'role': role,
                    'profile_picture': user_data[6]  # Profile picture filename in DB
                }

                skills_query = "SELECT skill_name FROM skill WHERE job_seeker_id = %s"
                cursor.execute(skills_query, (user_data[0],))
                skills = [row[0] for row in cursor.fetchall()]

        # Handle profile picture upload (POST request)
        if request.method == 'POST' and 'profile_picture' in request.FILES:
            uploaded_file = request.FILES['profile_picture']
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profile_pictures'))
            filename = fs.save(uploaded_file.name, uploaded_file)
            
            # Update profile picture in the database
            with connection.cursor() as cursor:
                if role == 'job_seeker':
                    update_query = "UPDATE job_seeker SET profile_picture = %s WHERE email = %s"
                elif role == 'recruiter':
                    update_query = "UPDATE recruiter SET profile_picture = %s WHERE email = %s"
                cursor.execute(update_query, (filename, auth_token))
                connection.commit()

            user['profile_picture'] = filename  # Update the profile picture filename in the user dict

        # Get the current profile picture URL after update
        profile_picture_url = settings.MEDIA_URL + 'profile_pictures/' + user.get('profile_picture', 'default.png')

    context = {
        'fname': user.get('fname'),
        'lname': user.get('lname'),
        'role': user.get('role'),
        'profile_picture_url': profile_picture_url,
        'skills': skills,
    }

    return render(request, 'profile.html', context)
