from django.contrib import messages

from django.shortcuts import render
from django.contrib import messages
from .forms import JobPostForm
from .models import JobPost

def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job post created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to create job post. Check your inputs.")
    else:
        form = JobPostForm()
    return render(request, 'job_post/create_post.html', {'form': form})

def dashboard(request):
    job_posts = JobPost.objects.all().order_by('-created_at')  # Fetch all job posts
    return render(request, 'job_post/dashboard.html', {'job_posts': job_posts})