from rest_framework import serializers
from .models import Sessions,Lecture
from course.models import SubCat,Course
from course.serializers import CategorySerializer

        
        
class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
        
class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = '__all__'
        
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta: 
        model= SubCat
        fields = '__all__'
        
class CreateCourseSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Course
        fields = '__all__'