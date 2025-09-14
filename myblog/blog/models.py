from django.contrib.auth.models import User
from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=200,verbose_name="分类名称")
    class Meta:
        verbose_name="博客分类"
        verbose_name_plural=verbose_name

class Blog(models.Model):
    title = models.CharField(max_length=200,verbose_name="标题")
    content = models.TextField(verbose_name="博客内容")
    time = models.DateTimeField(verbose_name="博客发布时间",auto_now=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE,verbose_name="博客分类")
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="博客作者")
    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name
        ordering=("-time",)

class BlogComment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    pub_time = models.DateTimeField(verbose_name="评论发布内容",auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="comments",verbose_name="所属博客")
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="作者")
    class Meta:
        verbose_name="博客评论"
        verbose_name_plural=verbose_name
        ordering=("-pub_time",)