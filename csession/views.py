from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Sessions,Lecture
from account.models import User
from course.models import Course
from .serializers import SessionsSerializer,LectureSerializer,SubCategorySerializer,CreateCourseSerializer,CourseSerializer
from course.serializers import CreateSubcategory
from course.models import Category,SubCat




from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
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
            
            user = request.data['user']
            current_user = User.objects.get(id=user)
            email = 'swalihmp438368@gmail.com'
            
            current_site = get_current_site(request)
            
            mail_subject = 'New Course Created'
            
            message = render_to_string('admin_alert_email.html', {
                'user': current_user,
                'domain': current_site,
                'usename': urlsafe_base64_encode(force_bytes(current_user.username)),
                'title' : request.data['title']
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
      
            
            
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})
        

class UpdateCourse(ListCreateAPIView):
    def post(self, request, pk):
        print(pk)
        print(request.data)
        try:
            queryset = Course.objects.get(id=pk)
        except:
            Course.DoesNotExist
            return Response({'msg': 404})
        if queryset:
            print(queryset)
            
            cat = request.data.get('category')
            sub = request.data.get('sub_category')
            category = Category.objects.get(id=cat)
            sub_category = SubCat.objects.get(id=sub)
                        
            title = request.data.get('title')
            subtitle = request.data.get('subtitle')
            description = request.data.get('discription')
            category = category
            sub_category = sub_category
            image = request.data.get('image')
            video = request.data.get('video')
            welcomemsg = request.data.get('welcomemsg')
            endmsg = request.data.get('endmsg')
            price = request.data.get('saleprice')
            saleprice = request.data.get('price')
            
            queryset.title = title
            queryset.subtitle = subtitle
            queryset.description = description
            queryset.category = category
            queryset.sub_category = sub_category
            queryset.image = image
            queryset.video = video
            queryset.welcomemsg= welcomemsg
            queryset.endmsg = endmsg
            queryset.price = price
            queryset.saleprice = saleprice
            
            queryset.save()
            
            return Response({'msg': 200})
        else:
            return Response({'msg': 500})
        
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
    
    
class RejectCourse(APIView):
    def get(self, request, msg,id):
        print(msg,id)
        
        
        course = Course.objects.get(id=id)
        
        email = course.user.email
        
        current_site = get_current_site(request)
        
        mail_subject = 'Course Rejected....'
        
        message = render_to_string('user_alert_email.html', {
            'course': course,
            'course_name' : course.title,
            'msg':msg,
            'domain': current_site,
            'usename': urlsafe_base64_encode(force_bytes(course.user.username)),
        })
        to_email = email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        
        course.is_rejected = True
        course.reason = msg
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
        
        
class SearchCourse(APIView):
    
    def get(self, request, data):
        courses = Course.objects.filter(title__icontains=data,is_active=True)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data) 
    
    
class Courses(APIView):
    def get(self,request):
        courses = Course.objects.filter(is_active=True)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
        