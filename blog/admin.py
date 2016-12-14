# coding:utf-8
from django.contrib import admin
from blog.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ('title', 'desc', 'content')

class ArticleAdmin(admin.ModelAdmin):
    # fields = ('title', 'desc', 'content')
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', )
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)