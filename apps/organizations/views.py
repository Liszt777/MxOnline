from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organizations.forms import AddAskForm
from apps.organizations.models import CourseOrg, City


class AddAskView(View):
    """
    处理用户的咨询
    """
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            # 将前端传来的数据存到数据库中（commit=True），而不是仅仅提交而已，返回的是user_ask实例,不是form
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "咨询失败，请核实所填信息",
            })


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_org = CourseOrg.objects.all()
        all_citys = City.objects.all()
        # 按点击数进行排名
        hot_org = all_org.order_by("-click_nums")[:3]

        # 通过机构类别对课程机构进行筛选
        category = request.GET.get("ct", '')

        if category:
            all_org = all_org.filter(category=category)

        # 通过所在城市对课程机构进行筛选
        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_org = all_org.filter(city_id=int(city_id))

        # 对课程机构进行排序
        sort = request.GET.get('sort', '')
        if sort == "students":
            all_org = all_org.order_by("-students")
        if sort == "courses":
            all_org = all_org.order_by("-course_nums")

        org_nums = all_org.count()

        # 对课程机构数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, per_page=5, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_org': orgs,
            'org_nums': org_nums,
            'all_citys': all_citys,
            'category': category,
            'city_id': city_id,
            'sort': sort,
            "hot_org": hot_org,
        })