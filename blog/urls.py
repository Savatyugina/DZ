from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.service_list, name='service_list'),
]