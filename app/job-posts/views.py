from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def job_posts(request, job_post_id):
  with connection.cursor() as cursor:
    query_job_post = "SELECT * FROM job_post WHERE job_post_id = %s"
    cursor.execute(query_job_post, (job_post_id,))
    data = cursor.fetchone()
    
    user = {
                'title': data[2],
                'description': data[3],
                'key_responsibilities': data[4],
                'location': data[5],
                'educational_requirement': data[6],
                'deadline': data[7],
                'year_of_experience': data[8],
                'type': data[9]
            }
    print(user)
  
  return render(request, 'job-posts.html',user)
