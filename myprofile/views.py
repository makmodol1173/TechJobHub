from django.shortcuts import render
from .forms import ProfileForm, SkillForm, LanguageForm
from .models import Skill, Language

def profile_view(request):
    profile_form = ProfileForm()
    skill_form = SkillForm()
    language_form = LanguageForm()
    
    # Dummy data or actual user-specific data
    skills = Skill.objects.filter(user=request.user) if request.user.is_authenticated else []
    languages = Language.objects.filter(user=request.user) if request.user.is_authenticated else []
    
    context = {
        'profile_form': profile_form,
        'skill_form': skill_form,
        'language_form': language_form,
        'skills': skills,
        'languages': languages,
    }
    
    return render(request, 'profile.html', context)
