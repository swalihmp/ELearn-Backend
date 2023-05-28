from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sessions,Lecture
from .serializers import SessionsSerializer,LectureSerializer

# Create your views here.


class SessionView(APIView):
    def get(self, request, pk):
        queryset = Sessions.objects.filter(course=pk)
        serializer = SessionsSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
class LectureView(APIView):
    def get(self, request, pk):
        queryset = Lecture.objects.filter(course=pk)
        serializer = LectureSerializer(queryset, many=True)
        
        return Response(serializer.data)
