from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import razorpay
from rest_framework.decorators import api_view
from account.models import User
from datetime import datetime
from cart.models import Cart
from course.models import EnrolledCourse

from .models import Order
from .serializers import OrderSerializer,EnrolledCourseSerializer
# Create your views here.

class start_payment(APIView):
    def post(self, request, format=None):
        # request.data is coming from frontend
        
        amount = request.data['amount']
        current_user = request.data['user']
        user = User.objects.get(id=current_user)
        PUBLIC_KEY = 'rzp_test_GrC2fomAR5BvCu'
        SECRET_KEY = 'K3oUpvscgHYIteoxLW3u0Quf'

        # setup razorpay client this is the client to whome user is paying money that's you
        client = razorpay.Client(auth=(PUBLIC_KEY,SECRET_KEY))


        payment = client.order.create({"amount": int(amount) * 100, 
                                    "currency": "INR", 
                                    "payment_capture": "1"})


        order = Order.objects.create(order_user=user, 
                                    order_amount=amount, 
                                    order_payment_id=payment['id'],
                                    order_date= datetime.now().date(),
                                    firtname = request.data['fname'],
                                    lastname = request.data['lname'],
                                    addrress1 = request.data['address1'],
                                    addrress2 = request.data['address2'],
                                    email = request.data['email'],
                                    phone = request.data['phone'],
                                    coupon = request.data['coupon'],
                                    discount = request.data['discount'],)

        serializer = OrderSerializer(order)

        """order response will be 
        {'id': 17, 
        'order_date': '23 January 2021 03:28 PM', 
        'order_product': '**product name from frontend**', 
        'order_amount': '**product amount from frontend**', 
        'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
        'isPaid': False}"""

        data = {
            "payment": payment,
            "order": serializer.data
        }
        return Response(data)



class handle_payment_success(APIView):
    def post(self, request, format=None):
        res = json.loads(request.data["response"])
        current_user = json.loads(request.data["user"])
        user = User.objects.get(id=current_user)



        ord_id = ""
        raz_pay_id = ""
        raz_signature = ""

        # res.keys() will give us list of keys in res
        for key in res.keys():
            if key == 'razorpay_order_id':
                ord_id = res[key]
            elif key == 'razorpay_payment_id':
                raz_pay_id = res[key]
            elif key == 'razorpay_signature':
                raz_signature = res[key]

        order = Order.objects.get(order_payment_id=ord_id)

        data = {
            'razorpay_order_id': ord_id,
            'razorpay_payment_id': raz_pay_id,
            'razorpay_signature': raz_signature
        }

        PUBLIC_KEY = 'rzp_test_GrC2fomAR5BvCu'
        SECRET_KEY = 'K3oUpvscgHYIteoxLW3u0Quf'
        
        client = razorpay.Client(auth=(PUBLIC_KEY, SECRET_KEY))

        # checking if the transaction is valid or not by passing above data dictionary in 
        # razorpay client if it is "valid" then check will return None
        check = client.utility.verify_payment_signature(data)

        # if check is not None:
        #     print("Redirect to error url or error page")
        #     return Response({'error': 'Something went wrong'})

        print(order)
        # if payment is successful that means check is None then we will turn isPaid=True
        order.isPaid = True
        order.save()
        
        cart_items = Cart.objects.filter(user=user)
        print(cart_items)
        for item in cart_items:
            course = EnrolledCourse.objects.create(
                user = user,
                course = item.course,
                order_id = order,
            )
            serializer = EnrolledCourseSerializer(course)
            
        # Cart.objects.filter(user=user).delete()

        res_data = {
            'message': 'payment successfully received!'
        }

        return Response(res_data)
        