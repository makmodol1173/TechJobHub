# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import UserProfile, Skill
# # from .forms import ProfileForm, SkillForm

# @login_required
# def profile_view(request):
#     user_profile = get_object_or_404(UserProfile, user=request.user)

#     profile_form = ProfileForm(instance=user_profile)
#     skill_form = None

#     if user_profile.role == "job_seeker":
#         skill_form = SkillForm()

#     if request.method == "POST":
#         if 'profile_submit' in request.POST: 
#             profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
#             if profile_form.is_valid():
#                 profile_form.save()
#                 return redirect('profile') 

#         elif 'skill_submit' in request.POST and user_profile.role == "job_seeker":
#             skill_form = SkillForm(request.POST)
#             if skill_form.is_valid():
#                 skill = skill_form.save(commit=False)
#                 skill.save()
#                 user_profile.skills.add(skill)
#                 return redirect('profile') 

#     context = {
#         'user_profile': user_profile,
#         'profile_form': profile_form,
#         'skill_form': skill_form,
#     }
#     return render(request, 'Profile.html', context)

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import JobPostForm

# @login_required
# def create_job_post(request):
#     if request.method == 'POST':
#         form = JobPostForm(request.POST)
#         if form.is_valid():
#             job_post = form.save(commit=False)
#             job_post.recruiter = request.user  # Assuming the user is the recruiter
#             job_post.save()
#             return redirect('Dashboard')  # Replace with the actual name of your dashboard view
#     else:
#         form = JobPostForm()
#     return render(request, 'Create_post.html', {'form': form})
from django.shortcuts import render, redirect
from .models import JobPost
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

@login_required
def create_job_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Updated to match form field name
        description = request.POST.get('description')  # Updated to match form field name
        location = request.POST.get('location')
        responsibilities = request.POST.get('key_responsibilities')  # Updated to match form field name
        education = request.POST.get('education_requirement')  # Updated to match form field name
        qualifications = request.POST.get('years_experience')  # Updated to match form field name
        deadline = request.POST.get('deadline')
        job_type = request.POST.get('job_type')  # Updated to match form field name

        # Ensure that the recruiter is the logged-in user (assuming 'Recruiter' is related to user)
        recruiter = request.user  # Assuming you are directly using the user as the recruiter

        # Save to the database
        JobPost.objects.create(
            recruiter=recruiter,  # Associate the current user as the recruiter
            title=title,
            description=description,
            location=location,
            key_responsibilities=responsibilities,
            education_requirement=education,
            years_experience=qualifications,  # Assuming this field is experience years
            deadline=deadline,
            job_type=job_type,
            created_at=now(),
        )

        return redirect('Dashboard')  # Redirect to the dashboard after successful submission

    return render(request, 'Create_post.html')
