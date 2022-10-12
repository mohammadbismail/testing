from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')

def regist_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=first_name, last_name=last_name, email=email, password=pw_hash)
        request.session['id'] = user.id
        return redirect('/trees/')


def login_user(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/trees/')
    messages.error(request, "Wrong email or password!")
    return redirect('/login')


def logout(request):
    del request.session['id']
    return redirect('/')
