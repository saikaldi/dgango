from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm
# Create your views here.

def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid(): 
            User.objects.create(**form.cleaned_data)
            return redirect('/users/login/')
    else:
        return render(
            request, 
            'users/register.html', context={'form':form}
        )