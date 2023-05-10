from django.db import models
from accounte_module.models import User
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
