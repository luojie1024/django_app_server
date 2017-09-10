from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_is_exist/$', views.register_is_exist),
    url(r'^(?P<pk>[0-9]+)/$', views.login_handle),
    url(r'^login/(?P<pk>[0-9]+)/$', views.login_old),
    url(r'^', views.login),
    url(r'^snippets/$', views.snippet_list),
]

