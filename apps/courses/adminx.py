import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag


class CourseAdmin(object):
    list_display = ['name', 'teacher', 'degree', 'desc', 'detail', 'learn_times']
    search_fields = ['name', 'teacher', 'degree']
    # 在外键的字段后面加上__(两个下划线)和外键相应的字段，就能对外键的这个字段进行过滤，如下'teacher__name'
    list_filter = ['name', 'teacher__name', 'degree', 'learn_times', 'add_time']
    list_editable = ['desc', 'degree', 'learn_times']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time', 'learn_times']
    search_fields = ['name', 'course']
    list_filter = ['name', 'add_time', 'course']


class VideoAdmin(object):
    list_display = ['lesson' ,'name', 'add_time', 'learn_times', 'url']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'add_time', 'lesson']


class CourseResourceAdmin(object):
    list_display = ['course' ,'name', 'file']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course', 'add_time']


class CourseTagAdmin(object):
    list_display = ['course', 'tag', 'add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)