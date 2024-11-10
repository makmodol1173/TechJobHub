from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'description', 'company', 'location', 'category',
            'educational_requirements', 'deadline', 'work_modality',
            'job_type', 'about_us', 'role_overview', 'key_responsibilities',
            'qualification_experience', 'is_active'
        ]
