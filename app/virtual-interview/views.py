from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.dateparse import parse_date, parse_time

def virtual_interview(request):
    # Fetching all applicant emails from the job_seeker table
    with connection.cursor() as cursor:
        cursor.execute("SELECT email FROM job_seeker")
        applicant_emails = [row[0] for row in cursor.fetchall()]

    if request.method == 'POST':
        # Collect form data
        applicant_email = request.POST.get('applicant-email')  # This will be selected by the user from the dropdown
        interview_date = parse_date(request.POST.get('set-date'))
        interview_time = parse_time(request.POST.get('set-time'))
        meet_link = request.POST.get('meet-link')

        # Validate that the email exists in the job_seeker table
        with connection.cursor() as cursor:
            cursor.execute("SELECT email FROM job_seeker WHERE email = %s", [applicant_email])
            email_exists = cursor.fetchone()

        if not email_exists:
            messages.error(request, "Applicant email does not exist in the database!")
            return redirect('/virtual-interview/')

        # Insert interview details into the interview table
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO interview (email, interview_date, interview_time, meet_link)
                VALUES (%s, %s, %s, %s)
            """, [applicant_email, interview_date, interview_time, meet_link])

        # Send email to the applicant with the interview details
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

    # Render the template with dynamic email data
    return render(request, 'virtual-interview.html', {'applicant_emails': applicant_emails})
