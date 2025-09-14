from django.urls import path
from . import views

app_name = "blogauth"
urlpatterns = [
    path("login",views.mylogin,name="login"),
    path("register",views.register,name="register"),
    path("captcha",views.send_email_captcha,name="email_captcha"),
    path("logout",views.mylogout,name="logout"),
    path("profile/<int:user_id>/",views.profile,name="profile"),
    path("edit_profile/<int:user_id>/",views.edit_profile,name="edit_profile"),
]