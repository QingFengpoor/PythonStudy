#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   search2.py
@Time    :   2020/06/29 10:14:38
@Author  :   Qingfeng 
@Version :   1.0
@Contact :   2267647906@qq.com
'''

from django.shortcuts import render
# from django.views.decorators import csrf

def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
