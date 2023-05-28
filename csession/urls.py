from django.urls import path
from . import views
from .views import SessionView,LectureView


urlpatterns = [
    path('session/<int:pk>', SessionView.as_view(), name='session'),
    path('lectures/<int:pk>',LectureView.as_view(), name='lectures'),
]