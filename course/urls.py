from django.urls import path
from . import views
from .views import Course,Category


urlpatterns = [
    path('course/', Course.as_view(), name='course'),
    path('category/',Category.as_view(), name='category'),
]
