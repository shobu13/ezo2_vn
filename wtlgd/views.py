from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def wtlgd_home(request):
    return HttpResponse("<center><h1>i'm a teapot</h1></center>")
