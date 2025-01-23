from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def assessment_mark(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))
    job_post_id = request.GET.get("job_post_id")
    job_seeker_id = request.GET.get("job_seeker_id")
    job_seekers = answers_data = None

    if not auth_token or role != 'recruiter':
        return redirect('/login')

    with connection.cursor() as cursor:
        query_recruiter = "SELECT recruiter_id FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter = cursor.fetchone()
        if not recruiter:
            return redirect('/login')

        recruiter_id = recruiter[0]

        if recruiter_id: 
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
        
        if job_post_id:

            query_job_seekers = """
                SELECT DISTINCT
                    js.job_seeker_id,
                    js.fname AS first_name,
                    js.lname AS last_name,
                    js.email AS email,
                    js.resume AS resume
                FROM 
                    job_post jp
                JOIN 
                    application a ON jp.job_post_id = a.job_post_id
                JOIN 
                    job_seeker js ON a.job_seeker_id = js.job_seeker_id
                WHERE 
                    jp.job_post_id = %s;
            """

            cursor.execute(query_job_seekers, job_post_id)
            job_seekers = cursor.fetchall()

        if job_seeker_id and job_post_id:
            query_answers = """
                SELECT a.answer_id, a.answer_1, a.answer_2, a.answer_3, 
                       a.answer_4, a.answer_5, a.answer_6, a.answer_7, 
                       a.answer_8, a.answer_9, a.answer_10
                FROM answers a
                JOIN application ap ON ap.application_id = a.application_id
                WHERE ap.job_seeker_id = %s AND ap.job_post_id = %s
            """
            
            # Assuming cursor is already created and connected to your database
            cursor.execute(query_answers, (job_seeker_id, job_post_id))
            answers_data = cursor.fetchall()
            print(answers_data)


        # if not answers_data:
        #     messages.error(request, "No answers available for marking.")
        #     return redirect('/dashboard')

        if request.method == 'POST':
            marks = request.POST.get('marks')
            answer_id = request.POST.get('answer_id')

            if not marks or not answer_id:
                messages.error(request, "Please provide marks.")
                return render(request, 'assessment-mark.html', {'answers': answers_data})

            query = "SELECT * FROM assessment WHERE answer_id = %s"
            cursor.execute(query, (answer_id,))
            assessment = cursor.fetchone()
            if not assessment:
                insert_marks_query = """
                    INSERT INTO assessment (answer_id, mark)
                    VALUES (%s, %s)
                """
                cursor.execute(insert_marks_query, (answer_id, marks))

                messages.success(request, "Marks have been saved successfully.")
                return redirect('/dashboard')

    return render(request, 'assessment-mark.html', {'answers':answers_data,'job_post': job_post, 'role':role, 'job_post_id':job_post_id, 'job_seekers': job_seekers, 'job_seeker_id':job_seeker_id })
