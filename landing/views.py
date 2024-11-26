from django.shortcuts import render

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
    return render(request, 'Company_details.html')

def Rating(request):
    return render(request, 'Rating.html')

def Rec_Job(request):
    return render(request, 'Rec_job.html')

def Set_Interview(request):
    return render(request, 'Set_Interview.html')

def Virtual_int(request):
    return render(request, 'Virtual_int.html')


from .models import Job

def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'job_list.html', {'jobs': jobs})