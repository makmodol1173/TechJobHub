from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def assessment(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token or role != 'job_seeker':
        return redirect('/login')

    with connection.cursor() as cursor:
        query_job_seeker = "SELECT job_seeker_id FROM job_seeker WHERE email = %s"
        cursor.execute(query_job_seeker, (auth_token,))
        job_seeker = cursor.fetchone()
        
        if not job_seeker:
            return redirect('/login')

        job_seeker_id = job_seeker[0]
        job_post_id = request.GET.get('job_post_id')

    #     query_job_post = """
    #         SELECT job_post_id
    #         FROM application
    #         WHERE job_seeker_id = %s
    #         LIMIT 1
    #     """
        
    #     cursor.execute(query_job_post, (job_seeker_id,))
    #     job_post = cursor.fetchone()

    #     if not job_post:
    #         messages.error(request, "No application found for this job seeker.")
    #         return redirect('/dashboard')

    #     job_post_id = job_post[0]
    #     print(job_post_id)

        query_questions = """
            SELECT question_1, question_2, question_3, question_4, question_5,
                   question_6, question_7, question_8, question_9, question_10
            FROM questions
            WHERE job_post_id = %s
        """
        cursor.execute(query_questions, (job_post_id,))
        questions_data = cursor.fetchone()

    # if not questions_data:
    #     messages.error(request, "No questions found for this job post.")
    #     return redirect('/set-assessment')

    print(questions_data)
    print(job_post_id)
    print(job_seeker_id)
    questions=None
    if not questions_data:
        return redirect("/application-list")
    else:
        questions = [q for q in questions_data if q] 


    # if request.method == 'POST':
    #     answers = [request.POST.get(f'question-{i + 1}') for i in range(len(questions))]

    #     if not all(answers):
    #         messages.error(request, "Please provide answers to all the questions.")
    #         return render(request, 'assessment.html', {'questions': questions})

    #     with connection.cursor() as cursor:
    #         insert_answers_query = """
    #             INSERT INTO answers (
    #                 application_id, answer_1, answer_2, answer_3, answer_4,
    #                 answer_5, answer_6, answer_7, answer_8, answer_9, answer_10
    #             ) VALUES (
    #                 (SELECT application_id FROM application WHERE job_seeker_id = %s AND job_post_id = %s LIMIT 1),
    #                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    #             )
    #         """
    #         cursor.execute(insert_answers_query, (job_seeker_id, job_post_id, *answers))

    #     messages.success(request, "Your answers have been submitted successfully.")
    #     return redirect('/assessment-mark')

    return render(request, 'assessment.html', {'questions': questions, 'role':role})
