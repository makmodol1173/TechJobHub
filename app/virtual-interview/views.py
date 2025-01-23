from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.dateparse import parse_date, parse_time
from decouple import config

def virtual_interview(request):
    role = request.COOKIES.get(config('COOKIE_KEY_2'))
    job_seeker_id = request.GET.get('job_seeker_id')
    print(job_seeker_id)

    if not job_seeker_id:
        return redirect('/applicant-list')
    
    with connection.cursor() as cursor:
        query = "SELECT * FROM job_seeker WHERE job_seeker_id = %s"
        cursor.execute(query, (job_seeker_id))
        job_seeker = cursor.fetchone()
        applicant_emails = job_seeker[3]
    

    if request.method == 'POST':
        applicant_email = request.POST.get('applicant-email') 
        interview_date = parse_date(request.POST.get('set-date'))
        interview_time = parse_time(request.POST.get('set-time'))
        meet_link = request.POST.get('meet-link')

        with connection.cursor() as cursor:
            cursor.execute("SELECT email FROM job_seeker WHERE email = %s", [applicant_email])
            email_exists = cursor.fetchone()

        if not email_exists:
            messages.error(request, "Applicant email does not exist in the database!")
            return redirect('/virtual-interview/')

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO interview (email, interview_date, interview_time, meet_link)
                VALUES (%s, %s, %s, %s)
            """, [applicant_email, interview_date, interview_time, meet_link])

        subject = "Virtual Interview Invitation - TechJobHub"
        message = f"""
        Dear Applicant,

        Your virtual interview has been scheduled as follows:

        Date: {interview_date}
        Time: {interview_time}
        Meeting Link: {meet_link}

        Please click the link above to join the meeting at the specified time.

        Best regards,
        TechJobHub Team
        """
        send_mail(
            subject,
            message,
            'makmodol1173@gmail.com',
            [applicant_email]
        )

        messages.success(request, "Invitation email sent successfully!")
        return redirect('/virtual-interview/')

    return render(request, 'virtual-interview.html', {'applicant_emails': applicant_emails, 'role':role})
