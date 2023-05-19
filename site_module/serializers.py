from rest_framework import serializers
from .models import SiteBanner

class SiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model =SiteBanner
        exclude = ['is_active',]
