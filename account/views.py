from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import UserSerializer,CourseSerializer,AddCategorySerializer,InstructorCourseSerializer,UserSerializer1
from account.models import User
from course.models import Course,Category,SubCat
from course.serializers import CategorySerializer,SubcategorySerializer


from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh'
    ]
    return Response(routes)



class UserRegistration(APIView):
     def post(self, request, format=None):
        email = request.data.get('email')
        print(request.data)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            mail_subject = 'Please activate your account'
            
            message = render_to_string('account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'usename': urlsafe_base64_encode(force_bytes(user.username))
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            return Response({'msg':'Registration Success'})
        
        return Response({'msg':'Registration Failed'})
    
    
@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        # userdata = request.session.get('userdata')
        # print('userd',userdata)
        # url = reverse('http://localhost:3000/login')

        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):

        user.is_active = True
        user.save()
        print('saved')

        return HttpResponseRedirect('http://localhost:3000/login')
        # return Response({"msg": "activated"})
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        token['is_admin'] = user.is_superadmin
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    

class ForgotPassword(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')

        if User.objects.filter(email=email).exists:
            user = User.objects.get(email__exact=email)

            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            return Response({'msg':'Please Reset Password In The Link', 'user_id':user.id})
        
        return Response({'msg': 'No Account Registered With This Email'})
    
    
@api_view(['GET'])    
def reset_validate(request, uidb64, token):
    
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid

        sessionid = request.session.get('uid')
        print(sessionid)

        return HttpResponseRedirect('http://localhost:3000/reset-password/')
    
    return Response({'msg': 'Link Expired or Invalid Token'})


class GetProfile(APIView):
    def get(self, request, pk):
        user = User.objects.filter(id=pk)
        print(user)
        
        serializer = UserSerializer1(user,many=True)
        
        return Response(serializer.data)


class ResetPassword(APIView):
    def post(self, request, format=None):
        
        str_user_id = request.data.get('user_id')
        user_id = int(str_user_id)
        password = request.data.get('password')
        
        print(user_id)
        if user_id :
            
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            print('saved')

            return Response({'msg': 'Password Updated Successfully'})
    
        return HttpResponseRedirect('http://localhost:3000/reset-password')
    
    
class ChangeImage(APIView):
    def post(self,request, format=None):
        print(request.data)
        current_user = request.data.get('user')
        user = User.objects.get(id=current_user)
        image = request.data.get('image')
        
        user.image = image
        user.save()
        
        return Response({'msg':200})
    
    
class UpdateProfile(APIView):
    def post(self, request, format=None):
        user_id = request.data['user_id']
        current_user = User.objects.get(id=user_id)
        current_user.first_name = request.data['first_name']
        current_user.last_name = request.data['last_name']
        current_user.discription = request.data['discription']
        current_user.save()
        return Response({'msg':200})
    

class ChangePass(APIView):
    def post(self, request, format=None):
        oldpassword = request.data['oldpass']
        password = request.data['password']
        user_id = request.data['user_id']
        
        user = User.objects.get(id=user_id)

        success = user.check_password(oldpassword)
        if success:
            user.set_password(password)
            user.save()
            print("updated")
            data = {
                'msg': 200
            }
            return Response(data)
        else:
            print("Not done")
            data = {
                'msg': 500
            }
            return Response(data)

        
        
        
        
        
class Listuser(ListCreateAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = UserSerializer
    
    
class Blockuser(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        print(user.is_active)
        user.is_active = not user.is_active
        user.save()
        return Response({'msg': 200})
    
class Singlecourse(APIView):
    def get(self, request, pk):
        query = Course.objects.get(id=pk)
        serializer = CourseSerializer(query)
        return Response(serializer.data) 
    
class Singleuser(APIView):
    def get(self, request, pk):
        query = Course.objects.get(id=pk)
        user = query.user
        query1 = User.objects.get(username=user)
        serializer = UserSerializer(query1)
        return Response(serializer.data) 
    

class CreateCategory(APIView):
    def post(self, request, format=None):
        serializer = AddCategorySerializer(data=request.data)
        print(request.data)
        is_valid = serializer.is_valid()
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            cat = Category.objects.last()
            cat.is_active = True
            cat.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})
  
  
        
class Singlecat(APIView):
    def get(self, request, id):
        
        query = Category.objects.get(id=id)
        serializer = AddCategorySerializer(query)
        return Response(serializer.data) 
    
    def put(self, request, id):
        try:
            queryset = Category.objects.get(id=id)
        except:
            Category.DoesNotExist
            return Response({'msg': 404})
        if queryset:
            if request.data.get('image')== 'null':
                name = request.data.get('name')
                description = request.data.get('description')
                
                queryset.name = name
                queryset.description = description 
                queryset.save()
                
                return Response({'msg': 200})
            else:
                name = request.data.get('name')
                description = request.data.get('description')
                image = request.data.get('image')
                
                queryset.name = name
                queryset.description = description 
                queryset.image = image
                queryset.save()
                
                return Response({'msg': 200})
        else:
            return Response({'msg': 500})


class BlockCat(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        
        category.is_active = not category.is_active
        category.save()
        return Response({'msg': 200})
    

class BlockSubcat(APIView):
    def get(self, request, pk):
        subcategory = SubCat.objects.get(id=pk)
        
        subcategory.is_active = not subcategory.is_active
        subcategory.save()
        return Response({'msg': 200})
    
class AllCategory(ListCreateAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    
    
    
class InstructorCourse(APIView):
    def get(self, request, pk):
        courses = Course.objects.filter(user=pk)
        serializer = InstructorCourseSerializer(courses, many=True)
        return Response(serializer.data) 
    
    
class PendingCourse(APIView):
    def get(self, request, pk):
        courses = Course.objects.filter(user=pk,is_active=False)
        serializer = InstructorCourseSerializer(courses, many=True)
        return Response(serializer.data) 


class ApprovedCourse(APIView):
    def get(self, request, pk):
        courses = Course.objects.filter(user=pk,is_active=True)
        serializer = InstructorCourseSerializer(courses, many=True)
        return Response(serializer.data) 
    
    