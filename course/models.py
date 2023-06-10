from django.db import models
from account.models import User
from payment.models import Order

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=700)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='photos/categ')
    is_active = models.BooleanField(default=False)
    
class SubCat(models.Model):
    name = models.CharField(max_length=700)
    description = models.CharField(max_length=700)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=500,null=False)
    subtitle = models.CharField(max_length=600,null=False)
    description = models.CharField(max_length=600,null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCat,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/course')
    video = models.FileField(upload_to='photos/course')
    is_active = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reason = models.CharField(max_length=600,null=True,default='')
    welcomemsg = models.CharField(max_length=500,null=False)
    endmsg = models.CharField(max_length=500,null=False)
    price = models.IntegerField()
    saleprice = models.IntegerField()
    

class EnrolledCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)   
    progress = models.CharField(max_length=500,default=0)
    

