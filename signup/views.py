from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm

def signaction(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Process form data
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Save user
            user = User.objects.create_user(
                username=email, email=email, first_name=first_name, last_name=last_name, password=password
            )
            user.save()
            return redirect('Login')
    else:
        form = UserRegistrationForm()
    return render(request, 'Signup.html', {'form': form})
