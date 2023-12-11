from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, LoginForm
# Create your views here.

def register_view(request):
    if request.method == 'GET':
        context = {
            "form": RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == "POST":
        form = RegisterForm(request.POST) 
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data) 
            # User.objects.create(
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password'],
            #     password_repeat=form.cleaned_data['password_repeat'],
            #     email=form.cleaned_data['email'],
            #     first_name=form.cleaned_data['first_name'],
            #     last_name=form.cleaned_data['last_name'],
            # )
            return redirect('/users/login/')
        else:
            return render(
                request, 
                'users/register.html', context={'form' : form}
            )
        
def login_view(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm
        }
        return render(
            request=request,
            template_name='users/login.html',
            context=context
        )
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)  # None | User

            if user is not None:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error(
                    'username',
                    'Username or password is incorrect!'
                )

        return render(
            request=request,
            template_name='users/login.html',
            context={"form": form}
        )

def logout_view(request):
    logout(request)
    return redirect('/products/')

def profile_view(request):
    if request.method == 'GET':
        return render(
            request,
            'users/profile.html',
            {"user": request.user}
        )

