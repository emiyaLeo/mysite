from django.shortcuts import render
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum,ReadDetail
from blog.models import Blog


# Create your views here.
def read_statistics_once_read(request, obj):
    """
        作用：阅读+1的处理逻辑功能
        request：请求对象
        obj：post实例对象
    """
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        # 如果使用get_or_create就能省略上面一大段，可以简化
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)

        # 总阅读计数+1
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数+1
        date = timezone.now().date()
        readdetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readdetail.read_num += 1
        readdetail.save()
    return key


def get_seven_days_read(content_type):
    today = timezone.now().date()
    read_nums = []
    for i in range(7,-1,-1):
        date = today - datetime.timedelta(days=i)
        read_details = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return read_nums


def get_today_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type,date=today).order_by('-read_num')
    return read_details[:7]

def get_yesterday_hot_data(content_type):
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type,date=yesterday).order_by('-read_num')
    return read_details[:7]

def get_7days_hot_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lt=today,read_details__date__gte=date)\
                .values('id','title')\
                .annotate(read_num_sum=Sum('read_details__read_num'))\
                .order_by('-read_num_sum')
    return blogs[:7]



