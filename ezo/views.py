from django.shortcuts import render


def ezo_home(request):
    return render(request, 'ezo/ezoHome.html')
