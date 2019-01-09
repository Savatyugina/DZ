from django.shortcuts import render, get_object_or_404
from .models import Service
#from django.utils import timezone
from django.contrib.auth.models import User



def service_list(request):
    me = User.objects.get(username='kebablyulya')
    services = Service.objects.filter(author=me)
    return render(request, 'blog/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'blog/service_detail.html', {'service': service})

# Create your views here.

