from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart


from .serializers import AddCartSerializer,GetCartSerializer

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
        print(cart)
        serializer = AddCartSerializer(cart, many=True)
        
        return Response(serializer.data)
    
class GetCartView(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(user=pk)
        print(cart)
        serializer = GetCartSerializer(cart, many=True)
        
        return Response(serializer.data)