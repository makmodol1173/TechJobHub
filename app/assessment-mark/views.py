from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def assessment_mark(request):
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

        query_answers = """
            SELECT a.answer_id, a.answer_1, a.answer_2, a.answer_3, 
                   a.answer_4, a.answer_5, a.answer_6, a.answer_7, 
                   a.answer_8, a.answer_9, a.answer_10
            FROM answers a
            WHERE a.application_id = %s
        """
        # FIXED APPLICATION ID
        cursor.execute(query_answers,4)
        answers_data = cursor.fetchall()

        if not answers_data:
            messages.error(request, "No answers available for marking.")
            return redirect('/dashboard')

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

    return render(request, 'assessment-mark.html', {'answers': answers_data, 'role':role})
