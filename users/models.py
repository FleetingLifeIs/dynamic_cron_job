from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 集成内置的user模型,并添加新的字段
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birday = models.DateField(null=True, blank=True, verbose_name='生日')
    choice_gender = (
        ("male", "男"),
        ("female", "女"),
    )
    gender = models.CharField(choices=choice_gender, default='male', max_length=5, verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"

    def __unicode__(self):
        return self.username
