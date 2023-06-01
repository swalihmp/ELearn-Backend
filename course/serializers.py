from rest_framework import serializers
from course.models import Course,Category,SubCat
from account.serializers import UserSerializer




class CourseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'