from django.contrib import admin
from .models import SiteBanner


# Register your models here.

class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']


admin.site.register(SiteBanner,SiteBannerAdmin)