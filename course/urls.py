from django.urls import path
from . import views
from .views import Course,Category
from account.views import Singlecourse,Singleuser


urlpatterns = [
    path('course/', Course.as_view(), name='course'),
    path('category/',Category.as_view(), name='category'),
    path('singlecourse/<int:pk>',Singlecourse.as_view(),name='singlecourse'),
    path('singleuser/<int:pk>',Singleuser.as_view(),name='singleuser'),
]
