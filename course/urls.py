from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import Course,Category
from account.views import Singlecourse,Singleuser,CreateCategory,Singlecat,BlockCat,AllCategory,InstructorCourse,BlockSubcat,PendingCourse,ApprovedCourse
from csession.views import SubCategory,CreareCourse,AllCourse,BlockCourse,AllSubCategory,CreateSubCategory,RejectCourse,SearchCourse,Courses,UpdateCourse


urlpatterns = [
    path('course/', Courses.as_view(), name='course'),
    path('search/<str:data>',SearchCourse.as_view(),name='search'),
    path('allcourse/', AllCourse.as_view(), name='allcourse'),
    path('instructorcourse/<int:pk>',InstructorCourse.as_view(),name='instructorcourse'),
    path('category/',Category.as_view(), name='category'),
    path('allcategory/',AllCategory.as_view(), name='allcategory'),
    path('allsubcategory/',AllSubCategory.as_view(), name='allsubcategory'),
    path('subcategory/<int:pk>',SubCategory.as_view(),name='subcategory'),
    path('singlecourse/<int:pk>',Singlecourse.as_view(),name='singlecourse'),
    path('singleuser/<int:pk>',Singleuser.as_view(),name='singleuser'),
    path('createcourse/',CreareCourse.as_view(),name='createcourse'),
    path('addcategory/', CreateCategory.as_view(), name='addcategory'),
    path('addsubcategory/', CreateSubCategory.as_view(), name='addsubcategory'),
    path('singlecat/<int:id>', Singlecat.as_view(), name='singlecat'),
    path('blockcategory/<int:pk>',BlockCat.as_view(),name='blockcategory'),
    path('blocksubcategory/<int:pk>',BlockSubcat.as_view(),name='blocksubcategory'),
    path('blockcourse/<int:pk>',BlockCourse.as_view(),name='blockcourse'),
    path('rejectcourse/<str:msg>/<int:id>',RejectCourse.as_view(), name='rejectcourse'),
    path('pendingcourse/<int:pk>',PendingCourse.as_view(),name='pendingcourse'),
    path('aprovedcourse/<int:pk>',ApprovedCourse.as_view(),name='aprovedcourse'),
    path('updatecourse/<int:pk>',UpdateCourse.as_view(),name='UpdateCourse'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
