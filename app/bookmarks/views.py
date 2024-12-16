from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.db import connection

def bookmarks(request):
    job_post_id = request.GET.get('job_post_id')
    job_seeker_id = request.GET.get('job_seeker_id')

    with connection.cursor() as cursor:
      query_job_seeker = "SELECT * FROM job_seeker WHERE job_seeker_id = %s"
      cursor.execute(query_job_seeker, (job_seeker_id,))
      job_seeker = cursor.fetchone()
      if job_seeker is None:
          return redirect(f"/job-posts/{job_post_id}?message='Invalid Request'")
      
      query_job_post = "SELECT * FROM job_post WHERE job_post_id = %s"
      cursor.execute(query_job_post, (job_post_id,))
      job_post = cursor.fetchone()
      if job_post is None:
          return redirect(f"/job-posts/{job_post_id}?message='Invalid Request'")
      
      query_application = "SELECT * FROM bookmarks WHERE job_seeker_id = %s & job_post_id = %s"
      cursor.execute(query_application, (job_seeker_id, job_post_id))
      application = cursor.fetchone()
      if application:
          return redirect(f"/bookmarks/{job_post_id}?message='Already bookmarked'")
          
      job_seeker_insert_query = """INSERT INTO bookmarks (job_seeker_id, job_post_id) VALUES (%s, %s)"""
      cursor.execute(job_seeker_insert_query, (job_seeker_id, job_post_id))
      connection.commit()
    return redirect(f"/job-posts/{job_post_id}?message='Applied Successful'")
      