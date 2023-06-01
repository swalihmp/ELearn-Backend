from django.db import models
from account.models import User

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
    is_active = models.BooleanField(default=False)


class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=500,null=False)
    subtitle = models.CharField(max_length=600,null=False)
    description = models.CharField(max_length=600,null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCat,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/course')
    video = models.FileField(upload_to='photos/course')
    is_active = models.BooleanField(default=True)
    welcomemsg = models.CharField(max_length=500,null=False)
    endmsg = models.CharField(max_length=500,null=False)
    price = models.IntegerField()
    saleprice = models.IntegerField()
    
    
    

