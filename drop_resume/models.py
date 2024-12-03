# from django.db import models

# class JobSeeker(models.Model):
#     js_id = models.AutoField(primary_key=True)
#     email = models.EmailField(unique=True)
#     fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     password = models.CharField(max_length=128)
#     address = models.TextField()
#     education = models.TextField()
#     resume = models.FileField(upload_to='resumes/')  # File storage location

#     def __str__(self):
#         return f"{self.fname} {self.lname} ({self.email})"
