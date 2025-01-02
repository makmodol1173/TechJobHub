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

    recent_rating = None
    average_rating = None
    job_title = None  # Variable to hold the job title

    with connection.cursor() as cursor:
        # Corrected query to get the most recent rating and corresponding job title
        query_recent_rating = """
            SELECT ass.mark, jp.title
            FROM job_post jp
            JOIN application app ON jp.job_post_id = app.job_post_id
            JOIN answers ans ON app.application_id = ans.application_id
            LEFT JOIN assessment ass ON ans.answer_id = ass.answer_id
            WHERE app.job_seeker_id = (
                SELECT job_seeker_id FROM job_seeker WHERE email = %s
            )
            ORDER BY ass.assessment_id DESC
            LIMIT 1
        """
        cursor.execute(query_recent_rating, (auth_token,))
        recent_rating_data = cursor.fetchone()  # Fetch the most recent rating data

        if recent_rating_data:
            recent_rating = recent_rating_data[0]  # Rating score
            job_title = recent_rating_data[1]  # Job title

        # Now fetch the average rating for the job seeker
        query_avg_rating = """
            SELECT AVG(ass.mark)
            FROM job_post jp
            JOIN application app ON jp.job_post_id = app.job_post_id
            JOIN answers ans ON app.application_id = ans.application_id
            LEFT JOIN assessment ass ON ans.answer_id = ass.answer_id
            WHERE app.job_seeker_id = (
                SELECT job_seeker_id FROM job_seeker WHERE email = %s
            )
        """
        cursor.execute(query_avg_rating, (auth_token,))
        avg_rating_data = cursor.fetchone()
        if avg_rating_data:
            average_rating = avg_rating_data[0]  # Average rating score

    # If no ratings found, return a message
    if not recent_rating:
        return render(request, 'rating.html', {
            'message': 'You have not received any ratings yet.',
            'role': role
        })

    # Render the rating page with the job seeker's ratings
    return render(request, 'rating.html', {
        'recent_rating': recent_rating,
        'average_rating': average_rating,
        'job_title': job_title,
        'role': role
    })
