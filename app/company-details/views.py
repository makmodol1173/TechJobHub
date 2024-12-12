from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config

def company_details(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token or not role == 'recruiter':
        return redirect('/login')

    if request.method == 'POST':
      company_name = request.POST.get('company-name')
      address = request.POST.get('address')
      trade_license = request.POST.get('license')
      website = request.POST.get('website')
      
      if not company_name or not address:
        messages.error(request, "Please filled required field!")
        return render(request, 'company-details.html')
      
      with connection.cursor() as cursor:
        query_recruiter = "SELECT recruiter_id FROM recruiter WHERE email = %s"
        cursor.execute(query_recruiter, (auth_token,))
        recruiter = cursor.fetchone()

        if not recruiter:
            return redirect('/login')
          
        recruiter_id = recruiter[0]
        insert_query = """
                    INSERT INTO company (recruiter_id, name, address, trade_license_number, website_url) 
                    VALUES (%s, %s, %s, %s, %s)
                """
        cursor.execute(insert_query, (recruiter_id, company_name, address, trade_license, website))
        connection.commit()
        return redirect('/dashboard')

    return render(request, 'company-details.html')
