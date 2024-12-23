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
    profile_picture_url = '/static/image/image.png'  # Default profile picture
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
                    'profile_picture': user_data[5]  # Profile picture column in recruiter table
                }
                profile_picture_url = user_data[5] if user_data[5] else profile_picture_url
        elif role == 'job_seeker':
            query = "SELECT * FROM job_seeker WHERE email = %s"
            cursor.execute(query, (auth_token,))
            user_data = cursor.fetchone()
            if user_data:
                user = {
                    'fname': user_data[1],
                    'lname': user_data[2],
                    'role': role,
                    'profile_picture': user_data[6]  # Profile picture column in job_seeker table
                }
                profile_picture_url = user_data[6] if user_data[6] else profile_picture_url

                # Fetch skills for job seekers
                skills_query = "SELECT skill_name FROM skill WHERE job_seeker_id = %s"
                cursor.execute(skills_query, (user_data[0],))
                skills = [row[0] for row in cursor.fetchall()]

    # Handle profile picture upload (POST request)
    if request.method == 'POST' and 'profile_picture' in request.FILES:
        profile_picture = request.FILES['profile_picture']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profile_pictures'))
        filename = fs.save(profile_picture.name, profile_picture)
        uploaded_file_url = settings.MEDIA_URL + 'profile_pictures/' + filename

        # Update profile picture in the database
        with connection.cursor() as cursor:
            if role == 'job_seeker':
                update_query = "UPDATE job_seeker SET profile_picture = %s WHERE email = %s"
            elif role == 'recruiter':
                update_query = "UPDATE recruiter SET profile_picture = %s WHERE email = %s"
            cursor.execute(update_query, (filename, auth_token))  # Save just the filename in DB, not the full URL
        profile_picture_url = uploaded_file_url  # Update the URL for the uploaded profile picture

    # Handle skills update (if applicable)
    if request.method == 'POST' and 'skills' in request.POST:
        updated_skills = request.POST.get('skills', '').split(',')
        updated_skills = [skill.strip() for skill in updated_skills if skill.strip()]  # Remove empty or whitespace-only skills

        if role == 'job_seeker':
            with connection.cursor() as cursor:
                # Delete existing skills
                delete_skills_query = "DELETE FROM skill WHERE job_seeker_id = %s"
                cursor.execute(delete_skills_query, (user_data[0],))

                # Insert updated skills
                insert_skill_query = "INSERT INTO skill (job_seeker_id, skill_name) VALUES (%s, %s)"
                for skill in updated_skills:
                    cursor.execute(insert_skill_query, (user_data[0], skill))
            skills = updated_skills  # Update the context with new skills

    context = {
        'fname': user['fname'],
        'lname': user['lname'],
        'role': user['role'],
        'profile_picture_url': profile_picture_url,
        'skills': skills,
    }

    return render(request, 'profile.html', context)
