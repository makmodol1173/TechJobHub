from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db import connection
from django.contrib import messages
import os
from decouple import config

def drop_resume(request):
  auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
  role = request.COOKIES.get(config('COOKIE_KEY_2'))

  if not auth_token or not role == 'job_seeker':
    return redirect('/login')

  with connection.cursor() as cursor:
      query_job_seeker = "SELECT job_seeker_id FROM job_seeker WHERE email = %s"
      cursor.execute(query_job_seeker, (auth_token,))
      job_seeker = cursor.fetchone()
      
      if not job_seeker:
        return redirect('/login')
      job_seeker_id = job_seeker[0]
    
  if request.method == 'POST':
    uploaded_file = request.FILES['resume']
    fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'resume'))
    filename = fs.save(uploaded_file.name, uploaded_file)
    with connection.cursor() as cursor:
      update_query = "UPDATE job_seeker SET resume = %s WHERE job_seeker_id = %s"
      cursor.execute(update_query, (filename, job_seeker_id))
      connection.commit()
      messages.success(request,"Resume uploaded successfully.")
  return render(request, 'drop-resume.html')