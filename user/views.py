from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def register_user(request):
    if request.method =="POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,("you have registered..."))
                return redirect("dashbord")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            form=SingUpForm()
            return render(request, "register.html",{
                'form' : form
            })
    else:
        form=SingUpForm()
        return render(request, "register.html",{
            'form' : form
        })





def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You are now logged in")
            return redirect("home")
        else:
            messages.success(request, "Please try again")
            return redirect('login')
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('login')

def dashbord(request):
    if request.method == "POST":
        u_update = UserUpdateForm(request.POST,instance=request.user)
        if u_update.is_valid():
            u_update.save()
            return redirect('home')

    else:
        u_update = UserUpdateForm() 
        return render(request, "dashbord.html", {
            'u_update' : u_update
        })


