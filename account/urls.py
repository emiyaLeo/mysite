from django.urls import path,include
from .views import user_reg,user_info

urlpatterns = [
    path('register/',user_reg,name = 'register'),
    path('user_info/',user_info,name = 'user_info'),
    #使用django自带用户账户方法
    path('',include('django.contrib.auth.urls')),
]