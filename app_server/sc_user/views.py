# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import JsonResponse
from .models import UserInfo

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import UserSerializer


# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = UserInfo.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = UserInfo.objects.get(pk=pk)
#     except UserInfo.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(snippet)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         else:
#             return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


# @api_view(http_method_names=['GET'])
# @permission_classes((permissions.AllowAny,))
# def getUserList(request):
#     return Response([
#         {"name": "admin", "password": "123"},
#         {"name": "auditor", "password": "456"},
#     ])
#
#
# @api_view(http_method_names=['POST'])
# @permission_classes((permissions.AllowAny,))
# def setUser(request):
#     return Response({
#         "data": request.data,
#         "test": "111"
#     })


# 注册处理
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})


# 登录
@csrf_exempt
def login_old(request,pk):
    if request.method == 'GET':
        users = UserInfo.objects.filter(uphone=pk)
        pk = users[0].id
        try:
            user = UserInfo.objects.get(pk=pk)
        except user.DoesNotExist:
            return HttpResponse(status=404)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=200)


# 判断用户是否已经存在
@csrf_exempt
def register_is_exist(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        uphone = data['uphone']
        count = UserInfo.objects.filter(uphone=uphone).count()
        if count == 0:
            return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': True})


# 登录
@csrf_exempt
def login_handle(request, pk):
    try:
        user = UserInfo.objects.get(pk=pk)
    except user.DoesNotExist:
        return HttpResponse(status=404)
    #
    if request.method == 'POST':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    # 获得指定用户的信息
    elif request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)
    # 修改指定用户的信息（忘记密码）
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            user = UserInfo.objects.get(pk=pk)
        except user.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    # 删除指定用户信息
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


# 登录
@csrf_exempt
def login(request):
    if request.method == 'GET':
        users = UserInfo.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)
    # 注册
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.data, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        uphone = data['uphone']
        upwd = data['upwd']
        # 查询对应手机号的用户
        users = UserInfo.objects.filter(uphone=uphone)
        # 判断用户是否存在
        if len(users) < 1:
            return HttpResponse(status=404)
        # 获得用户的PK
        pk = users[0].id
        try:
            user = UserInfo.objects.get(pk=pk)
        except user.DoesNotExist:
            return HttpResponse(status=404)
        # 修改密码
        user.upwd = upwd
        # 序列化
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# 登录处理
# def login_handle(request):
#     # 接收请求信息
#     get = request.POST
#     uname = get.get('username')
#     upwd = get.get('pwd')
#     jizhu = get.get('jizhu', 0)
#     # 根据用户名查询对象
#     users = UserInfo.objects.filter(uname=uname)
#     print uname
#     # 判断如果未查到则用户名错，查到再判断密码是否正确，正确则转到用户中心
#     if len(users) == 1:
#         s1 = sha1()
#         s1.update(upwd)
#         if s1.hexdigest() == users[0].upwd:
#             # red = HttpResponseRedirect('/user/info')
#             # 记住用户名
#             if jizhu != 0:
#                 red.set_cookie('uname', uname)
#             else:
#                 red.set_cookie('uname', '', max_age=-1)
#             request.session['user_id'] = users[0].id
#             request.session['user_name'] = uname
#             return red
#         else:
#             context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
#             return render(request, 'df_user/login.html', context)
#     else:
#         context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
#         return render(request, 'df_user/login.html', context)
