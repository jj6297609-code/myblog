from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import CaptchaModel, Profile

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=20, min_length=2,
        error_messages={
            'required': '请输入用户名！',
            'max_length': '用户名长度在2-20之间！',
            'min_length': '用户名长度在2-20之间！'
        }
    )
    email = forms.EmailField(
        error_messages={
            'required': '请输入邮箱！',
            'invalid': '请输入正确的邮箱！'
        }
    )
    captcha = forms.CharField(
        max_length=4, min_length=4,
        error_messages={
            'max_length': '验证码长度不对！',
            'min_length': '验证码长度不对！'
        }
    )
    password = forms.CharField(
        max_length=20, min_length=6,
        widget=forms.PasswordInput,
        error_messages={
            'required': '请输入密码！',
            'min_length': '密码至少 6 位！'
        }
    )
    confirmation = forms.CharField(
        max_length=20, min_length=6,
        widget=forms.PasswordInput,
        error_messages={
            'required': '请确认密码！',
        }
    )

    # 单字段校验：邮箱
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已被注册')
        return email

    # 单字段校验：验证码
    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        email = self.cleaned_data.get('email')
        if not email:  # 如果邮箱本身就没通过校验，直接跳过
            return captcha
        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError('验证码和邮箱不匹配！')
        captcha_model.delete()
        return captcha

    # 跨字段校验：两次密码一致性
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation = cleaned_data.get('confirmation')
        if password and confirmation and password != confirmation:
            raise forms.ValidationError('两次密码不一致！')
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'requierd': '请输入邮箱！', 'invaild': '请输入正确的邮箱！'})
    password = forms.CharField(max_length=20, min_length=6, error_messages={})
    remember = forms.IntegerField(required=False)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "location", "website"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.TextInput(attrs={"class": "form-control"}),
        }
