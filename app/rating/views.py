from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def rating(request):
    # Get the auth token and role from cookies
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    # Ensure the user is logged in
    if not auth_token:
        return redirect('/login')

    # Ensure role is 'job_seeker'
    if role != 'job_seeker':
        return redirect('/login')

    ratings_data = []  # Initialize the ratings data

    with connection.cursor() as cursor:
        # Corrected query to get job seeker information and their corresponding assessment ratings
        query_job_seeker = """
            SELECT jp.title AS job_title, ass.mark
            FROM job_post jp
            JOIN application app ON jp.job_post_id = app.job_post_id
            JOIN answers ans ON app.application_id = ans.application_id
            LEFT JOIN assessment ass ON ans.answer_id = ass.answer_id
            WHERE app.job_seeker_id = (
                SELECT job_seeker_id FROM job_seeker WHERE email = %s
            )
        """
        cursor.execute(query_job_seeker, (auth_token,))
        ratings_data = cursor.fetchall()

    # If no ratings found, return a message
    if not ratings_data:
        return render(request, 'rating.html', {
            'message': 'You have not received any ratings yet.',
            'role': role
        })

    # Render the rating page with the job seeker's ratings
    return render(request, 'rating.html', {
        'ratings': ratings_data,
        'role': role
    })
