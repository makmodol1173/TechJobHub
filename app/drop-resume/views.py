from django.shortcuts import render

def drop_resume(request):
  return render(request, 'drop-resume.html')
