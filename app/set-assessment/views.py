from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def set_assessment(request):
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

        query_job_post = "SELECT job_post_id FROM job_post WHERE recruiter_id = %s LIMIT 1"
        cursor.execute(query_job_post, (recruiter_id,))
        job_post = cursor.fetchone()

        if not job_post:
            messages.error(request, "No job post found for this recruiter.")
            return redirect('/dashboard')

        job_post_id = job_post[0]

    if request.method == 'POST':
        questions = [request.POST.get(f'question{i}') for i in range(1, 11)]

        if not any(questions):
            messages.error(request, "Please provide at least one question.")
            return render(request, 'set-assessment.html', {'question_range': range(1, 11), 'role':role})

        with connection.cursor() as cursor:
            insert_query = """
                INSERT INTO questions (
                    job_post_id, question_1, question_2, question_3, question_4,
                    question_5, question_6, question_7, question_8, question_9, question_10
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (job_post_id, *questions))

        messages.success(request, "Assessment questions have been set successfully.")
        return redirect('/assessment')

    return render(request, 'set-assessment.html', {'question_range': range(1, 11), 'role':role})
