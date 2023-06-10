from django.contrib import admin
from .models import Course,Category,SubCat,EnrolledCourse

# Register your models here.


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(SubCat) 
admin.site.register(EnrolledCourse)