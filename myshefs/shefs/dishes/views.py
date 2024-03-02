from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Shefs, Cuisines


def show_shef_and_dishes(request, shef_id):
    shef = get_object_or_404(Shefs, id=shef_id)
    dishes = shef.dishes.all()
    return render(request, "shef_and_dishes.html", {"shef": shef, "dishes": dishes})


def show_all_shef(request):
    shefs = Shefs.objects.all()
    return render(request, "shefs.html", {"shefs": shefs})


# def tmp(request):
#     FOOD_CHOICES = (
#         ("Белорусская кухня", "Белорусская кухня"),
#         ("Русская кухня", "Русская кухня"),
#         ("Американская кухня", "Американская кухня"),
#         ("Азиатская кухня", "Азиатская кухня"),
#         ("Армянская кухня", "Армянская кухня"),
#         ("Греческая кухня", "Греческая кухня"),
#         ("Грузинская кухня", "Грузинская кухня"),
#         ("Европейская кухня", "Европейская кухня"),
#         ("Индийская кухня", "Индийская кухня"),
#         ("Итальянская кухня", "Итальянская кухня"),
#         ("Кавказская кухня", "Кавказская кухня"),
#         ("Мексиканская кухня", "Мексиканская кухня"),
#         ("Немецкая кухня", "Немецкая кухня"),
#         ("Турецкая кухня", "Турецкая кухня"),
#         ("Тайская кухня", "Тайская кухня"),
#         ("Средиземноморская кухня", "Средиземноморская кухня"),
#         ("Узбекская кухня", "Узбекская кухня"),
#         ("Украинская кухня", "Украинская кухня"),
#         ("Французская кухня", "Французская кухня"),
#         ("Японская кухня", "Японская кухня"),
#     )
#     for a in FOOD_CHOICES:
#         cuisine = Cuisines(cuisine_of_country=a[0])
#         cuisine.save()
#     return HttpResponse("created")
