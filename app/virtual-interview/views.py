from django.shortcuts import render

def virtual_interview(request):
    return render(request, 'virtual-interview.html')