from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import User




from .serializers import OnboardSerializer

# Create your views here.


class Onboard(APIView):
    def post(self, request):
        data = request.data
        user = data['user']
        current_user = User.objects.get(id=user)
        
        serializer = OnboardSerializer(data=request.data)
        print(request.data)
        serializer.is_valid()
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            current_user.is_staff=True
            current_user.save()
            return Response({'msg': 200})
        else :
            print('False')
            return Response({'msg': 404})