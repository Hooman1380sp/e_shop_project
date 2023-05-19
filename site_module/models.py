from django.db import models

# Create your models here.

class SiteBanner(models.Model):
    class SiteBannerPosition(models.TextChoices):
        product_list = 'product_list', 'صفحه ی لیست محصولات'
        product_detail = 'product_detail', 'صفحه ی جزییات محصولات'
        about_us = 'about_us', 'صفحه ی درباره ما'
        index_page = 'index_page', 'صفحه ی اصلی سایت'
        category_list = 'category_list', 'صفحه لیست دسته بندی محصولات'
        category_detail = 'category_detail', 'صفحه جزییات دسته بندی محصولات'

    title = models.CharField(max_length=200,verbose_name='عنوان',db_index=True)
    url = models.URLField(max_length=400,verbose_name='آدرس بنر',blank=True,null=True)
    image = models.ImageField(upload_to='site/site_banner',verbose_name='تصویر بنر')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    position = models.CharField(max_length=200,choices=SiteBannerPosition.choices , verbose_name='جایگاه نمایشی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'