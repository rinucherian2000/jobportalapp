from django.db import models
from users.models import User


# Create your models here.


class CompanyProfile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    company_name=models.CharField(max_length=120)
    services=models.CharField(max_length=200)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class Jobs(models.Model):
    company=models.ForeignKey(CompanyProfile,on_delete=models.CASCADE,null=True)
    post=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    skills=models.CharField(max_length=120)
    description=models.CharField(max_length=150)
    posted_date=models.DateField(auto_now_add=True, null=True)
    last_date=models.DateField()