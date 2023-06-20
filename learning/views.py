from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from course.models import EnrolledCourse
from csession.models import Lecture
from .models import Progress
from .serializers import ProgressSerializer,ReviewSerializer
from course.models import Course

class ProgressView(APIView):
    def get(self, request, pk):
        course = EnrolledCourse.objects.get(course=pk)
        lectures = Progress.objects.filter(current_course=course)
        
        serializer = ProgressSerializer(lectures, many=True)
        return Response(serializer.data)
    
class AddReview(APIView):
    def post(self, request, format=None):
        print(request.data)
        print(request.data.get('course'))
        
        review = ReviewSerializer(data=request.data)
        is_valid = review.is_valid()
        print(review.errors)

        if review.is_valid():
            review.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})