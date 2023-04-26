from django.shortcuts import render,get_object_or_404
from .serializers import ProductSerializer,ProductCategorySerializer
from rest_framework.views import APIView
from .models import Product,ProductCategory
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.




class ProductListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = ProductSerializer
    """
    for see list product.s
    """
    def get(self,request):
        queryset = Product.objects.filter(is_delete=False,is_active=True)
        ser_data = ProductSerializer(instance=queryset,many=True)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)

class ProductDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = ProductSerializer
    """
    for see one product by slug
    """
    def get(self,request,slug):
        queryset = Product.objects.filter(is_delete=False, is_active=True,slug=slug)
        object_var = get_object_or_404(queryset,slug=slug)
        ser_data = ProductSerializer(instance=object_var)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)


class ProductCategoryListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = ProductCategorySerializer
    """
    for see list product category
    """
    def get(self,request):
        queryset = ProductCategory.objects.filter(is_delete=False, is_active=True)
        ser_data = ProductCategorySerializer(instance=queryset,many=True)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)


class ProductCategoryDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = ProductCategorySerializer
    """
    for see one product_category.s
    """
    def get(self,request,slug):
        queryset = ProductCategory.objects.filter(is_delete=False, is_active=True,slug=slug)
        object_var = get_object_or_404(queryset,slug=slug)
        ser_data = ProductCategorySerializer(instance=object_var)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)