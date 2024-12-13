from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def job_posts(request, job_post_id):
  auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
  role = request.COOKIES.get(config('COOKIE_KEY_2'))
  message = request.GET.get('message')
  # if not auth_token or not role == 'job_seeker':
  #   messages.error(request,"Invalid user")
  job_seeker_id=None
  with connection.cursor() as cursor:
    query_job_seeker = "SELECT job_seeker_id FROM job_seeker WHERE email = %s"
    cursor.execute(query_job_seeker, (auth_token,))
    job_seeker = cursor.fetchone()
    if job_seeker:
            job_seeker_id = job_seeker[0]
            
  #   if not role == "job_seeker":
  #     messages.error(request,"Invalid role")
      

  with connection.cursor() as cursor:
    query_job_post = """SELECT 
      jp.job_post_id,
      jp.title,
      jp.description,
      jp.key_responsibilities,
      jp.location,
      jp.educational_requirement,
      jp.deadline,
      jp.year_of_experience,
      jp.type AS job_type,
      jp.keywords,
      c.company_id,
      c.name AS company_name,
      c.address AS company_address,
      c.description AS company_description,
      c.trade_license_number,
      c.website_url
    FROM 
      job_post jp
    LEFT JOIN 
      company c ON jp.recruiter_id = c.recruiter_id
    WHERE 
      jp.job_post_id = %s;
    """
    cursor.execute(query_job_post, (job_post_id,))
    data = cursor.fetchone()
    user = {
                'title': data[1],
                'description': data[2],
                'key_responsibilities': data[3],
                'location': data[4],
                'educational_requirement': data[5],
                'deadline': data[6],
                'year_of_experience': data[7],
                'type': data[8],
                'company_name': data[11],
                'job_post_id': data[0],
                'job_seeker_id': job_seeker_id,
                'message': message
            }
  
  return render(request, 'job-posts.html',user)
