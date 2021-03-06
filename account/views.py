from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from .forms import LoginForm,RegistrationForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form:
            username = request.POST.get('username',"")
            password = request.POST.get('password',"")
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
            else:
                return render(request,"account/error.html",{'message':"用户名或密码错误"})
        else:
            return HttpResponse('sorry')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})


def user_reg(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            username=reg_form.cleaned_data['username']
            email=reg_form.cleaned_data['email']
            password=reg_form.cleaned_data['password']
            #创建用户
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            #登录
            login(request,user)
            return redirect('/')
    else:
        reg_form=RegistrationForm()
    return render(request,'account/register.html',{'reg_form':reg_form})

def user_info(request):
    context = {}
    return render(request, 'account/user_info.html', context)

def user_logout(request):
    logout(request)
    return render(request,'account/logout.html')