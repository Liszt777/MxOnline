from django.db import models

from django.contrib.auth import get_user_model

from apps.courses.models import Course
from apps.users.models import BaseModel


user = get_user_model()
# 为防止当不使用userprofile时，而使用django自带的user时而产生的麻烦（或者是使用其他的表），
# 我们使用settings中的AUTH_USER_MODEL中的内容，因此当改用其他的表时，我们只需要改动AUTH_USER_MODEL即可

FAV_TYPE_CHOICES = (
    (1, "课程"),
    (2, "机构"),
    (3, "讲师"),
)


class UserAsk(BaseModel):
    name = models.CharField(verbose_name="咨询人名称", max_length=10)
    mobile = models.CharField(verbose_name="咨询人手机号", max_length=11)
    course_name = models.CharField(verbose_name="被咨询课程名", max_length=50)

    class Meta:
        verbose_name = "未注册用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course}({mobile})"\
            .format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    comments = models.CharField(verbose_name="评论内容", max_length=200)

    user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFav(BaseModel):
    fav_type = models.IntegerField(verbose_name="收藏类型", choices=FAV_TYPE_CHOICES)
    fav_id = models.IntegerField(verbose_name="对应类型数据的主键ID")

    user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name="用户")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.name, id=self.fav_id)


class UserMessage(BaseModel):
    message = models.CharField(verbose_name="消息内容", max_length=200)
    has_read = models.BooleanField(verbose_name="是否已读", default=False)

    user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name="用户")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name
