from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Skill
from .forms import ProfileForm, SkillForm

@login_required
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    profile_form = ProfileForm(instance=user_profile)
    skill_form = None

    if user_profile.role == "job_seeker":
        skill_form = SkillForm()

    if request.method == "POST":
        if 'profile_submit' in request.POST: 
            profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile') 

        elif 'skill_submit' in request.POST and user_profile.role == "job_seeker":
            skill_form = SkillForm(request.POST)
            if skill_form.is_valid():
                skill = skill_form.save(commit=False)
                skill.save()
                user_profile.skills.add(skill)
                return redirect('profile') 

    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
        'skill_form': skill_form,
    }
    return render(request, 'Profile.html', context)
