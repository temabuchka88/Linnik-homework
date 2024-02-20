from django.urls import path
from . import views

urlpatterns = [
    path(
        "shef/<int:shef_id>/", views.show_shef_and_dishes, name="show_shef_and_dishes"
    ),
    path("shef/", views.show_all_shef, name="show_all_shef"),
    path("", views.show_all_shef, name="show_all_shef"),
]
