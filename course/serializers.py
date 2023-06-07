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
        
        
class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = SubCat
        fields = '__all__'
        
        
        
class CreateSubcategory(serializers.ModelSerializer):
    class Meta:
        model = SubCat
        fields = '__all__'