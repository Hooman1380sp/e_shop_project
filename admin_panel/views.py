from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .permissions import *
from django.contrib.auth import get_user_model
User = get_user_model()
from product_module.models import Product,ProductCategory,ProductVisit
from contact_module.models import ContactUs,AboutUs
from site_module.models import SiteBanner
from cart_module.models import Cart,CartDetail



# Create your views here.


class UserViewSet(ViewSet):
    queryset = User.objects.all()
    permission_classes = [UserPermission,]
    def list(self, request):
        self.check_object_permissions(request, self.queryset)
        ser_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(request, self.queryset)
        ser_data = UserSerializer(instance=user)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def create(self,request):
        self.check_object_permissions(request, self.queryset)
        ser_data = UserSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self,request,pk=None):
        self.check_object_permissions(request, self.queryset)
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user,data=request.POST,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(data=ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        self.check_object_permissions(request, self.queryset)
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        user.save()
        return Response(data={'message': 'user deactivated'},status=status.HTTP_204_NO_CONTENT)
