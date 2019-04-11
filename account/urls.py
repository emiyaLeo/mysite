from django.urls import path,include
from .views import user_reg,user_info,user_login,user_logout

urlpatterns = [
    path('register/',user_reg,name = 'register'),
    path('login/',user_login,name = 'login'),
    path('logout/',user_logout,name = 'logout'),
    path('user_info/',user_info,name = 'user_info'),
    #使用django自带用户账户方法
    # path('',include('django.contrib.auth.urls')),
]