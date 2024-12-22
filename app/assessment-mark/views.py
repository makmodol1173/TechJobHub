from django.shortcuts import render

def assessment_mark(request):
    return render(request, 'assessment-mark.html')
