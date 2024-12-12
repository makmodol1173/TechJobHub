from django.shortcuts import render

def company_details(request):
    return render(request, 'company-details.html')
