from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from product_module.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True,blank=True,verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

class CartDetail(models.Model):
    cart_shop = models.ForeignKey(to=Cart,on_delete=models.CASCADE,verbose_name='سبد خرید')
    product = models.ForeignKey(to=Product,on_delete=models.CASCADE,verbose_name='محصول')
    final_price = models.IntegerField(null=True,blank=True,verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return str(self.cart_shop)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبد خرید'