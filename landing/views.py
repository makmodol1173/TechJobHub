from django.shortcuts import render, redirect
from django.contrib import messages
from new.models import Profile, Recruiter, JobSeeker, Company

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
    return render(request, 'Create_post.html')

def Menu_options(request):
    return render(request, 'Menu_options.html')

def Bookmarks(request):
    return render(request, 'Bookmarks.html')

def Drop_resume(request):
    return render(request, 'Drop_resume.html')

def Profile(request):
        # default get method
        # eikhane role check kora ta khub beshi important nah, but por e kaj e lagbe
        # ei khane check korte hobe role er value ('Job Seeker') ki nah
        # jodi na hoi taile login e redirect
        # both are same
    # if 'user_id' not in request.session:
    #     messages.error(request, "User is not logged in.")
    #     return redirect('Login')  # Redirect to login page
    
    # user_id = request.session.get('user_id')
    # user_role = request.session.get('role')
    # #print(user_email)
    # #print(user_role)

    # if(user_role=='Recruiter'):
    #     recruiter = Recruiter.objects.filter(r_id=user_id).first()
    #     print(recruiter)

    # if Recruiter.objects.filter(email=email).exists():
    #             messages.error(request, "Email already registered!")
    #             return redirect('Signup')

    return render(request, 'Profile.html')

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
