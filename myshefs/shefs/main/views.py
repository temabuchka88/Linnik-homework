from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegisterUser, LoginUser, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dishes.models import Shefs, Cuisines
from django.contrib import messages


def registration(request):
    if request.method == "POST":
        user = RegisterUser(request.POST)
        if user.is_valid():
            new_user = user.save(commit=False)
            new_user.set_password(user.cleaned_data["password"])
            new_user.save()
            messages.success(
                request, "Вы успешно зарегистрированы. Теперь вы можете войти."
            )
            return redirect("login")
    else:
        user = RegisterUser()
        return render(request, "registration.html", {"user": user})


def user_login(request):
    log = LoginUser()
    if request.method == "POST":
        log = LoginUser(data=request.POST)
        if log.is_valid():
            user = authenticate(
                request,
                username=log.cleaned_data.get("username"),
                password=log.cleaned_data.get("password"),
            )
            if user is not None:
                login(request, user)
                return redirect("/order/")
    return render(request, "login.html", {"login": log})


def user_logout(request):
    logout(request)
    return redirect("/order/")


@login_required
def show_my_profile(request):
    user = request.user
    return render(request, "my_profile.html", {"user": user})


@login_required
def edit_my_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("/my_profile/")
    else:
        form = UserProfileForm(instance=user)
    return render(request, "edit_my_profile.html", {"form": form})
