from django.urls import path
from . import views

urlpatterns = [
    path("order/shef/<int:shef_id>/", views.show_shefs),
]
