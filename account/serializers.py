from rest_framework import serializers
from account.models import User
from course.models import Course,Category,SubCat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
    
class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','discription','id']
    
# class Allcategory(serializers.ModelSerializer):
#     class Meta:
#         model: Category
#         fields = '__all__'
  
  
class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SubCategory(serializers.ModelSerializer):
    class Meta:
        model = SubCat
        fields = "__all__"
        
              
        
class CourseSerializer(serializers.ModelSerializer):
    category = AddCategorySerializer()
    sub_category = SubCategory()
    user = UserSerializer1()
    
    class Meta:
        model = Course
        fields = '__all__'
        
        

        
        
class InstructorCourseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        
