from django.db import models
from course.models import Course
from account.models import User

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    price = models.CharField(max_length=30,blank=True) 