from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CaptchaModel(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=4)
    create_time = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField("个人简介", blank=True, null=True)
    location = models.CharField("所在地", max_length=100, blank=True, null=True)

    website = models.TextField("个人网站", blank=True, null=True)

def __str__(self):
        return f"{self.user.username} 的简介"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()