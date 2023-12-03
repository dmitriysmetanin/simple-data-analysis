from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginn
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as logoutt
from .models import *

# Create your views here.
def index(request):
    data = {}
    return render(request, 'index.html', context=data)

def register(request):
    return render(request, 'register.html') 


def login(request):
    if request.POST:
        username = request.POST.get("your_username")
        password = request.POST.get("your_password")
        user = authenticate(username=username, password=password)
        if user is not None:
            loginn(request, user)
            return HttpResponseRedirect('/')
        

        else:
            data = {
                "invalid_credentials_message": True
            }
            return render(request, 'login.html', context=data)

    return render(request, 'login.html')

def logout(request):
    logoutt(request)
    return HttpResponseRedirect('/')

# @login_required(login_url="/registration/login")
def contact(request):
    if request.POST:
        organization = request.POST["your_organization"]
        problem = request.POST["your_problem"]
        contact = request.POST["your_contact"]
        # print(request.POST)

        Feedback.objects.create(organization=organization,
                                problem=problem,
                                contact=contact)
        
        return HttpResponseRedirect('/')
        
    return render(request, 'contact.html')

def logout(request):
    logoutt(request)
    return HttpResponseRedirect('/')