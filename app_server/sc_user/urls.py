from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register_handle),
    url(r'^register_is_exist/$', views.register_is_exist),
    # url(r'^login_handle/$', views.login_handle),
    url(r'^login/$', views.login),
    # url(r'^getUserList/$', views.getUserList),
    # url(r'^setUser/$', views.setUser),
    url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
