from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('login/',views.login,name='login'), # 登录
    path('register/', views.register,name='register'), # 注册
]


