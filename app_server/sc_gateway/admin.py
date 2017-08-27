# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import GatewayInfo
# Register your models here.
@admin.register(GatewayInfo)
class GatewayInfoAdmin(admin.ModelAdmin):
    # 自定义显示
    list_display = ['id', 'guser','gdid','gname', 'gmac', 'gpasscode']
    # 过滤器
    list_filter = ['guser']
    # 搜索功能
    search_fields = ['guser']
    # 每页显示多少条数据
    list_per_page = 10
    # 修改,添加页分组
    fieldsets = [('base', {'fields': ['guser']}),]