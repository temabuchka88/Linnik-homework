from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from dishes.models import Shefs
from django import forms


class RegisterUser(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]


class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label="Photo", required=False)

    class Meta:
        model = User
        fields = ["avatar", "first_name", "last_name"]
