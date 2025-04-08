from django.db import models
from django.contrib.auth.models import User
from django.db import models


class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Contact(models.Model):
    cv = models.ForeignKey(CV, related_name='contacts', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # Ensure this line exists


class Education(models.Model):
    cv = models.ForeignKey(CV, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_started = models.PositiveIntegerField()
    year_completed = models.PositiveIntegerField()

class WorkExperience(models.Model):
    cv = models.ForeignKey(CV, related_name='work_experience', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    description = models.TextField()

class Skill(models.Model):
    cv = models.ForeignKey(CV, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
class Certificate(models.Model):
    cv = models.ForeignKey(CV, related_name='certificates', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

class Project(models.Model):
    cv = models.ForeignKey(CV, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

class SocialLink(models.Model):
    cv = models.ForeignKey(CV, related_name='social_links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    url = models.URLField()
