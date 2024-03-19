from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegisterUser, LoginUser, UserProfileForm, CreateDish, MyUser, User, EditDish
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dishes.models import Shefs, Cuisines, Dishes
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
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user.myuser)
        if form.is_valid():
            form.save()
            return redirect("/account/profile/")
    else:
        form = UserProfileForm(instance=user.myuser)

    return render(request, "edit_my_profile.html", {"form": form})


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
        # request.user.myuser.cuisines.set(selected_cuisines)
        if not request.user.myuser.is_shef:
            shef = Shefs.objects.create(
                name=request.user.myuser.username,
                photo = request.user.myuser.avatar,
            )
            for cuisine_id in selected_cuisines:
                cuisine = Cuisines.objects.get(id=cuisine_id)
                shef.cuisines_country.add(cuisine)
            shef.save()
            request.user.myuser.is_shef = True
            request.user.myuser.shef = shef
            request.user.myuser.save()
        return render(request, "shef_create_info.html")
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
        return redirect("/account/profile/")
    return render(request, "shef_supply_info.html")

# @login_required
# def shef_profile(request):
#     if request.method == 'POST':
#         pass
#     else:
#         return render(request, 'shef_profile.html',)
@login_required
def create_dish(request):
    if request.method == "POST":
        form = CreateDish(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            shef = Shefs.objects.get(name=request.user.myuser.username)
            dish.chef = shef
            dish.save()
            return redirect("/")
    else:
        form = CreateDish()
    return render(request, "create_dish.html", {"form": form})

@login_required
def all_food_items(request):
    if request.method == "POST":
        dish_id = request.POST.get("dish_id")
        dish = get_object_or_404(Dishes, id=dish_id)
        dish.delete()
        return redirect("all_food_items")
    else:
        shef = Shefs.objects.get(name=request.user.myuser.username)
        dishes = shef.dishes.all()
        return render(request, "all_food_items.html", {"shef": shef, "dishes": dishes})
    
@login_required
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dishes, id=dish_id)
    if request.method == "POST":
        form = EditDish(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect("all_food_items")
    else:
        form = EditDish(instance=dish)
    return render(request, "edit_dish.html", {"form": form, "dish": dish})

# @login_required
# def edit_shef_profile(request):
#     if request.method == "POST":
#         pass
#     else:
#         return render(request,)