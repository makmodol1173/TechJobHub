from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def set_assessment(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))
    job_post_id = request.GET.get("job_post_id")

    if not auth_token or role != 'recruiter':
        return redirect('/login')

    with connection.cursor() as cursor:
        query_recruiter = "SELECT recruiter_id FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter = cursor.fetchone()

        if not recruiter:
            return redirect('/login')

        recruiter_id = recruiter[0]

        query_job_post = """
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
        cursor.execute(query_job_post, (recruiter_id,))
        job_post = cursor.fetchall()

        if not job_post:
            messages.error(request, "No job post found for this recruiter.")
            return redirect('/dashboard')

    if request.method == 'POST':
        questions = [request.POST.get(f'question{i}') for i in range(1, 11)]

        if not any(questions) or not job_post_id:
            messages.error(request, "Please provide at least one question.")
            return render(request, 'set-assessment.html', {'question_range': range(1, 11), 'role':role, 'job_post': job_post})

        with connection.cursor() as cursor:

            query_job_post = "SELECT * FROM questions WHERE job_post_id = %s"
            cursor.execute(query_job_post, (job_post_id,))
            job_post_questions = cursor.fetchall()
            if not job_post_questions:
                insert_query = """
                    INSERT INTO questions (
                        job_post_id, question_1, question_2, question_3, question_4,
                        question_5, question_6, question_7, question_8, question_9, question_10
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (job_post_id, *questions))

                messages.success(request, "Assessment questions have been set successfully.")
        return redirect('/assessment-mark')

    return render(request, 'set-assessment.html', {'question_range': range(1, 11), 'role':role, 'job_post': job_post, 'job_post_id': job_post_id})
