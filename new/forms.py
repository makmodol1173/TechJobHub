from django import forms
from .models import UserProfile, Skill

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'location']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']  
