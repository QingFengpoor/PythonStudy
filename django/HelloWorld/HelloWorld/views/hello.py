from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context = {}
    context['hello'] = 'Hello World ! '
    context['name'] = 'RUNOOB'
    context['person'] = {"name":"MY", "sex":"female", "age":"21"}
    context['runoob'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, 'runoob.html', context)