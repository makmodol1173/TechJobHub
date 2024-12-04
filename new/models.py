# # from django.db import models

# # Create your models here.
# from django.db import models

# class Job(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     company = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     posted_date = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
class Recruiter(models.Model):
    r_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensures unique emails
    password = models.CharField(max_length=128)  # Accommodates hashed passwords
    address = models.TextField()  # TextField for more flexible address storage

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"


class Company(models.Model):
    c_id = models.AutoField(primary_key=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name="companies")  # ForeignKey to Recruiter
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    trade_license_number = models.CharField(max_length=100, unique=True)  # Unique trade license

    def __str__(self):
        return self.name


class JobPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name="job_posts")
    title = models.CharField(max_length=100)
    education_requirement = models.CharField(max_length=100)
    deadline = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)  # E.g., Full-time, Part-time
    years_experience = models.PositiveIntegerField()
    key_responsibilities = models.TextField()

    def __str__(self):
        return self.title


class JobSeeker(models.Model):
    js_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    address = models.TextField()
    education = models.TextField()
    resume = models.FileField(upload_to='resumes/')  # Supports file upload

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"


class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


class Application(models.Model):
    app_id = models.AutoField(primary_key=True)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="applications")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="applications")
    created_at = models.DateTimeField(auto_now_add=True)
    questions_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Application {self.app_id} for {self.job_post}"


class Bookmark(models.Model):
    bm_id = models.AutoField(primary_key=True)
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="bookmarks")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="bookmarks")

    def __str__(self):
        return f"Bookmark {self.bm_id} for {self.job_post}"


class Question(models.Model):
    ques_id = models.AutoField(primary_key=True)
    app = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="questions")
    question1 = models.TextField(blank=True, null=True)
    question2 = models.TextField(blank=True, null=True)
    question3 = models.TextField(blank=True, null=True)
    question4 = models.TextField(blank=True, null=True)
    question5 = models.TextField(blank=True, null=True)
    question6 = models.TextField(blank=True, null=True)
    question7 = models.TextField(blank=True, null=True)
    question8 = models.TextField(blank=True, null=True)
    question9 = models.TextField(blank=True, null=True)
    question10 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Questions for Application {self.application.name}"


class Answer(models.Model):
    ans_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField()

    def __str__(self):
        return f"Answer {self.ans_id}"


class Assessment(models.Model):
    asses_id = models.AutoField(primary_key=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="assessments")
    marks = models.JSONField()  # Store marks as a JSON object for flexibility

    def __str__(self):
        return f"Assessment {self.asses_id}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(
        max_length=20,
        choices=[('recruiter', 'Recruiter'), ('job_seeker', 'Job Seeker')],
        default='job_seeker'
    )
    location = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_picture/", default="default.png")
    recruiter_info = models.OneToOneField(Recruiter, on_delete=models.CASCADE, null=True, blank=True)
    job_seeker_info = models.OneToOneField(JobSeeker, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"