from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request, "There was an issue logging in, try again.")
            return redirect("login_user")
    else:
        return render(request, "accounts/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("/")


def register_user(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"],
                email=request.POST["email"]
            )
            login(request, user)
            return redirect("/")
        except ValueError:
            messages.success(request, "There was an issue creating an account, try again.")
            return redirect("register_user")

    return render(request, "accounts/register.html", {})
