from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ProgressView,AddReview


urlpatterns = [
    path('progress/<int:pk>',ProgressView.as_view(), name='progress'),
    path('addreview/',AddReview.as_view(),name='addreview')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)