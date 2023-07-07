from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request) :
    return render(request, 'generator/home.html')

def password(request) :

    length = int(request.GET.get('length', 10))
    charecters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase') :
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers') :
        charecters.extend(list('0123456789'))
    if request.GET.get('special') :
        charecters.extend(list('!@#$%^&*()_'))

    thepassword = ''

    for i in range(length) :
        thepassword += random.choice(charecters)

    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request) :
    return render(request, 'generator/about.html')