from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import os
import json

def hello(request):
    return HttpResponse("Hello world ! ")

def my_view(request):
    static_html = 'index.html'
    return render(request, static_html)

def test1(request):
    if request.method == 'GET':
        print(request.GET.get('name'))
        print(request.GET.get('value'))

    return HttpResponse(json.dumps({"msg":"success"}))
