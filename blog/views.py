# coding:utf-8
import logging
from django.shortcuts import render
from django.conf import settings
# Create your views here.
logger = logging.getLogger('blog.views')

# 调用全局配置中的信息
def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,
            }

def index(request):
    try:
        open('ss.txt', 'r')
    except Exception as e:
        pass
    return render(request, 'index.html', locals())