from django.urls import path
from . import views
from .views import Onboard


urlpatterns = [
    path('onboard/', Onboard.as_view(), name='onboard'),
]