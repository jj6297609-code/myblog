import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http.response import JsonResponse
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User

from pyexpat.errors import messages
from .models import CaptchaModel, Profile
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import get_user_model, login, logout

User = get_user_model()


@require_http_methods(["GET", "POST"])
def mylogin(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            user = User.objects.get(email=email)
            if user and user.check_password(password):
                login(request, user)
                user.is_authenticated
                if not remember:
                    request.session.set_expiry(0)
                return redirect("/")
            else:
                print("邮箱或密码错误")
                form.add_error('email', '邮箱或密码错误')
                return render(request, "login.html", context={'form': form, 'error': "邮箱或密码错误"})


def mylogout(request):
    logout(request)
    return redirect("/")


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 创建用户
            User.objects.create_user(username=username, email=email, password=password)
            return redirect(reverse('blogauth:login'))
        # 验证失败，返回注册页面并显示错误
        return render(request, "register.html", {"form": form})
def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({"code": 400, "message": "必须传递邮箱！"})
    captcha = "".join(random.sample(string.digits, 4))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    print(captcha)
    send_mail("MyBlog注册验证码", message=f"您的注册验证码是：{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code": 200, "message": "验证码发送成功。"})
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, "profile.html", {
        "user": user,
        "profile": profile,
    })

def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("blogauth:profile", user_id=user.id)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "edit_profile.html", {"form": form})
