from django.db import models

from apps.organizations.models import Teacher
from apps.users.models import BaseModel


#1.设计表结构有几个重要的点
"""
实体1 <关系> 实体2
课程 章节 视频（小节） 课程资源
"""
#2.实体的具体字段
#3.每个字段的类型，是否必填

DEGREE_CHOICES = (
    ("cj", "初级"),
    ("zj", "中级"),
    ("gj", "高级"),
)


class Course(BaseModel):
    name = models.CharField(verbose_name="课程名", max_length=20)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    degree = models.CharField(verbose_name="难度", choices=DEGREE_CHOICES, max_length=2)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    category = models.CharField(verbose_name="课程类别", max_length=20, default="")
    tag = models.CharField(verbose_name="课程标签", max_length=20, default="")
    youneed_know = models.CharField(verbose_name="课程须知", max_length=300, default="")
    teacher_tell = models.CharField(verbose_name="老师告诉你", max_length=300, default="")
    detail = models.TextField(verbose_name="课程详情", default="")
    image = models.ImageField(verbose_name="封面图", upload_to="courses/img/%Y/%m", max_length=100)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="所属讲师")

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # on_delete表示对应的外键被删除后，当前的数据该怎么办
    name = models.CharField(verbose_name="章节名", max_length=100)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="视频名", max_length=100)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    url = models.CharField(verbose_name="视频地址", max_length=200)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="课程资源名称", max_length=100)
    file = models.FileField(verbose_name="下载地址", upload_to="courses/resources/%Y/%m", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name