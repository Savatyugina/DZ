from django.shortcuts import render
from .models import Service
from django.utils import timezone
from django.contrib.auth.models import User


def service_list(request):
    me = User.objects.get(username='kebablyulya')
    services = Service.objects.filter(author=me)
    return render(request, 'blog/service_list.html', {'services': services})

# Create your views here.

