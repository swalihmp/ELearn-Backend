from django.db import models
from account.models import User

# Create your models here.

class Instructor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    expmode = models.CharField(max_length=50,null=False)
    exptype = models.CharField(max_length=50,null=False)
    subject = models.CharField(max_length=50,null=False)
    qualification = models.CharField(max_length=50,null=False)
