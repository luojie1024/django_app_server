# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import JsonResponse
from .models import GatewayInfo

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from serializers import GatewaySerializer

# Create your views here.
# 注册处理
@csrf_exempt
def create(request):
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = GatewaySerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'success': True})
    #     else:
            return JsonResponse({'success': False})


# 判断用户是否已经存在
@csrf_exempt
def update(request):
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     uphone = data['uphone']
    #     count = GatewayInfo.objects.filter(uphone=uphone).count()
    #     if count == 0:
    #         return JsonResponse({'success': False})
    #     else:
            return JsonResponse({'success': True})


# 登录
@csrf_exempt
def delete(request):
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     uphone=data['uphone']
    #     upwd = data['upwd']
    #     users = GatewayInfo.objects.filter(uphone=uphone)
    #     if len(users) == 1:
    #       if upwd == users[0].upwd:
    #           return JsonResponse({'success': True})
    #       else:
    #           return JsonResponse({'success': False})
    #     else:
            return JsonResponse({'success': False})

# 判断用户是否已经存在
@csrf_exempt
def retrieve(request):
    return JsonResponse({'success': False})
