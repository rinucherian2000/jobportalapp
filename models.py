from django.db import models
from django.contrib.auth.models import User
from users.models import User

# Create your models here.



class Candidate(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    candidate_name = models.CharField(max_length=100)
    cv = models.ImageField(upload_to="images")
    qualification = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    experience = models.CharField( max_length=200)