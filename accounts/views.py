from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from accounts.util import login_required
from config import settings


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('list')
        return render(request, 'accounts/register.html', {'form': form})
    form = RegisterForm(request.POST)
    return render(request, 'accounts/register.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(email=data.get('email'), password=data.get('password'))
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(error='Invalid username or password', field=None)
            return render(request, 'accounts/login.html', {'form': form})

    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_(request):
    logout(request)
    return redirect('accounts:login')


def google_login(request):
    url= settings.GOOGLE_LOGIN_URL
    client_id=settings.GOOGLE_CLIENT_ID
    client_secret=settings.GOOGLE_CLIENT_SECRET
    return url
