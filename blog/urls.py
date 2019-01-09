from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.service_list, name='service_list'),
    url(r'^service/(?P<pk>\d+)/$', views.service_detail, name='service_detail'),
    url(r'^service/new/$', views.service_new, name='service_new'),
    url(r'^service/(?P<pk>\d+)/edit/$', views.service_edit, name='service_edit'),
]