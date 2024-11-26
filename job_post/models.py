
# job_post/models.py
from django.db import models

class JobPost(models.Model):
    job_title = models.CharField(max_length=255)
    about= models.TextField()
    location = models.CharField(max_length=255)
    responsibilities = models.TextField()
    education= models.TextField(blank=True, null=True)
    qualifications= models.TextField()
    deadline = models.DateField()
    job_type = models.CharField(
        max_length=50,
        choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title
