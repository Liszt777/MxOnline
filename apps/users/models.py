from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        abstract = True


# 自定义userprofile表覆盖默认的user表
class UserProfile(AbstractUser):
    nickname = models.CharField(verbose_name="昵称", max_length=50, default="我是一个学员")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    mobile = models.CharField(verbose_name="手机号码", max_length=11)
    address = models.CharField(verbose_name="地址", max_length=100, default="")
    image = models.ImageField(verbose_name="头像", upload_to="static/media/image/%Y/%m", max_length=100, default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username