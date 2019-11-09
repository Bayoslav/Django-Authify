from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegForm
# Create your views here.


class Dashboard(View):
    def get(self, request):
        if(request.user.is_authenticated):
            name = request.user
            return render(request, 'dashboard.html', {'username': name})

        return render(request, 'login.html', {'form': LoginForm()})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/login')


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            name = (request.user)
            return render(request, 'dashboard.html', {'username': name})
        form = RegForm(request.POST)
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegForm(request.POST)
        error = 0
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('/')
        else:
            error = 1
            form = RegFOrm()

        return render(request, 'register.html', {'form': form, 'error': error})


class LogIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            name = (request.user)
            return render(request, 'dashboard.html', {'username': name})
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            try:
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'dashboard.html', {'username': request.user})
            except:
                return render(request, 'login.html', {'form': form, 'error': "Invalid Username & Password!"})

        return render(request, 'login.html', {'form': form, 'error': "Invalid Username & Password!"})
