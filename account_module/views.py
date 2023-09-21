from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework_simplejwt.tokens import RefreshToken  # برای درست کردن توکن jwt قبل از ریجیستر

from .permissions import PermissionEditUserProfile
from .serializers import (
    UserLoginSerializer,
    UserRegisterSerializer,
    UserResetPasswordSerializer,
    UserForgotPasswordSerializer,
    ChangePasswordAccountSerializer,
    EditUserProfileSerializer,
)
from .utils import SendMail

# Create your views here.

# def get_token_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
User = get_user_model()  # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم


@extend_schema_view(
    post=extend_schema(
        responses={
            201: "create",
            400: "not is valid",
            406: "user already is exist",
        },
        tags=["Account"],
        description="to display whole products",
    )
)
class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    """
    create a new user (user register page)

    """

    def post(self, request):
        ser_date = self.serializer_class(data=request.data)
        ser_date.is_valid(raise_exception=True)
        user_email = ser_date.validated_data.get("email")
        user_password = ser_date.validated_data.get("password")
        if User.objects.filter(email__iexact=user_email).exists():
            return Response(data=ser_date.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            random_str = get_random_string(84)
            new_user = User(email=user_email, username=user_email, is_active=False, email_active_code=random_str)
            new_user.set_password(user_password)
            # get_token_for_user(new_user)
            new_user.save()
            address = "https://Hoomansp80.pythonanywhere.com/api/account/activate-account/"
            SendMail(to=user_email, address=address, random_str=random_str)
            return Response(data=ser_date.data, status=status.HTTP_201_CREATED)


class ActivateAccountView(APIView):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            user.is_active = True
            user.email_active_code = get_random_string(84)
            user.save()
            return Response({"message": "now your accounted is active"}, status=status.HTTP_200_OK)
        return redirect("https://Hoomansp80.pythonanywhere.com")


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    """
    page login view
    """

    def post(self, request):
        ser_data = self.serializer_class(data=request.data)
        ser_data.is_valid(raise_exception=True)
        user_email = ser_data.validated_data.get("email")
        user_password = ser_data.validated_data.get("password")
        user: User = User.objects.filter(email=user_email).first()
        if user is not None:
            if not user.is_active:
                return Response({"message": "اکانت شما فعال نشده است"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                if user_email == user.email:
                    if user.check_password(user_password):
                        login(request, user)
                        return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
                    return Response({"message": "کلمه عبور وارد شده اشتباه است"}, status=status.HTTP_400_BAD_REQUEST)
                return Response({"message": "ایمیل وارد شده اشتباه است"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"message": "کاربری با مشخصات شما یافت نشده است"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("https://Hoomansp80.pythonanywhere.com")


class UserForgotPasswordView(APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    serializer_class = UserForgotPasswordSerializer
    """
    page forget password
    """

    def post(self, request):
        ser_data = self.serializer_class(data=request.data)
        ser_data.is_valid(raise_exception=True)
        user_email = ser_data.validated_data.get("email")
        user = User.objects.filter(email__iexact=user_email).first()
        if user is not None:
            random_str = user.email_active_code
            address = "https://Hoomansp80.pythonanywhere.com/api/account/activate-account/"
            SendMail(to=user_email, address=address, random_str=random_str)
            return Response(data=ser_data.data, status=status.HTTP_202_ACCEPTED)
        return Response({"message": "ایمیل وارد شده, قبلا ثبت نام نکرده است "}, status=status.HTTP_406_NOT_ACCEPTABLE)
        # return Response({'message': 'در وارد کردن اطلاعات خود دقت کنید'}, status=status.HTTP_400_BAD_REQUEST)


class UserResetPasswordView(APIView):
    serializer_class = UserResetPasswordSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    """
    page reset password!
    """

    def post(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is not None:
            ser_data = UserResetPasswordSerializer(instance=user, data=request.data)
            ser_data.is_valid(raise_exception=True)
            # ser_data.save() # این روش غیر امنیتی هست
            user_password = ser_data.validated_data.get("password")
            user.set_password(user_password)
            user.is_active = True
            user.email_active_code = get_random_string(84)
            user.save()
            return Response(data=ser_data.data, status=status.HTTP_202_ACCEPTED)
        return Response({"message": "کاربری با همچنین ایمیلی ثبت نشده است"}, status=status.HTTP_404_NOT_FOUND)


class EditUserProfileView(APIView):
    serializer_class = EditUserProfileSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [
        PermissionEditUserProfile,
    ]
    """
    this page for edit profile

    """

    def put(self, request):
        current_user: User = User.objects.filter(id=request.user.id).first()
        self.check_object_permissions(request, current_user)
        ser_data = self.serializer_class(instance=current_user, data=request.data, partial=True)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        return Response(data=ser_data.data, status=status.HTTP_206_PARTIAL_CONTENT)


class ChangePasswordAccountView(APIView):
    serializer_class = ChangePasswordAccountSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [PermissionEditUserProfile]

    """
    change password
    have tow field
    new_password == str
    current_password == str
    """

    def post(self, request):
        user: User = User.objects.filter(id=request.user.id).first()
        ser_data = self.serializer_class(data=request.data)
        ser_data.is_valid(raise_exception=True)
        current_password = ser_data.validated_data.get("current_password")
        new_password = ser_data.validated_data.get("new_password")
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            return Response(data=ser_data.data, status=status.HTTP_202_ACCEPTED)
        return Response({"message": "کلمه عبور اشتباه میباشد"}, status=status.HTTP_409_CONFLICT)
