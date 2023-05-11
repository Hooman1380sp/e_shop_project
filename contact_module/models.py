from django.db import models
from django.contrib.auth import get_user_model # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم
User = get_user_model() # زمانی که یک user جنگو سفارشی درست میکنیم باید به این شکل مدل user را معرفی کنیم


# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=180,verbose_name='عنوان')
    full_name = models.CharField(max_length=220,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200,verbose_name='ایمیل')
    message = models.TextField(verbose_name='متن دریافت شده')
    response = models.TextField(verbose_name='متن پاسخ, متن دریافت شده',null=True,blank=True)
    created_data = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    is_read_by_admin = models.BooleanField(default=False,verbose_name='خوانده شده توسط ادمین')
    ip = models.CharField(max_length=40,verbose_name='آی پی کاربر')
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='کاربر',null=True,blank=True)


    def __str__(self):
        return f'{self.title} - {self.message[:30]} - {self.ip}'

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

class AboutUs(models.Model):
    team_name = models.CharField(max_length=200,db_index=True,verbose_name='نام تیم')
    phone_team = models.PositiveIntegerField(verbose_name='تلفن گروه')
    address = models.TextField(verbose_name='آدرس مجموعه')
    logo_image = models.ImageField(upload_to='contact_us/about_us',verbose_name='تصویر لوگو')
    about_team = models.TextField(verbose_name='توضیحات درباره تیم')
    is_active = models.BooleanField(default=True,verbose_name='فعال / غیر فعال')

    def __str__(self):
        return f'{self.is_active}'


    class Meta:
        verbose_name = 'فرم درباره ما'
        verbose_name_plural = 'فرم های درباره ما'