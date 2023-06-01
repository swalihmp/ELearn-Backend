from django.urls import path
from . import views
from .views import AddCart,CartView,GetCartView


urlpatterns = [
    path('addcart/', AddCart.as_view(), name='addcart'),
    path('carts/<int:pk>',CartView.as_view(), name='carts'),
    path('getcarts/<int:pk>',GetCartView.as_view(), name='getcarts'),
]