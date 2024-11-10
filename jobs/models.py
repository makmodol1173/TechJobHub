from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('MKT', 'Marketing'),
    ]

    WORK_MODALITY_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
    ]

    JOB_TYPE_CHOICES = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    educational_requirements = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    work_modality = models.CharField(max_length=20, choices=WORK_MODALITY_CHOICES, blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    role_overview = models.TextField(blank=True, null=True)
    key_responsibilities = models.TextField(blank=True, null=True)
    qualification_experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
