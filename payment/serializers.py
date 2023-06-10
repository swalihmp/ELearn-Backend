from rest_framework import serializers

from .models import Order
from course.models import EnrolledCourse

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        depth = 2
        
        
class EnrolledCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnrolledCourse
        fields = '__all__'