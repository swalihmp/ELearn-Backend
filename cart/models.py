from django.db import models
from course.models import Course
from account.models import User

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    price = models.CharField(max_length=30,blank=True) 
    
    
class Coupon(models.Model):
    name = models.CharField(max_length=200,null=False)
    min_amount = models.IntegerField(null=True)
    activ_date = models.DateField(null=True)
    exp_date = models.DateField(null=True)
    allowed_users = models.IntegerField()
    discount = models.IntegerField(default=0)
    
    

