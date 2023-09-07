from rest_framework import serializers
from .models import ProductCategory,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['is_delete',]
        # read_only_fields = True

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =ProductCategory
        exclude =  ['is_delete',]