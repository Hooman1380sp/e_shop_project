from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=20, min_length=8)

    class Meta:
        model = User
        fields = ["email", "password", "confirm_password"]
        # extra_kwargs = {
        #     "password": {"write_only": True},
        # }

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(detail="password not equal with confirm-password")
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=20, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "confirm_password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(detail="password not equal with confirm-password")
        del data["confirm_password"]
        return data


class UserForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)


class UserResetPasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=20, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("password", "confirm_password")

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(detail="password not equal with confirm-password")
        del data["confirm_password"]
        return data


class ChangePasswordAccountSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=20, min_length=8, write_only=True)
    new_password = serializers.CharField(max_length=20, min_length=8, write_only=True)


class EditUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "Address", "phone_number"]
