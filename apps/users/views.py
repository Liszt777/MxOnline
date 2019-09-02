from random import randint



from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse

from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from MxOnline.settings import yp_apikey
from apps.users.forms import LoginForm, DynamicLoginForm
from apps.utils.YunPian import send_single_sms


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data['mobile']
            for x in range(4):
                nums = [i for i in randint[1:10]]
                code = code + str(nums)
            res_json = send_single_sms(yp_apikey, code, mobile)
            if res_json["code"] == 0:
                re_dict['status'] = 'success'
            else:
                re_dict['msg'] = res_json['msg']

        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))

        login_form = DynamicLoginForm()
        return render(request, 'login.html', {
            "login_form": login_form,
        })

    def post(self, request):
        # user_name = request.POST.get("username", "")
        # password = request.POST.get("password", "")

        # if not user_name:
        #     return render(request, 'login.html', {"msg": "请输入用户名"})
        #
        # if not password or len(password) < 3:
        #     return render(request, 'login.html', {"msg": "密码错误，请重新输入"})
        # -----> 表单验证(通过form表单对登录框进行验证)
        login_form = LoginForm(request.POST)

        # 用form来判断用户输入是否有效
        if login_form.is_valid():
            # 用于通过用户和密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)

            if user is not None:
                # 查询到用户
                login(request, user)
                # 登录成功之后应该怎么返回页面
                # return render(request, 'index.html')
                return HttpResponseRedirect(reverse("index"))
            else:
                # 未查询到用户
                return render(request, 'login.html', {
                    "msg": "用户名或密码错误",
                    "login_form": login_form,
                })

        else:
            return render(request, 'login.html', {"login_form": login_form})
