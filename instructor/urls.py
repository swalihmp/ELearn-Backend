from django.urls import path
from . import views
from .views import Onboard,Instructors


urlpatterns = [
    path('onboard/', Onboard.as_view(), name='onboard'),
    path('instructors/',Instructors.as_view(),name='instructors')
]