from django.db import models

# Create your models here.
from apps.users.models import BaseModel


CATEGORY_CHOICES = (
    ("pxjg", "培训机构"),
    ("gr", "个人"),
    ("gx", "高校"),
)


class City(BaseModel):
    name = models.CharField(verbose_name="城市名", max_length=20)
    desc = models.CharField(verbose_name="城市描述", max_length=200)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    # 便于在进行后台管理的时候能够看到城市名称，return的值必须是上面定义过的，且是必填项，
    # 这样就不容易出现错误
    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(verbose_name="机构名称", max_length=50)
    desc = models.TextField(verbose_name="机构描述")
    tag = models.CharField(verbose_name="机构标签", max_length=10, default="全国知名")
    category = models.CharField(verbose_name="机构类别", choices=CATEGORY_CHOICES, max_length=4)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    image = models.ImageField(verbose_name="机构logo", upload_to="static/media/org/%Y/%m", max_length=100)

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    name = models.CharField(verbose_name="讲师姓名", max_length=30)
    work_years = models.IntegerField(verbose_name="工作年限", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=50)
    work_position = models.CharField(verbose_name="公司职位", max_length=50)
    points = models.CharField(verbose_name="教学特点", max_length=50)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    age = models.IntegerField(verbose_name="讲师年龄", default=18)
    image = models.ImageField(verbose_name="讲师头像", upload_to="static/media/teacher/%Y/%m", max_length=100)

    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name