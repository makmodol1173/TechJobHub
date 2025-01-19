from django.shortcuts import render, redirect
from django.contrib import messages
from decouple import config
from django.db import connection

def bookmarks(request):
  auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
  role = request.COOKIES.get(config('COOKIE_KEY_2'))

  if not auth_token or not role == 'job_seeker':
    return redirect('/login')
  
  job_post_id = request.GET.get('job_post_id')
  job_seeker_id=None
  with connection.cursor() as cursor:
    query_job_seeker = "SELECT job_seeker_id FROM job_seeker WHERE email = %s"
    cursor.execute(query_job_seeker, (auth_token,))
    job_seeker = cursor.fetchone()
    if job_seeker:
      job_seeker_id = job_seeker[0]
            
      query = """
        SELECT 
            c.name AS company_title,
            jp.title AS job_post_title,
            jp.job_post_id AS job_post_id
        FROM 
            bookmark b
        JOIN 
            job_post jp ON b.job_post_id = jp.job_post_id
        JOIN 
            company c ON jp.recruiter_id = c.recruiter_id
        WHERE 
            b.job_seeker_id = %s;
      """

    cursor.execute(query, (job_seeker_id,))
    data = cursor.fetchall()
    # if data:
    #   company_title, job_post_title = data[0] 
    #   user = {
    #     'company_title': company_title,
    #     'job_post_title': job_post_title,
    #   }
    
    query_job_post = "SELECT job_post_id FROM job_post WHERE job_post_id = %s"
    cursor.execute(query_job_post, (job_post_id,))
    job_post = cursor.fetchone()
    if not job_post:
      # messages.error(request, "Invalid Job Post")
      return render(request, 'bookmarks.html',{'bookmarks': data, 'role':role})
    job_post_id = job_post[0]
    
    query_bookmark = "SELECT * FROM bookmark WHERE job_seeker_id = %s AND job_post_id = %s"
    cursor.execute(query_bookmark, (job_seeker_id, job_post_id))
    bookmark = cursor.fetchone()
    if bookmark:
      messages.error(request, "Already Bookmarked")
      return render(request, 'bookmarks.html',{'bookmarks': data, 'role':role})
    
    if job_post_id and job_seeker_id:
      bookmark_insert_query = """INSERT INTO bookmark (job_seeker_id, job_post_id) VALUES (%s, %s)"""
      cursor.execute(bookmark_insert_query, (job_seeker_id, job_post_id))
      connection.commit()

      query = """
        SELECT 
            c.name AS company_title,
            jp.title AS job_post_title,
            jp.job_post_id AS job_post_id
        FROM 
            bookmark b
        JOIN 
            job_post jp ON b.job_post_id = jp.job_post_id
        JOIN 
            company c ON jp.recruiter_id = c.recruiter_id
        WHERE 
            b.job_seeker_id = %s;
      """

      cursor.execute(query, (job_seeker_id,))
      data = cursor.fetchall()

      messages.success(request, "Bookmark added successfully")
      return render(request, 'bookmarks.html',{'bookmarks': data, 'role':role})

      
  return render(request, 'bookmarks.html',{'bookmarks': data, 'role':role})

