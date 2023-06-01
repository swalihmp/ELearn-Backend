from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import SessionView,LectureView


urlpatterns = [
    path('session/<int:pk>', SessionView.as_view(), name='session'),
    path('lectures/<int:pk>',LectureView.as_view(), name='lectures'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)