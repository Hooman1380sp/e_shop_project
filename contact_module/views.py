from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from contact_module.models import ContactUs,AboutUs
from .serializers import ContactUsSerializers,AboutUsSerializers
from account_module.models import User
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# Create your views here.


class ContactUsView(APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = ContactUsSerializers
    """
    this is view for send contactus (message)for admin application
    """
    def post(self, request: HttpRequest):
        ser_data = self.serializer_class(data=request.POST)
        ser_data.is_valid(raise_exception=True)
        ip_HTTP_X = request.META.get('HTTP_X_FORWARDED_FOR')
        print(ip_HTTP_X)
        if ip_HTTP_X is None:
            ip_HTTP_X = request.META.get('REMOTE_ADDR')
            print(ip_HTTP_X)
            user = User.objects.filter(id=request.user.id).first()
            # if user is not None:
            title = ser_data.validated_data.get('title')
            full_name = ser_data.validated_data.get('full_name')
            email = ser_data.validated_data.get('email')
            message = ser_data.validated_data.get('message')
            if user:
                print('user True')
                ContactUs(user=user, ip=ip_HTTP_X, title=title, full_name=full_name, email=email, message=message).save()
                return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
                # message_contact = ContactUs(ip=ip_HTTP_X,title=title,user=user,full_name=full_name,email=email,message=message)
                # message_contact.save()
            else:
                print('user False')
                ContactUs(ip=ip_HTTP_X, title=title, full_name=full_name, email=email, message=message).save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)


class AboutUsView(APIView):
    serializer_class = AboutUsSerializers
    throttle_scope = 'get_request'
    """
    this page just for show to user (about_team(we))
    """
    def get(self,request):
        about_us = AboutUs.objects.filter(is_active=True)
        ser_data = AboutUsSerializers(instance=about_us,many=True)
        return Response(ser_data.data,status=status.HTTP_202_ACCEPTED)