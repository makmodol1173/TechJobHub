from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def rating(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token:
        return redirect('/login')

    if role != 'job_seeker':
        return redirect('/login')

    recent_rating = None
    average_rating = None
    job_title = None
    has_high_rating = False

    with connection.cursor() as cursor:
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
        recent_rating_data = cursor.fetchone()
        if recent_rating_data:
            recent_rating, job_title = recent_rating_data

    with connection.cursor() as cursor:
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
            average_rating = avg_rating_data[0]

    if average_rating and average_rating >= 7.0:
        has_high_rating = True

    context = {
        'role': role,
        'recent_rating': recent_rating,
        'average_rating': average_rating,
        'job_title': job_title,
        'has_high_rating': has_high_rating,
    }

    return render(request, 'rating.html', context)
