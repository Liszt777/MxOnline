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
    image = models.ImageField(verbose_name="机构logo", upload_to="org/%Y/%m", max_length=100)
    address = models.CharField(max_length=150, verbose_name="机构地址", default="无")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")

    is_auth = models.BooleanField(verbose_name="是否认证", default=False)
    is_gold = models.BooleanField(verbose_name="是否金牌", default=False)

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def courses(self):
        # 把包放在这里是为了避免循环引用而出错，动态语言调用这个方法时才会运行，所以在这里调用不会出错
        # from apps.courses.models import Course
        # courses = Course.objects.filter(course_org=self)
        # 上面的方法虽然能够实现功能，但还是让人觉得不舒服（因为循环引用了）
        # 由于courses中的models中的Course外键关联了CourseOrg，所以自然而然的CourseOrg反向关联了Course(这是models自动帮我们完成的)
        courses = self.course_set.filter(is_classics=True)[:5]  # 这里的course_set类似于objects的功能
        return courses

class Teacher(BaseModel):
    name = models.CharField(verbose_name="讲师姓名", max_length=30)
    work_years = models.IntegerField(verbose_name="工作年限", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=50)
    work_position = models.CharField(verbose_name="公司职位", max_length=50)
    points = models.CharField(verbose_name="教学特点", max_length=50)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    age = models.IntegerField(verbose_name="讲师年龄", default=18)
    image = models.ImageField(verbose_name="讲师头像", upload_to="teacher/%Y/%m", max_length=100)


    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name