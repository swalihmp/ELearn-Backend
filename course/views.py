from django.http import JsonResponse
from .models import Course,Category

from rest_framework.generics import ListCreateAPIView



from .serializers import CourseSerializer,CategorySerializer

# Create your views here.

class Course(ListCreateAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    
class Category(ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    
    