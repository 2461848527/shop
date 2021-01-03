
from django.urls import path,include


urlpatterns = [
    path('tinymce/',include("tinymce.urls")),  # 富文本编辑器路由
    path('user/', include("user.urls",namespace="user")),  # 用户路由
    path('order/',include("order.urls",namespace="order")),  # 订单路由
    path('cases/',include("cases.urls",namespace="cases")),  # 订单路由
    path('cms/',include("cms.urls",namespace="cms")),  # 订单路由
    path('', include("dianzhuang.urls",namespace="dianzhuang")),  # 案例路由
]


