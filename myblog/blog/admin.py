from django.contrib import admin
from .models import Blog,BlogComment,BlogCategory

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = [ 'name' ]
    def __str__(self):
        return self.name



class BlogAdmin(admin.ModelAdmin):
    list_display = [ 'title','category','content','author','time' ]
    def __str__(self):
        return self.title



class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['content','pub_time','blog','author']
    def __str__(self):
        return self.content
    class Meta:
        verbose_name="博客评论"
        verbose_name_plural=verbose_name

admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
admin.site.register(Blog,BlogAdmin)