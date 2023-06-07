from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Sessions,Lecture
from course.models import Course
from .serializers import SessionsSerializer,LectureSerializer,SubCategorySerializer,CreateCourseSerializer,CourseSerializer
from course.serializers import CreateSubcategory
from course.models import Category,SubCat

# Create your views here.


class SessionView(APIView):
    def get(self, request, pk):
        print(pk)
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
    
class AllCourse(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
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
        
class AddSession(APIView):
    def post(self, request, format=None):
        session = SessionsSerializer(data=request.data)
        
        is_valid = session.is_valid()
        print(session.errors)
        if session.is_valid():
            session.save()
            return Response({'msg': 200})
        else:
            return Response({'msg': 404})
        
class AddMaterial(APIView):
    def post(self, request, format=None):
        material = LectureSerializer(data=request.data)
        
        is_valid = material.is_valid()
        print(material.errors)
        if material.is_valid():
            material.save()
            return Response({'msg': 200})
        else:
            return Response({'msg': 404})
        
        


class BlockCourse(APIView):
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        
        course.is_active = not course.is_active
        course.save()
        return Response({'msg': 200})
    

class AllSubCategory(ListCreateAPIView):
    queryset = SubCat.objects.filter()
    serializer_class = SubCategorySerializer
    

class CreateSubCategory(APIView):
    def post(self, request, format=None):
        subcategory = CreateSubcategory(data=request.data)
        print(request.data)
        is_valid = subcategory.is_valid()
        print(subcategory.errors)

        if subcategory.is_valid():
            subcategory.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})