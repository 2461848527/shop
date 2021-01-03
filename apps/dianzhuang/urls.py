from django.urls import path, re_path
from . import views

app_name = "dianzhuang"

urlpatterns = [
    path('',views.index,name='index'), # 首页
    path('design/',views.design,name='design'), # 设计
    path('youshi/',views.youshi,name='youshi'), # 优势
    path('case/',views.case,name='case'), # 案例
    path('team/',views.team,name='team'), # 团队
    path('about/',views.about,name='about'), # 关于
    path('news/',views.news,name='news'), # 资讯
    path('contact/',views.contact,name='contact'), # 联系
]


