# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import UserInfo
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # 自定义显示
    list_display = ['id', 'uname', 'uphone', 'upwd']
    # 过滤器
    list_filter = ['uphone']
    # 搜索功能
    search_fields = ['uphone']
    # 每页显示多少条数据
    list_per_page = 10
    # 修改,添加页分组
    fieldsets = [('base', {'fields': ['uphone']}),
                 ('super', {'fields': ['uname']})
                 ]