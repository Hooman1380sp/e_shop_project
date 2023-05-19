from django.http import HttpRequest
from django.shortcuts import render
from product_module.models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .serializers import AddProductToCartSerializer
from .models import Cart,CartDetail
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


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
