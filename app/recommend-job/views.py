from django.shortcuts import render

def recommend_job(request):
  return render(request, 'recommend-job.html')
