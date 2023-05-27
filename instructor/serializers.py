from rest_framework import serializers
from .models import Instructor



class OnboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'