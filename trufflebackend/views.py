from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Welcome to New django website aboutus")

def login(request):
    data={
        'title':'Login Page',
        'LoopData':['one','two','three']
    }
    return render(request,"login.html",data)

def changepassword(request):
    return HttpResponse("Welcome to New django website aboutus")

def dashboard(request):
    return render(request,"dashboard.html")

def users(request):
     return render(request,"users.html")

def profile(request):
    return HttpResponse("profile")

def userDetail(request,userid):
    return HttpResponse(userid)