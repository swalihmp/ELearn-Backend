from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('courses/',include('course.urls')),
    path('instruct/',include('instructor.urls')),
    path('csession/',include('csession.urls')),
    path('cart/',include('cart.urls')),
    path('payment/',include('payment.urls')),
    path('learning/',include('learning.urls')),
    path('chat/',include('chat.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
