from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import Course,Category
from account.views import Singlecourse,Singleuser,CreateCategory,Singlecat,BlockCat,AllCategory,InstructorCourse
from csession.views import SubCategory,CreareCourse


urlpatterns = [
    path('course/', Course.as_view(), name='course'),
    path('instructorcourse/<int:pk>',InstructorCourse.as_view(),name='instructorcourse'),
    path('category/',Category.as_view(), name='category'),
    path('allcategory/',AllCategory.as_view(), name='allcategory'),
    path('subcategory/<int:pk>',SubCategory.as_view(),name='subcategory'),
    path('singlecourse/<int:pk>',Singlecourse.as_view(),name='singlecourse'),
    path('singleuser/<int:pk>',Singleuser.as_view(),name='singleuser'),
    path('createcourse/',CreareCourse.as_view(),name='createcourse'),
    path('addcategory/', CreateCategory.as_view(), name='addcategory'),
    path('singlecat/<int:id>', Singlecat.as_view(), name='singlecat'),
    path('blockcategory/<int:pk>',BlockCat.as_view(),name='blockcategory'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
