from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from new.models import Question, JobSeeker, Application

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
                return redirect('drop_resume')
            else:
                messages.error(request, error_message)
        else:
            messages.error(request, "Please select a file to upload.")
    
    return render(request, 'Drop_resume.html', {
        'resume': job_seeker.resume if job_seeker.resume else None,
    })


def save_question(request):
    if request.method == "POST":
        
        app_id = request.POST.get('app_id')  # Assuming app_id is passed via the form

        try:
            application = Application.objects.get(app_id=app_id)
        except Application.DoesNotExist:
            raise Http404("Application not found")
        
        # Retrieve questions from the POST request
        question1 = request.POST.get('question1', '')
        question2 = request.POST.get('question2', '')
        question3 = request.POST.get('question3', '')
        question4 = request.POST.get('question4', '')
        question5 = request.POST.get('question5', '')
        question6 = request.POST.get('question6', '')
        question7 = request.POST.get('question7', '')
        question8 = request.POST.get('question8', '')
        question9 = request.POST.get('question9', '')
        question10 = request.POST.get('question10', '')

        # Save all questions as a single database entry
        Question.objects.create(
            application=application,
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            question5=question5,
            question6=question6,
            question7=question7,
            question8=question8,
            question9=question9,
            question10=question10
        )

        # Redirect to a success page or back to the form
        return redirect('Dashboard')  # Replace 'assessment' with the correct URL name for your success page

    return render(request, 'Set_assessment.html')  # Render the form


def set_assessment(request):
    # Assuming you are passing the application id when rendering the form
    app_id = request.GET.get('app_id')  # Example if you are passing it as a URL parameter
    return render(request, 'Set_assessment.html', {'app_id': app_id})

def dashboard(request):
    # Your dashboard logic here
    return render(request, 'Dashboard.html')