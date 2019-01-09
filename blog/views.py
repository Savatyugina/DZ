from django.shortcuts import render


def service_list(request):
    return render(request, 'blog/service_list.html', {})

# Create your views here.
