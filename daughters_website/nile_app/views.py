# nile_app/views.py

from django.shortcuts import render

def about(request):
    return render(request, 'nile_app/about.html')

def community(request):
    return render(request, 'nile-app/community.html')

def contact(request):
    return render(request, 'nile_app/contact.html')

def home(request):
    return render(request, 'nile_apphome.html')

def login(request):
    return render(request, 'nile_app/login.html')

def post(request):
    return render(request, 'nile_apppost.html')

def programs(request):
    return render(request, 'nile_app/programs.html')

def resources(request):
    return render(request, 'nile_app/resources.html')

def signup(request):
    return render(request, 'nile_app/signup.html')
