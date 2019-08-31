from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass

# 将model注册到后台管理系统中去
# useradmin可以将在后台管系统创建的新用户的密码转为密文
#admin.site.register(UserProfile, UserAdmin)