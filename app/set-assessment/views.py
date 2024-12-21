from django.shortcuts import render

def set_assessment(request):
    return render(request, 'set-assessment.html')
