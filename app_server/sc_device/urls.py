from django.conf.urls import url
import views
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.device_detail),
    url(r'^', views.device_list),

]

