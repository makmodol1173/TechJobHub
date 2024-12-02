# from django import forms
# from django.contrib.auth.models import User

# class UserRegistrationForm(forms.ModelForm):
#     fname = forms.CharField(label="First Name", max_length=50)
#     lname = forms.CharField(label="Last Name", max_length=50)
#     email = forms.EmailField(label="Email")
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
#     role = forms.ChoiceField(choices=[('Recruiter', 'Recruiter'), ('Job Seeker', 'Job Seeker')], label="Role")

#     class Meta:
#         model = User
#         fields = ['fname', 'lname', 'email', 'password']

# from django import forms

# class UserRegistrationForm(forms.Form):
#     fname = forms.CharField(max_length=30, required=True, label="First Name")
#     lname = forms.CharField(max_length=30, required=True, label="Last Name")
#     email = forms.EmailField(required=True, label="Email")
#     password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
#     role = forms.ChoiceField(
#         choices=[("Recruiter", "Recruiter"), ("Job Seeker", "Job Seeker")],
#         required=True,
#         label="Role"
#     )
