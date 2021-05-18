from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .form import LoginForm
from django.http import HttpResponse

import requests

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])

            if user is not None:
                login(request,user)
                return HttpResponse('Authentication was successfull!')
            
            else:
                return HttpResponse('Authetication failed, please try again.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

def index(request):
    return render(request, 'app/index.html')


def home(request):
    response = requests.get('https://fakestoreapi.com/users').json()
    return render(request,'index.html', {'response':response})
