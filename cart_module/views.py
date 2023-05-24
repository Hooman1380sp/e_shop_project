import time
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
import requests
import json
from product_module.models import Product
from .models import Cart, CartDetail
from .serializers import AddProductToCartSerializer,ReceiptOfMyShopSerializer


# Create your views here.


SANDBOX = ''
#? sandbox merchant
if SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

MERCHANT = ''
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
amount = 1000  # Rial / Required
description = "نهایی کردن خرید از سایت ما"  # Required
phone = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'


class AddProductToCartView(APIView):
    class_serializer = AddProductToCartSerializer
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    """
    Cart_shop request is post 
    
    information: id product send to me with post.request!, and user this api for get request
    """
    def post(self,request: HttpRequest):
        ser_data = AddProductToCartSerializer(data=request.POST)
        if request.user.is_authenticated:
            if ser_data.is_valid():
                count_of_product = ser_data.validated_data.get('count')
                if count_of_product < 1:
                    return Response(data={'message': 'در دادن نوع درخواست خود دقت کنید'},status=status.HTTP_409_CONFLICT)
                else:
                    product_id = ser_data.validated_data.get('product_id')
                    product = Product.objects.filter(is_delete=False,is_active=True,id=product_id).first()
                    print(product)
                    if product is not None:
                        current_cart, created = Cart.objects.get_or_create(is_paid=False,user_id=request.user.id)
                        current_cat_detail = current_cart.cartdetail_set.filter(product_id=product_id).first()
                        if current_cat_detail is not None:
                            current_cat_detail.count += int(count_of_product)
                            current_cat_detail.save()
                            return Response(data={'message': 'محصول به سبد خرید شما اضافه شد!'},status=status.HTTP_208_ALREADY_REPORTED)
                        else:
                            new_detail = CartDetail(cart_shop_id=current_cart.id,product_id=product_id,count=count_of_product)
                            new_detail.save()
                            return Response(data={'message': 'سبد خرید شما ایجاد شد'},status=status.HTTP_202_ACCEPTED)
                    return Response({'message': 'درخواست شما با موفقیت ثبت شده است'},status=status.HTTP_200_OK)
            return Response({'message': 'تداخل در نا کار آمدی درخواست'},status=status.HTTP_408_REQUEST_TIMEOUT)
        return Response({'message': 'برای ثبت سفارش نیاز به ثبت نام است'}, status=status.HTTP_401_UNAUTHORIZED)

class ReceiptOfMyShopView(APIView):

    def setup(self, request, *args, **kwargs):
        self.query = Cart.objects.filter(is_paid=True, user_id=request.user.id).all()
        super().setup(request, *args, **kwargs)

    def get(self,request: HttpRequest):
            # e = Cart.objects.filter(id=4, is_paid=True).first()
            # print(e)
            ser_data = ReceiptOfMyShopSerializer(instance=self.query,many=True)
            return Response(data=ser_data.data,status=status.HTTP_202_ACCEPTED)



@login_required
def send_request(request: HttpRequest):
    current_cart, created = Cart.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_cart.calculate_price_whole()
    if total_price == 0:
        return redirect('http://127.0.0.1:8000/')
    data = {
        "MerchantID": MERCHANT,
        "Amount": total_price * 10,
        "Description": description,
        # "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}

@login_required()
def verify(authority,request: HttpRequest):
    print(request.user)
    print(request.user.id)
    current_cart, created = Cart.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_cart.calculate_price_whole()
    data = {
        "MerchantID": MERCHANT,
        "Amount": total_price * 10,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            current_cart.is_paid = True
            current_cart.payment_date = time.time()
            current_cart.save()
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response