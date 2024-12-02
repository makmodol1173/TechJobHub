from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from new.models import Profile, Recruiter, JobSeeker, Company

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
            response = redirect('Login')  # Redirect to page
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

            response = redirect('Login')  # Redirect to login page
            response.set_cookie('user_id', job_seeker.js_id)
            response.set_cookie('role', 'Job Seeker')
            # request.session['user_id'] = job_seeker.j_id
            # request.session['role'] = 'Job Seeker'

            messages.success(request, "Job Seeker registered successfully!")
            return response

    return render(request, 'Signup.html')

def loginaction(request):
    #if request.COOKIES.get('user_id') and request.COOKIES.get('role'):
        # If cookies are already set, redirect to profile
        #return redirect('profile')
     
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        recruiter = Recruiter.objects.filter(email=email).first()
        if recruiter and recruiter.check_password(password):
            # request.session['user_id'] = recruiter.r_id
            # request.session['role'] = 'Recruiter'
            response = redirect('company_details')  # Redirect to profile
            response.set_cookie('user_id', recruiter.r_id)
            response.set_cookie('role', 'Recruiter')
            return response

        job_seeker = JobSeeker.objects.filter(email=email).first()
        if job_seeker and job_seeker.check_password(password):
            # request.session['user_id'] = job_seeker.js_id
            # request.session['role'] = 'Job Seeker'
            response = redirect('Dashboard')  # Redirect to d
            response.set_cookie('user_id', job_seeker.js_id)
            response.set_cookie('role', 'Job Seeker')
            return response
        messages.error(request, "Invalid email or password.")
        return redirect('Login')

    return render(request, 'Login.html')

# class AuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         user_id = request.session.get('user_id')
#         if user_id:
#             role = request.session.get('role')
#             if role == 'Recruiter':
#                 request.user = Recruiter.objects.filter(r_id=user_id).first()
#             elif role == 'Job Seeker':
#                 request.user = JobSeeker.objects.filter(js_id=user_id).first()
#         else:
#             request.user = None
#         return self.get_response(request)
    
def logout(request):
    request.session.flush()  # Clears the session
    messages.success(request, "You have been logged out.")
    return redirect('Login')

def create_company(request):
    if request.method == 'POST':
        # Check if user cookies are available
        user_id = request.COOKIES.get('user_id')
        role = request.COOKIES.get('role')

        # Check if session data is available
        if not user_id or role != 'Recruiter':
            messages.error(request, "User is not logged in.")
            return redirect('Login')  # Redirect to login page

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
            description=website  # You can store website URL in description or create a new field if needed
        )
        company.save()
        
        # Show a success message and redirect to the create post page
       # messages.success(request, "Company created successfully!")
        return redirect('Create_post')  # Ensure Create_post URL is mapped correctly
    else:
        return render(request, 'company_details.html')



def profile_view(request):
    # Retrieve user details from cookies
    user_id = request.COOKIES.get('user_id')
    role = request.COOKIES.get('role')

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
    return render(request, 'profile.html', {'user': user, 'role': role})
