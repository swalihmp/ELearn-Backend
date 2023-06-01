from rest_framework import serializers
from account.models import User
from course.models import Course,Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
        
class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class InstructorCourseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        
