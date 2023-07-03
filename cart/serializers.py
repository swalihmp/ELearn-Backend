from rest_framework import serializers
from .models import Cart,Coupon
from course.serializers import CourseSerializer



class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        

class GetCartSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Cart
        fields = '__all__'
        
class GetCouponView(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
        
# class AddCouponSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Coupon
#         fields = '__all__'