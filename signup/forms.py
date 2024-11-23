from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    fname = forms.CharField(label="First Name", max_length=50)
    lname = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    role = forms.ChoiceField(choices=[('Recruiter', 'Recruiter'), ('Startup', 'Startup'), ('Job Seeker', 'Job Seeker')], label="Role")

    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'password']
