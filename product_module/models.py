from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=190)
    slug = models.SlugField(max_length=220, unique=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField()

    def __str__(self):
        return self.title[:90]


class Product(models.Model):
    title = models.CharField(max_length=190, db_index=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, related_name='product_category')
    price = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=220, blank=False, editable=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField()
    image = models.ImageField(upload_to='product/image')

    def __str__(self):
        return f'{self.title} - {self.price} --{self.category.title[:90]}'


class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return f'{self.product.title[:50]} - {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصولات'
        verbose_name_plural = 'بازدید های محصولات'
