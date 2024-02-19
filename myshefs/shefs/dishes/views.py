from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Shefs


def show_shefs(request, id):
    try:
        shef_info = get_object_or_404(Shefs, id=id)
    except Shefs.DoesNotExist:
        raise Http404("Shef does not exist")
    return render(request, "shef.html", {"shef_info": shef_info})
