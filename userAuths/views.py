from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def sign_up(request):
    template = 'auth/sign-up.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Welcome Shine Library!")

            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]

            new_user = authenticate(username=username, password1=password1)

            login(request, new_user)
            return redirect('home')

    else:
        form = RegisterForm()


    context = {
        'form': form
    }
    return render(request, template, context)


def sign_in(request):
    template = 'auth/sign-in.html'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)  
            messages.success(request, 'Welcome back to Shine Library')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')

    context = {}
    return render(request, template, context)

def sign_out(request):
    logout(request)
    messages.success(request, 'You logged out')
    return redirect('sign_in')