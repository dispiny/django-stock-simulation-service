# from django.http import HttpResponse
from time import gmtime, strftime
from django.shortcuts import render

def index(request):
    msg = 'test1212'
    return render(request, 'live/index.html', {'message': msg})

def dashboard(request):
    nowTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return render(request, 'dashboard/index.html',  {"time": nowTime})
