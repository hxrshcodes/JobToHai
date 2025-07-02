from django.db import models
from datetime import datetime

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    designation = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Achievement(models.Model):
    personal_info = models.ForeignKey(PersonalInformation, related_name='achievements', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

class Experience(models.Model):
    personal_info = models.ForeignKey(PersonalInformation, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

class Education(models.Model):
    personal_info = models.ForeignKey(PersonalInformation, related_name='educations', on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    start_date = models.DateField()
    graduation_date = models.DateField()
    description = models.TextField()

class Project(models.Model):
    personal_info = models.ForeignKey(PersonalInformation, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()

class Skill(models.Model):
    personal_info = models.ForeignKey(PersonalInformation, related_name='skills', on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(default=datetime.today())
    is_updated = models.DateTimeField(default=datetime.today())

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
