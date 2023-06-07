from rest_framework import serializers
from .models import Instructor
from account.serializers import UserSerializer



class OnboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'
        
        
class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Instructor
        fields = '__all__'