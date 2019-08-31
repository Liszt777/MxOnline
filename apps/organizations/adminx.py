import xadmin

from apps.organizations.models import Teacher, City, CourseOrg


class CityAdmin(object):
    # 进入到城市展示列表的时候会展现的字段
    list_display = ['id', 'name', 'desc', 'add_time']
    # 搜索框内可供搜索的字段
    search_fields = ['name', 'desc']
    # 过滤标签内可选择的过滤字段
    list_filter = ['name', 'desc', 'add_time']
    # 添加该变量后可使同样在list_display中的字段获得更加方便的修改
    list_editable = ['name', 'desc']


class CourseOrgAdmin(object):
    list_display = ['name', 'tag', 'category', 'city', 'add_time']
    search_fields = ['name', 'tag', 'category', 'city']
    list_filter = ['city', 'category', 'tag', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'age', 'org', 'work_years', 'work_company', 'add_time']
    search_fields = ['name', 'org']
    list_filter = ['org', 'work_years', 'add_time']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)