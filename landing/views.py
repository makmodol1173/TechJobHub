from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from new.models import Profile, Recruiter, JobSeeker, Company
from django.conf import settings
import os

def Home(request):
    return render(request, 'Home.html')

def Login(request):
    return render(request, 'Login.html')

def Signup(request):
    return render(request, 'Signup.html')

def Forget_pass(request):
    return render(request, 'Forget_pass.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

def Create_post(request):
    recruiter_id = request.COOKIES.get('user_id')
    role = request.COOKIES.get('role')

    if not recruiter_id or role != 'Recruiter':
        messages.error(request, "Only recruiters can create job posts.")
        return redirect('Login')
    return render(request, 'Create_post.html')

def Menu_options(request):
    return render(request, 'Menu_options.html')

def Bookmarks(request):
    return render(request, 'Bookmarks.html')

def Drop_resume(request):
    return render(request, 'Drop_resume.html')


def Profile(request):
    # Check if the user is logged in via cookies
    user_id = request.COOKIES.get('user_id')
    user_role = request.COOKIES.get('role')
    
    if not user_id or not user_role:
        messages.error(request, "User is not logged in.")
        return redirect('Login')  # Redirect to login page if cookies are missing
    
    # Determine the user type and fetch the respective model
    user = None
    if user_role == 'Recruiter':
        user = Recruiter.objects.filter(r_id=user_id).first()
    elif user_role == 'Job Seeker':
        user = JobSeeker.objects.filter(js_id=user_id).first()

    if not user:
        messages.error(request, "User not found.")
        return redirect('Login')

    # Handle file upload if there is a POST request with a file
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        uploaded_file = request.FILES['profile_picture']
        
        # Validate file type and size
        if uploaded_file.content_type not in ['image/jpeg', 'image/png']:
            messages.error(request, "Invalid file type. Only JPEG and PNG are allowed.")
            return redirect('Profile')

        if uploaded_file.size > 5 * 1024 * 1024:  # Limit to 5 MB
            messages.error(request, "File size exceeds the limit of 5 MB.")
            return redirect('Profile')

        # Save the file
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profile_picture'))
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Update the user's profile picture
        user.profile.profile_picture = file_url
        user.profile.save()

        messages.success(request, "Profile picture updated successfully!")
        return redirect('Profile')  # Redirect back to the profile page

    # If it's a GET request, render the profile page
    return render(request, 'Profile.html', {'user': user})

def Post(request):
    return render(request, 'Post.html')

def Applicant_list(request):
    return render(request, 'Applicant_list.html')

def Apply_list(request):
    return render(request, 'Apply_list.html')

def Assessment(request):
    return render(request, 'Assessment.html')

def Set_assessment(request):
    return render(request, 'Set_assessment.html')

def Assessment_mark(request):
    return render(request, 'Assessment_mark.html')

def Company_details(request):
    # if 'user_id' not in request.session and 'role' not in request.session:
        # ei khane check korte hobe role er value ('Job Seeker') ki nah
        # jodi na hoi taile login e redirect
        # both are same
    #     messages.error(request, "User is not logged in.")
    #     return redirect('Login')  # Redirect to login page
     return render(request, 'Company_details.html')

def Rating(request):
    return render(request, 'Rating.html')

def Rec_Job(request):
    return render(request, 'Rec_job.html')

def Set_Interview(request):
    return render(request, 'Set_Interview.html')

def Virtual_int(request):
    return render(request, 'Virtual_int.html')


# from .models import Job

# def job_list(request):
#     jobs = Job.objects.filter(is_active=True)
#     return render(request, 'job_list.html', {'jobs': jobs})

def logout(request):
    response = redirect('Login')  # Redirect to login page
    # Clear session data
    #request.session.flush()
    # Clear cookies
    response.delete_cookie('user_id')
    response.delete_cookie('role')
    
    messages.success(request, "You have been logged out.")
    return response
