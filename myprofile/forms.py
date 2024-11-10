from django import forms
from .models import Profile, Skill, Language

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'study_field', 'university', 'location', 'profile_picture', 'cover_photo', 'profile_url']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language_name']
