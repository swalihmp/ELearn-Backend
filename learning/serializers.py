from rest_framework import serializers\
    
from learning.models import Progress,Review
from csession.serializers import LectureSerializer


class ProgressSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer()
    
    class Meta:
        model = Progress
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'