


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import SignupForm, LoginForm

def home(request):
    return render(request, 'nile_app/home.html')

def about(request):
    return render(request, 'nile_app/about.html')

def programs(request):
    return render(request, 'nile_app/programs.html')

def resources(request):
    return render(request, 'nile_app/resources.html')

def community(request):
    return render(request, 'nile_app/community.html')

def contact(request):
    return render(request, 'nile_app/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'nile_app/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'nile_app/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')
