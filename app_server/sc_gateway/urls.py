from django.conf.urls import url
import views
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.gateway_detail),
    url(r'^', views.gateway_list),

]

