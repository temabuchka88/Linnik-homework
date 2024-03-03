from django.urls import path
from . import views

urlpatterns = [
    # path("", views.show_profile, name="show_profile"),
    # path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("login/", views.user_login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("my_profile/", views.show_my_profile, name="my_profile"),
    path("edit_profile/", views.edit_my_profile, name="edit_my_profile"),
    path("logout/", views.user_logout, name="logout"),
    path("create_dish/", views.create_dish, name="create_dish"),
]
