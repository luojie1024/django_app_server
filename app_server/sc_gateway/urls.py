from django.conf.urls import url
import views

urlpatterns = [
    url(r'^gateway_list/$', views.gateway_list),
    url(r'^gateway_detail/(?P<pk>[0-9]+)/$', views.gateway_detail),
]
