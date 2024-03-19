from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from dishes.models import Shefs, Dishes
from django import forms
from .models import MyUser


class RegisterUser(ModelForm):
    class Meta:
        model = MyUser
        fields = ["username", "password", "email"]


class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())


class UserProfileForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ["avatar", "first_name", "last_name"]


class CreateDish(ModelForm):
    class Meta:
        model = Dishes
        fields = ["dish_name", "dish_photo", "dish_description", "dish_prise", "dish_weight"]

class EditDish(ModelForm):
    class Meta:
        model = Dishes
        fields = ["dish_name", "dish_photo", "dish_description", "dish_prise", "dish_weight"]