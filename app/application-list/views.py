from django.shortcuts import render, redirect
from django.db import connection
from decouple import config

def application_list(request):
  auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
  with connection.cursor() as cursor:
    query_job_seeker = "SELECT job_seeker_id FROM job_seeker WHERE email = %s"
    cursor.execute(query_job_seeker, (auth_token,))
    job_seeker = cursor.fetchone()
    if job_seeker:
      job_seeker_id = job_seeker[0]

      query = """
                SELECT DISTINCT 
                    jp.job_post_id, 
                    jp.title, 
                    jp.description, 
                    jp.key_responsibilities, 
                    jp.deadline, 
                    c.name AS company_name
                FROM skill s
                JOIN job_seeker js ON s.job_seeker_id = js.job_seeker_id
                JOIN job_post jp ON 
                    jp.description LIKE CONCAT('%%', s.skill_name, '%%') OR
                    jp.key_responsibilities LIKE CONCAT('%%', s.skill_name, '%%')
                JOIN recruiter r ON jp.recruiter_id = r.recruiter_id
                JOIN company c ON r.recruiter_id = c.recruiter_id
                WHERE js.job_seeker_id = %s;
            """
      cursor.execute(query, (job_seeker_id,))
      data = cursor.fetchall()
  return render(request, 'application-list.html', {'jobs':data})
