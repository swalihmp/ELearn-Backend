from django.db import models
from account.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/categ')
    is_active = models.BooleanField(default=False)
    
class SubCat(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)



class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False)
    subtitle = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=100,null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCat,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/course')
    video = models.FileField(upload_to='photos/course')
    is_active = models.BooleanField(default=True)
    welcomemsg = models.CharField(max_length=50,null=False)
    endmsg = models.CharField(max_length=50,null=False)
    price = models.IntegerField()
    saleprice = models.IntegerField()
    
class Session(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
class Lecture(models.Model):
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    
    

