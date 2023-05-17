from rest_framework import serializers
from .models import CartDetail


class AddProductToCartSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    product_id = serializers.IntegerField()