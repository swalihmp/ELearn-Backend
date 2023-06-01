from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sessions,Lecture
from .serializers import SessionsSerializer,LectureSerializer,SubCategorySerializer,CreateCourseSerializer
from course.models import Category,SubCat

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
    
class SubCategory(APIView):
    def get(self, request, pk):
        subcat = SubCat.objects.filter(category=pk)
        serializer = SubCategorySerializer(subcat, many=True)
        
        return Response(serializer.data)
    

class CreareCourse(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = CreateCourseSerializer(data=request.data)
        
        is_valid = serializer.is_valid()
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})