import xadmin

from apps.operations.models import UserAsk, CourseComments, UserCourse, UserFav, UserMessage


# 后台管理系统的全局配置,可以放在任意一个adminx.py文件中都有效
class GlobalSettings(object):
    site_title = 'MX在线管理系统'
    site_footer = 'MX在线'
    # menu_style = 'accordion'  将各模块的子目录进行了一个归整


class BaseSettings(object):
    # 打开自带的后台管理系统的主题选择
    enable_themes = True
    use_bootswatch = True


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['course_name']
    list_filter = ['course_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserFavAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'has_read']
    list_filter = ['user', 'has_read', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)