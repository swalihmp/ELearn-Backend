from rest_framework import serializers
from .models import Room, Message
from account.serializers import UserSerializer1

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer1()
    
    class Meta:
        model = Message
        fields = '__all__'