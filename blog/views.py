from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum
from read_statistics.views import read_statistics_once_read
from comment.models import Comment
from comment.forms import CommentForm
from django.urls import reverse

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    page_num = request.GET.get('page',1)
    paginator = Paginator(blogs,10)
    page_of_blogs = paginator.page(page_num)

    context={}
    context['page_of_blogs'] = page_of_blogs
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = Blog.objects.dates('create_time','month',order='DESC')
    response = render(request,'blog/blog_list.html', context)
    return response

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request,blog)
    comments = Comment.objects.filter(to_blog=blog)
    # if not request.COOKIES.get('blog_%s_read'% blog_pk): #判断cookie，总阅读数加1
    #     ct = ContentType.objects.get_for_model(Blog)
    #     readnum,created = ReadNum.objects.get_or_create(content_type=ct,object_id=blog.pk)
    #     readnum.read_num += 1
    #     readnum.save()

    # if request.method =='POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.user = request.user
    #         new_comment.to_blog = blog
    #         new_comment.save()
    #         return redirect(reverse('blog_detail',args=(blog_pk,)))
    # else:
    #     comment_form = CommentForm()



    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    context['comment_form'] = CommentForm()
    context['comments'] = comments
    context['previous_blog'] = Blog.objects.filter(create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt=blog.create_time).first()
    response = render(request, 'blog/blog_detail.html', context)
    response.set_cookie(read_cookie_key,'true')
    return response


def blogs_with_type(request,blogs_with_type):
    blog_type = get_object_or_404(BlogType, pk=blogs_with_type)
    blogs = Blog.objects.filter(blog_type=blog_type)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs, 10)
    page_of_blogs = paginator.page(page_num)

    context = {}
    context['blogs'] = blogs
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = Blog.objects.dates('create_time', 'month', order='DESC')
    context['page_of_blogs'] = page_of_blogs
    return render(request,'blog/blogs_with_type.html',context)

def blogs_with_date(request,year,month):

    blogs = Blog.objects.filter(create_time__year=year,create_time__month=month)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs, 10)
    page_of_blogs = paginator.page(page_num)

    context = {}
    context['blogs'] = blogs
    context['blogs_with_date'] = "%s年%s月" % (year,month)
    context['blog_dates'] = Blog.objects.dates('create_time', 'month', order='DESC')
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['page_of_blogs'] = page_of_blogs
    return render(request, 'blog/blogs_with_date.html', context)

