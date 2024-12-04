from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from new.models import Profile, Recruiter, JobSeeker, Company, JobPost
from django.http import Http404
from django.contrib.auth.decorators import login_required

def signaction(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        if role == 'Recruiter':
            if Recruiter.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect('Signup')

            recruiter = Recruiter(fname=fname, lname=lname, email=email)
            recruiter.set_password(password)
            recruiter.save()
            # request.session['user_id'] = recruiter.r_id
            # request.session['role'] = 'Recruiter'
            response = redirect('company_details')  # Redirect to page
            response.set_cookie('user_id', recruiter.r_id)
            response.set_cookie('role', 'Recruiter')
            messages.success(request, "Recruiter registered successfully!")
            return response

        elif role == 'Job Seeker':
            if JobSeeker.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect('Signup')

            job_seeker = JobSeeker(fname=fname, lname=lname, email=email)
            job_seeker.set_password(password)
            job_seeker.save()

            response = redirect('Dashboard')  # Redirect to login page
            response.set_cookie('user_id', job_seeker.js_id)
            response.set_cookie('role', 'Job Seeker')
            # request.session['user_id'] = job_seeker.j_id
            # request.session['role'] = 'Job Seeker'

            messages.success(request, "Job Seeker registered successfully!")
            return response

    return render(request, 'Signup.html')

def loginaction(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        recruiter = Recruiter.objects.filter(email=email).first()
        if recruiter and recruiter.check_password(password):
            if recruiter.company_details_filled:
                response = redirect('Dashboard')  # Redirect to the dashboard
            else:
                response = redirect('company_details')
            response.set_cookie('user_id', recruiter.r_id)
            response.set_cookie('role', 'Recruiter')
            return response

        job_seeker = JobSeeker.objects.filter(email=email).first()
        if job_seeker and job_seeker.check_password(password):
            response = redirect('Dashboard')  # Redirect to dashboard
            response.set_cookie('user_id', job_seeker.js_id)
            response.set_cookie('role', 'Job Seeker')
            return response
        messages.error(request, "Invalid email or password.")
        return redirect('Login')

    return render(request, 'Login.html')

    
# def logout(request):
#     request.session.flush()  # Clears the session
#     messages.success(request, "You have been logged out.")
#     return redirect('Login')

def create_company(request):
    if request.method == 'POST':
        # Check if user cookies are available
        user_id = request.COOKIES.get('user_id')
        role = request.COOKIES.get('role')

        # Check if session data is available
        if not user_id or role != 'Recruiter':
            messages.error(request, "User is not logged in.")
            return redirect('Login')  

        # Get the data from the form
        company_name = request.POST['company-name']
        address = request.POST['address']
        trade_license = request.POST.get('license', '')
        website = request.POST.get('website', '')

        try:
            recruiter = Recruiter.objects.get(r_id=user_id)
        except Recruiter.DoesNotExist:
            messages.error(request, "Recruiter not found.")
            return redirect('Login')
        
        # Create and save the Company object
        company = Company(
            recruiter=recruiter,
            name=company_name,
            address=address,
            trade_license_number=trade_license,
            description=website 
        )
        company.save()
        
        # Set a cookie to indicate that the company has been created
        response = redirect('Create_post')
        response.set_cookie('company_created', 'True', max_age=365 * 24 * 60 * 60)
        messages.success(request, "Company created successfully!")
        return response

    return render(request, 'company_details.html')


def profile_view(request):
    # Retrieve user details from cookies
    user_id = request.COOKIES.get('user_id')
    role = request.COOKIES.get('role')
    print(user_id)
    print(role)

    if not user_id or not role:
        messages.error(request, "You need to log in to view your profile.")
        return redirect('Login')  # Redirect to login page

    user = None
    if role == 'Recruiter':
        try:
            user = Recruiter.objects.get(r_id=user_id)
        except Recruiter.DoesNotExist:
            messages.error(request, "Recruiter not found. Please log in again.")
            return redirect('Login')
    elif role == 'Job Seeker':
        try:
            user = JobSeeker.objects.get(js_id=user_id)
        except JobSeeker.DoesNotExist:
            messages.error(request, "Job Seeker not found. Please log in again.")
            return redirect('Login')

    # Pass user data to the template
    print(user)
    print(role)
    return render(request, 'profile.html', {'user': user, 'role': role})


from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from new.models import JobPost, Recruiter

def create_post(request):
    if request.method == 'POST':
        # Retrieve recruiter details from cookies
        recruiter_id = request.COOKIES.get('user_id')
        role = request.COOKIES.get('role')

        if not recruiter_id or role != 'Recruiter':
            messages.error(request, "Only recruiters can create job posts.")
            return redirect('Login')

        # Collect form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        key_responsibilities = request.POST.get('key_responsibilities')
        education_requirement = request.POST.get('education_requirement', '')
        years_experience = request.POST.get('years_experience', '0')
        deadline = request.POST.get('deadline')
        job_type = request.POST.get('job_type')

        try:
            recruiter = Recruiter.objects.get(r_id=recruiter_id)
        except Recruiter.DoesNotExist:
            messages.error(request, "Recruiter not found.")
            return redirect('Login')

        # Convert the deadline string to a date object
        try:
            deadline_date = datetime.strptime(deadline, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid deadline format.")
            return redirect('create-post')

        # Create the job post
        job_post = JobPost(
            recruiter=recruiter,
            title=title,
            description=description,
            location=location,
            key_responsibilities=key_responsibilities,
            education_requirement=education_requirement,
            years_experience=years_experience,
            deadline=deadline,
            job_type=job_type,
        )
        job_post.save()

        messages.success(request, "Job post created successfully!")
        return redirect('Dashboard')  # Redirect to the dashboard or any appropriate page

    return render(request, 'Create_post.html')

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


def drop_resume(request):
    # Manually authenticate the user
    user_id = request.COOKIES.get('user_id')
    role = request.COOKIES.get('role')

    if not user_id or role != 'Job Seeker':
        messages.error(request, "You must be logged in as a Job Seeker to upload a resume.")
        return redirect('Login')  # Redirect to login page if not authenticated

    try:
        job_seeker = JobSeeker.objects.get(js_id=user_id)
    except JobSeeker.DoesNotExist:
        raise Http404("JobSeeker profile not found.")

    if request.method == 'POST':
        if 'resume' in request.FILES:
            resume_file = request.FILES['resume']
            valid, error_message = is_valid_resume(resume_file)
            if valid:
                job_seeker.resume = resume_file
                job_seeker.save()  # Save the JobSeeker instance to update the resume field
                messages.success(request, "Resume uploaded successfully!")
                return redirect('drop_resume')
            else:
                messages.error(request, error_message)
        else:
            messages.error(request, "Please select a file to upload.")

    return render(request, 'Drop_resume.html', {
        'resume': job_seeker.resume.url if job_seeker.resume else None,
    })
