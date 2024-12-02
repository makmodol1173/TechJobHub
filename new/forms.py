# from django import forms
# from .models import UserProfile, Skill

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['profile_picture', 'location']

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         fields = ['name']  

from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'key_responsibilities', 'education_requirements', 'qualifications_experience', 'deadline', 'job_type']
