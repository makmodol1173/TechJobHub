from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = [
            'job_title', 'about', 'location',
            'responsibilities', 'education',
            'qualifications', 'deadline', 'job_type'
        ]
