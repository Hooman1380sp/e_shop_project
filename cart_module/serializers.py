from rest_framework import serializers
from .models import CartDetail,Cart


class AddProductToCartSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    product_id = serializers.IntegerField()

class ReceiptOfMyShopSerializer(serializers.ModelSerializer):
     class Meta:
         model = Cart
         fields = '__all__'