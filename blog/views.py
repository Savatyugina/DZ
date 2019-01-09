from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import ServiceForm


def service_list(request):
    me = User.objects.get(username='kebablyulya')
    services = Service.objects.filter(author=me)
    return render(request, 'blog/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'blog/service_detail.html', {'service': service})


def service_new(request):
    if request.method == "SERVICE":
        form = ServiceForm(request.SERVICE)
        if form.is_valid():
            service = form.save(commit=False)
            service.author = request.user
            service.published_date = timezone.now()
            service.save()
            return redirect('service_detail', pk=service.pk)
        else:
            form = ServiceForm()
        return render(request, 'blog/service_edit.html', {'form': form})


def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.author = request.user
            service.published_date = timezone.now()
            service.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'blog/service_edit.html', {'form': form})

# Create your views here.

