from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.service_list, name='service_list'),
    url(r'^service/(?P<pk>\d+)/$', views.service_detail, name='service_detail'),
]