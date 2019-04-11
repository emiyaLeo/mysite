from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
"""继承django自带form"""
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="用户名",max_length=30,min_length=3,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}))
    email = forms.EmailField(label='邮箱',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'请输入邮箱'}))
    password = forms.CharField(label="密码",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))
    password2 = forms.CharField(label="密码",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请再次输入密码'}))

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']