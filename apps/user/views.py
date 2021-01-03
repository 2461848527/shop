# authenticate为授权
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect,reverse,render
from django.contrib.auth import authenticate,login
from .models import User
import re
# Create your views here.

def login(request):
    if request.method == 'GET':
        '''访问登录页面'''
        return render(request,'user/login.html')
    else:
        '''登录校验'''
        # 接受数据
        # print(request.POST)
        username = request.POST.get('log_name')
        password = request.POST.get('log_pass')
        print(username,password)
        # 校验数据
        if not all([username,password]):
            return redirect(request,'user/loign.html',{'errmsg':'数据不完整'})
        # 校验输入的账号密码
        res = User.objects.filter(username=username, password=password)
        if res:
            print(1)
            email = User.objects.filter(username=username).values()[0]['email']
            # 存储session
            request.session['msg'] = {'email': email}
            # 将判断成功的数据返回给前端
            res = {'status': 0, 'form': '/'}
        else:
            res = {'status': 1, 'form': 'user:login'}
        return JsonResponse(res)

        # 业务处理：登录校验
        # user = authenticate(username=username, password=password)
        # print(user)


def logout_view(request):
    """退出登录"""
    logout(request)
    return redirect(reverse('index'))


# 只能通过post方式进行请求
# @require_POST
def register(request):
    """注册功能实现"""
    if request.method == 'GET':
        # 显示注册页面
        return render(request,'user/register.html')
    else:
        # print('-'*100)
        print(request.POST)
        # 进行注册逻辑
        username = request.POST.get('logname')
        # print(username)
        password1 = request.POST.get('logpass')
        password2 = request.POST.get('logpass2')
        email = request.POST.get('logemail')

        # 进行数据校验
        if not all([username,password1,password2,email]):
            # 数据不完整
            print(email)
            return render(request,'user/register.html',{'errmsg':'数据不完整'})

        # 校验邮箱
        # if not re.match(r'/^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/',email):
        #     return render(request,'user/register.html',{'errmsg':'邮箱格式不正确'})
        print(1, ')' * 100)
        # 校验两次密码是否一致
        if password1 != password2:
            print(username)
            return render(request,'user/register.html',{'errmsg':'密码不一致'})
        print(2, ')' * 100)
        # 进行业务处理：进行用户注册
        user = User.objects.create(username=username, email=email, password=password1)
        res = {'status': 0, 'form': f'/user/login'}
        return JsonResponse(res)


        # 返回应答，跳转到首页



