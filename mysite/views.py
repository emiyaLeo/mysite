from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from read_statistics.views import get_today_hot_data,get_yesterday_hot_data,get_7days_hot_data
from blog.models import Blog
from django.core.cache import cache


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    blogs = Blog.objects.all().order_by('-create_time')
    today_hot_data = get_today_hot_data(blog_content_type)
    yesterday_hot_data = get_yesterday_hot_data(blog_content_type)

    #获取7天热门博客的缓存数据
    hot_data_for_7days = cache.get('hot_data_for_7days')
    if hot_data_for_7days is None:
        hot_data_for_7days = get_7days_hot_data()
        cache.set('hot_data_for_7days',get_7days_hot_data(),3600)
        print('set cache')
    else:
        print('use cache')


    context={}
    context['blogs'] = blogs[:7]
    context['today_hot_data'] = today_hot_data
    context['yesterday_hot_data'] = yesterday_hot_data
    context['hot_data_for_7days'] = hot_data_for_7days

    return render(request,'home.html',context)


