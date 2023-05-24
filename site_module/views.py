from django.shortcuts import render
from .models import SiteBanner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SiteBannerSerializer

# Create your views here.

class SiteBannerProductListView(APIView):
    serializer_class = SiteBannerSerializer
    throttle_scope = 'get_request'
    """
    page List Product
    """

    def setup(self, request, *args, **kwargs):
        self.query = SiteBanner.objects.filter(is_active=True, position__iexact= SiteBanner.SiteBannerPosition.product_list).first()
        super().setup(request, *args, **kwargs)

    def get(self,request):
        ser_data = SiteBannerSerializer(instance=self.query)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)


class SiteBannerProductDetailView(APIView):
    serializer_class = SiteBannerSerializer
    throttle_scope = 'get_request'
    """
    page Detail Product
    """

    def setup(self, request, *args, **kwargs):
        self.query = SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerPosition.product_detail).first()
        super().setup(request, *args, **kwargs)

    def get(self, request):
        ser_data = SiteBannerSerializer(instance=self.query)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class SiteBannerCategoryListView(APIView):
    serializer_class = SiteBannerSerializer
    throttle_scope = 'get_request'
    """
    page List Category
    """

    def setup(self, request, *args, **kwargs):
        self.query = SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerPosition.category_list).first()
        super().setup(request, *args, **kwargs)

    def get(self, request):
        ser_data = SiteBannerSerializer(instance=self.query)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class SiteBannerCategoryDetailView(APIView):
    serializer_class = SiteBannerSerializer
    throttle_scope = 'get_request'
    """
    page Detail Category
    """

    def setup(self, request, *args, **kwargs):
        self.query = SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerPosition.category_detail).first()
        super().setup(request, *args, **kwargs)

    def get(self, request):
        ser_data = SiteBannerSerializer(instance=self.query)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class SiteBannerAboutUsView(APIView):
    serializer_class = SiteBannerSerializer
    throttle_scope = 'get_request'
    """
    page About Us
    """

    def setup(self, request, *args, **kwargs):
        self.query = SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerPosition.about_us).first()
        super().setup(request, *args, **kwargs)

    def get(self, request):
        ser_data = SiteBannerSerializer(instance=self.query)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class SiteBannerIndexPageView(APIView):
    serializer_class = SiteBannerSerializer
    throttle_scope = 'get_request'
    """
    page Index
    """

    def setup(self, request, *args, **kwargs):
        self.query = SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerPosition.index_page).first()
        super().setup(request, *args, **kwargs)

    def get(self, request):
        ser_data = SiteBannerSerializer(instance=self.query)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)
