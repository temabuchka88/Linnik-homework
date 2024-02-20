from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Shefs


def show_shef_and_dishes(request, shef_id):
    shef = get_object_or_404(Shefs, id=shef_id)
    dishes = shef.dishes.all()
    return render(request, "shef_and_dishes.html", {"shef": shef, "dishes": dishes})


def show_all_shef(request):
    shefs = Shefs.objects.all()
    return render(request, "shefs.html", {"shefs": shefs})
