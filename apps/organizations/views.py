from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organizations.models import CourseOrg, City


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_org = CourseOrg.objects.all()
        all_citys = City.objects.all()

        # 通过机构类别对课程机构进行筛选
        category = request.GET.get("ct", '')

        if category:
            all_org = all_org.filter(category=category)

        # 通过所在城市对课程机构进行筛选
        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_org = all_org.filter(city_id=int(city_id))

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
        })