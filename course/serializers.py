from rest_framework import serializers
from course.models import Course,Category,SubCat


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['user','title','subtitle','description','category','sub_category','image','video','is_active','welcomemsg','endmsg','price','saleprice']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description','image']