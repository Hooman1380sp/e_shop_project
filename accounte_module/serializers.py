from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم

User = get_user_model() # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']#,'username']
        # extra_kwargs = {
        #     'username':{'required':False},
        # }

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']


class UserForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email',]

class UserResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password',]

class ChangePasswordAccoutSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=22,min_length=5,write_only=True)
    new_password = serializers.CharField(max_length=22,min_length=5,write_only=True)

class EditUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','Address','phone_number']
