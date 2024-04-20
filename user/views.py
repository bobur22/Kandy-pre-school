from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib import messages

def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login-p')
    return render(request, "user/registration.html", {'form': form})


def login_view(request):
    error_m = None
    form_l = LoginForm()
    if request.method == "POST":
        form_l = LoginForm(request.POST)
        if form_l.is_valid():
            user = authenticate(username=form_l.cleaned_data['username'], password=form_l.cleaned_data['password'])
            if user is not None:
                error_m = "login"
                print(error_m)
                login(request, user)
                return redirect('home-p')
            else:
                error_m = "error"
                print(error_m)
                form_l.add_error('password', 'Username yoki parol noto\'g\'ri')

    return render(request, "user/login.html", {'form_l':form_l, 'error_m':error_m})


def logout_view(request):
    logout(request)
    return redirect('login-p')

def check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        # return HttpResponse("<p style='color:green'>This username already exists</p>")
        return HttpResponse("<div class='alert alert-success alert-dismissible fade show message_l' role='alert'>This username already exists.<button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button></div>")

    else:
        # return HttpResponse("<p style='color:red'>This username not found</p> ")
        return HttpResponse("<div class='alert alert-warning alert-dismissible fade show message_l' role='alert'>This username not found.<button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button></div>")

