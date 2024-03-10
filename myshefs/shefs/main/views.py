from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegisterUser, LoginUser, UserProfileForm, CreateDish, MyUser, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dishes.models import Shefs, Cuisines
from django.contrib import messages
from .models import MyUser


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
    print(dir(user))
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user.myuser)
        if form.is_valid():
            form.save()
            return redirect("/my_profile/")
    else:
        form = UserProfileForm(instance=user.myuser)

    return render(request, "edit_my_profile.html", {"form": form})


@login_required
def create_dish(request):
    if request.method == "POST":
        form = CreateDish(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateDish()
    return render(request, "create_dish.html", {"form": form})


@login_required
def select_cuisines(request):
    popular_cuisines = Cuisines.objects.filter(
        cuisine_of_country__in=[
            "Европейская кухня",
            "Русская кухня",
            "Белорусская кухня",
            "Американская кухня",
            "Итальянская кухня",
            "Французская кухня",
            "Грузинская кухня",
            "Украинская кухня",
            "Азиатская кухня",
        ]
    )
    other_cuisines = Cuisines.objects.exclude(
        cuisine_of_country__in=[
            "Европейская кухня",
            "Русская кухня",
            "Белорусская кухня",
            "Американская кухня",
            "Итальянская кухня",
            "Французская кухня",
            "Грузинская кухня",
            "Украинская кухня",
            "Азиатская кухня",
        ]
    )
    if request.method == "POST":
        selected_cuisines = request.POST.getlist("cuisine")
        request.user.myuser.cuisines.set(selected_cuisines)
        return redirect("/")  # Замените 'profile' на ваш URL для профиля шефа
    return render(
        request,
        "start_shef_cuisines.html",
        {"popular_cuisines": popular_cuisines, "other_cuisines": other_cuisines},
    )


@login_required
def shef_create_info(request):
    return render(request, "shef_create_info.html")


@login_required
def shef_supply_info(request):
    if request.method == "POST":
        user = request.user.myuser
        if not user.is_shef:
            shef = Shefs.objects.create(name=user.username)
            user.is_shef = True
            user.shef = shef
            user.save()
        return redirect("/my_profile/")
    return render(request, "shef_supply_info.html")


# @login_required
# def confirm_star_shef(request):
#     if request.method == "POST":
#         user = request.user.myuser
#         if not user.is_shef:
#             shef = Shefs.objects.create(name=user.username)
#             user.is_shef = True
#             user = shef
#             user.save()
