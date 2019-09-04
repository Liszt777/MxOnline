from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from apps.organizations.models import CourseOrg, City


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_org = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.count()
        all_citys = City.objects.all()
        return render(request, 'org-list.html', {
            'all_org': all_org,
            'org_nums': org_nums,
            'all_citys': all_citys,
        })