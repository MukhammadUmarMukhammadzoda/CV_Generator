from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    summary = models.TextField()
    degree = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    previus_work = models.TextField()
    skills = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name