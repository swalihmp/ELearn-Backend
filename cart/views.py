from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart,Coupon
from datetime import datetime


from .serializers import AddCartSerializer,GetCartSerializer,GetCouponView

# Create your views here.


class AddCart(APIView):
    def post(self, request, format=None):
        serializer = AddCartSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})
        

class CartView(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(user=pk)
        
        serializer = AddCartSerializer(cart, many=True)
        
        total =0
        for i in range(len(cart)):
            x = cart[i].course.saleprice
            total = total+x
        print(total)
        
        return Response(serializer.data)
    
class GetCartView(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(user=pk)
        
        total =0
        for i in range(len(cart)):
            x = cart[i].course.saleprice
            total = total+x
        print(total) 
        
        serializer = GetCartSerializer(cart, many=True)
        
        return Response({'data':serializer.data, 'total':total})


class GetCoupon(APIView):
    def get(self,request):
        coupons = Coupon.objects.all()
        serializer = GetCouponView(coupons, many=True) 
        return Response(serializer.data)
  
class RemoveCart(APIView):
    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(id=pk)
            cart.delete()
            return Response({'msg': 200})
        except:
            cart.DoesNotExist
            return Response({'msg': 500})
        
        
class ApplyCoupon(APIView):
    def post(self, request, format=None):
        coupon = request.data.get('coupon')
        total = request.data.get('total')
        
        try:
            coupon = Coupon.objects.get(name=coupon)
    
        except Coupon.DoesNotExist:
            return Response({'msg': 600})
        else : 
            date = datetime.now().date()
            sdate = coupon.activ_date
            edate = coupon.exp_date
            minimum = coupon.min_amount
            users = coupon.allowed_users
            if ( int(minimum)<int(total) and sdate <= date <= edate and users>0):
                
                amount = coupon.discount
                coupon_id = coupon.name
                g_total = int(total)-int(amount)
                
                data ={
                    'discount':amount,
                    'g_total': g_total,
                    'coupon_name': coupon_id,
                    'status' : 'success'
                }
                return JsonResponse(data)
            else:
                return Response({'msg': 500})
        
        
        
   
        # print(coupon,total)
        # return Response({'msg': 200})
        
        
        
class CreateCoupon(APIView):
    def post(self, request, format=None):
        serializer = GetCouponView(data=request.data)
        print(request.data)
        is_valid = serializer.is_valid()
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})
        
        
class DeleteCoupon(APIView):
    def get(self, request, pk):
        coupon = Coupon.objects.get(id=pk)
        coupon.delete()
        return Response({'msg': 200})