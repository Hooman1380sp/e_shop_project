from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema,extend_schema_view

from .utils import get_client_ip
from .serializers import ProductSerializer, ProductCategorySerializer
from .models import Product, ProductCategory, ProductVisit


@extend_schema_view(post=extend_schema(
    responses={
        200: 'ok',
        400: 'bad request',
        403: 'forbidden',
    },
    tags=['Product'],
    description='to display whole products'))
class ProductListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ProductSerializer
    throttle_scope = 'get_request'
    """
    for see list product.s
    """

    def setup(self, request, *args, **kwargs):
        self.queryset = Product.objects.filter(is_delete=False,is_active=True)
        super().setup(request, *args, **kwargs)
        # در زمانی که از این متد استفاده میکنیم (setup)حتما باید سوپر و تمام [request, *args, **kwargs]فراخانی کنیم!

    def get(self, request):
        ser_data = self.serializer_class(instance=self.queryset, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


# about product detail function
class ProductDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ProductSerializer
    throttle_scope = 'get_request'
    """
    for see one product by slug
    """

    def get(self, request, slug):
        queryset = Product.objects.filter(is_delete=False, is_active=True, slug=slug).first()
        loaded_product: queryset = queryset
        ser_data = self.serializer_class(instance=queryset)
        # get user ip and user id  for visit-product
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id).save()
            # new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            # new_visit.save()
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class MostVisitProductView(APIView):
    serializer_class = ProductSerializer
    throttle_scope = 'get_request'
    """
     most visit product api (12P) => 12 number product api
    """

    def get(self, request: HttpRequest):
        queryset = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        ser_data = self.serializer_class(instance=queryset, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class ProductCategoryListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ProductCategorySerializer
    throttle_scope = 'get_request'
    """
    for see list product category
    """

    def get(self, request):
        queryset = ProductCategory.objects.filter(is_delete=False, is_active=True)
        ser_data = self.serializer_class(instance=queryset, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class ProductCategoryDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ProductCategorySerializer
    throttle_scope = 'get_request'
    """
    for see one product_category.s
    """

    def get(self, request, slug):
        queryset = ProductCategory.objects.filter(is_delete=False, is_active=True, slug=slug)
        object_var = get_object_or_404(queryset, slug=slug)
        ser_data = self.serializer_class(instance=object_var)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)
