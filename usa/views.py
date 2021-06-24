from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html',{'name':'sss'})


def addit(request):
    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    res = a + b

    return render(request,'result.html',{'name':res})