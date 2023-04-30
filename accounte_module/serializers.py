from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم

User = get_user_model() # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم


class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','username','is_active','email_active_code']
        extra_kwargs = {
            'username':{'required':False},
            'is_active':{'required':False},
            'email_active_code' : {'required':False}
        }


class UserForgotPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email',]

class UserResetPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password',]