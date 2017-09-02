# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import JsonResponse
from .models import GatewayInfo
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from serializers import GatewaySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
class JSONResponse(HttpResponse):
    """
    用于返回JSON数据.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



# 网关列表
@csrf_exempt
def gateway(request):
    #获取网关列表
    if request.method == 'GET':
        gateway = GatewayInfo.objects.all()
        serializer = GatewaySerializer(gateway, many=True)
        return JSONResponse(serializer.data)
    #添加网关
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GatewaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.data,status=400)

# 指定用户的网关列表
@csrf_exempt
def gateway_list(request,pk):
    try:
        gateways = GatewayInfo.objects.filter(guser=pk)
    except gateways.DoesNotExist:
        return HttpResponse(status=404)
    #获得指定网关的信息
    if request.method == 'GET':
        serializer = GatewaySerializer(gateways,many=True)
        if len(gateways)<1:
            return HttpResponse(status=404)
        return JSONResponse(serializer.data,status=200)

# 网关列表
@csrf_exempt
def gateway_detail(request,pk):
    """
    修改或删除一个gateway.
    """
    try:
        gateway = GatewayInfo.objects.get(pk=pk)
    except gateway.DoesNotExist:
        return HttpResponse(status=404)
    #获得指定网关的信息
    if request.method == 'GET':
        serializer = GatewaySerializer(gateway)
        return JSONResponse(serializer.data)
    #修改指定网关的信息
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GatewaySerializer(gateway,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    #删除指定网关信息
    elif request.method == 'DELETE':
        gateway.delete()
        return HttpResponse(status=204)

