# coding:utf-8
from django.contrib import admin
from blog.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'avatar', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('first_name', 'last_name', 'qq', 'mobile',)
        }),
    )
    list_display = ['username', 'qq', 'avatar']
    list_filter = ['username', 'qq']


class ArticleAdmin(admin.ModelAdmin):
    # fields = ('title', 'desc', 'content')
    list_display = ('title', 'desc')
    list_filter = ('title', 'click_count')
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', 'user', 'tag', 'category')
        }),
    )

    class Media:
         js = (
             '/static/js/kindeditor-4.1.10/kindeditor-min.js',
             '/static/js/kindeditor-4.1.10/lang/zh-CN.js',
             '/static/js/kindeditor-4.1.10/config.js',
         )


admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)