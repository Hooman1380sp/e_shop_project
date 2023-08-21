from rest_framework import serializers
from product_module.models import Product, ProductCategory, ProductVisit
from contact_module.models import ContactUs, AboutUs
from site_module.models import SiteBanner
from cart_module.models import Cart, CartDetail
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVisit
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class SiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBanner
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = "__all__"
