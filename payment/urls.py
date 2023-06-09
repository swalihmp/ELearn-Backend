from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import start_payment,handle_payment_success

urlpatterns = [
    path('pay/', start_payment.as_view(), name='pay'),
    path('success/', handle_payment_success.as_view(), name='success')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)