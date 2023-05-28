from django.urls import path
from account.views import UserRegistration
from . import views
from .views import MyTokenObtainPairView,ForgotPassword,ResetPassword,Listuser,Blockuser

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('', views.getRoutes),
    path('register/', UserRegistration.as_view()),
    path('activate/<uidb64>/<token> ', views.activate, name='activate'),
    path('users/', Listuser.as_view(),name='users'),
    path('blockuser/<int:pk>',Blockuser.as_view(),name='blockuser'),
    
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('forgotpassword/', ForgotPassword.as_view()),
    path('reset_validate/<uidb64>/<token> ', views.reset_validate, name='reset_validate'),
    path('resetpassword/', ResetPassword.as_view()),
]