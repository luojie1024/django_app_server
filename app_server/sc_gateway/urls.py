from django.conf.urls import url
import views

urlpatterns = [
    url(r'^create/$', views.create),
    url(r'^update/$', views.update),
    url(r'^delete/$', views.delete),
    url(r'^retrieve/$', views.retrieve),
]
