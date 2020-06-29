#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   search.py
@Time    :   2020/06/29 09:33:41
@Author  :   Qingfeng 
@Version :   1.0
@Contact :   2267647906@qq.com
'''

from django.http import HttpResponse
from django.shortcuts import render

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = "answer:" + request.GET['q']
    else:
        message = "form applied"
    return HttpResponse(message)
