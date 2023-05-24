from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from product_module.models import Product,ProductCategory,ProductVisit
from contact_module.models import ContactUs,AboutUs
from site_module.models import SiteBanner
from cart_module.models import Cart,CartDetail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
