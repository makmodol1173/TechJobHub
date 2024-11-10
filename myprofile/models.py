from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    study_field = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')
    cover_photo = models.ImageField(upload_to='cover_photos/', default='default_cover.jpg')
    profile_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name="skills", on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

class Language(models.Model):
    profile = models.ForeignKey(Profile, related_name="languages", on_delete=models.CASCADE)
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name
