from django.contrib import admin
from .models import Product, ProductCategory, ProductVisit

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductVisit)
