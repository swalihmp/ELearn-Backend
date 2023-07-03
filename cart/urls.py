from django.urls import path
from . import views
from .views import AddCart,CartView,GetCartView,RemoveCart,ApplyCoupon,GetCoupon,CreateCoupon,DeleteCoupon


urlpatterns = [
    path('addcart/', AddCart.as_view(), name='addcart'),
    path('carts/<int:pk>',CartView.as_view(), name='carts'),
    path('getcarts/<int:pk>',GetCartView.as_view(), name='getcarts'),
    path('removecart/<int:pk>',RemoveCart.as_view(),name='removecart'),
    path('applycoupon/',ApplyCoupon.as_view(),name='applycoupon'),
    path('getcoupon/',GetCoupon.as_view(),name='getcoupon'),
    path('addcoupon/', CreateCoupon.as_view(), name='addcoupon'),
    path('deletecoupon/<int:pk>',DeleteCoupon.as_view(),name='deletecoupon'),
]