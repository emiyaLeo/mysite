from django.shortcuts import render,redirect,reverse,get_object_or_404
from blog.models import Blog
from .forms import CommentForm
from django.http import JsonResponse


# Create your views here.
def update_comment(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.to_blog = blog
            new_comment.save()
            return redirect(reverse('blog_detail', args=(blog_pk,)))
    else:
        return redirect(reverse('blog_detail', args=(blog_pk,)))
    #     comment_form = CommentForm()
    # context = {}
    # context['comment_form'] = comment_form
    # return render(request,'blog/blog_detail.html',context)