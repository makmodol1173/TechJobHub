from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .models import JobSeeker

def is_valid_resume(file):

    valid_mime_types = [
        'application/pdf', 
        'application/msword', 
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]
    valid_extensions = ['.pdf', '.doc', '.docx']
    max_file_size = 5 * 1024 * 1024  # 5MB

    if file.content_type not in valid_mime_types:
        return False, "Invalid file type. Only PDF and Word documents are allowed."
    if not any(file.name.endswith(ext) for ext in valid_extensions):
        return False, "Invalid file extension. Please upload a .pdf, .doc, or .docx file."
    if file.size > max_file_size:
        return False, "File size exceeds 5MB limit."
    return True, None

@login_required
def drop_resume(request):
    try:
        job_seeker = JobSeeker.objects.get(email=request.user.email)
    except JobSeeker.DoesNotExist:
        raise Http404("JobSeeker profile not found.")
    
    if request.method == 'POST':
        if 'resume' in request.FILES:
            resume_file = request.FILES['resume']
            valid, error_message = is_valid_resume(resume_file)
            if valid:
                job_seeker.resume = resume_file
                job_seeker.save()
                messages.success(request, "Resume uploaded successfully!")
                return redirect('Drop_resume')
            else:
                messages.error(request, error_message)
        else:
            messages.error(request, "Please select a file to upload.")
    
    return render(request, 'Drop_resume.html', {
        'resume': job_seeker.resume if job_seeker.resume else None,
    })
