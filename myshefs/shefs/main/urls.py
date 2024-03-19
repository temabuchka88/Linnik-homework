from django.urls import path
from . import views

urlpatterns = [
    # path("", views.show_profile, name="show_profile"),
    # path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("login/", views.user_login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.show_my_profile, name="my_profile"),
    path("edit_profile/", views.edit_my_profile, name="edit_my_profile"),
    path("logout/", views.user_logout, name="logout"),
    path(
        "my_profile/start_shef/cuisine", views.select_cuisines, name="select_cuisines"
    ),
    path("my_profile/start_shef/order", views.shef_create_info, name="start_info"),
    path("my_profile/start_shef/supply", views.shef_supply_info, name="supply_info"),
    # path("profile/", views., name=""),
    path("food-items/all/", views.all_food_items, name="all_food_items"),
    path("food-items/create_dish/", views.create_dish, name="create_dish"),
    path("food-items/edit_dish/<int:dish_id>", views.edit_dish, name="edit_dish"),
    path("food-items/delete_dish/", views.all_food_items, name="delete_dish"),
]
