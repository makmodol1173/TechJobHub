from django.shortcuts import render, get_object_or_404
from .models import Job, Category

def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    categories = Category.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'categories': categories})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

from django.shortcuts import render, redirect
from .forms import JobForm

def create_job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()  # Save the job post to the database
            return redirect('job_list')  # Redirect to the job list or another page
    else:
        form = JobForm()
    return render(request, 'jobs/create_job_post.html', {'form': form})


from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()  # Retrieve all job posts
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
