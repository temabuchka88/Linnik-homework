from django.contrib.auth.models import User
from django.db import models
from dishes.models import Shefs


class MyUser(User):
    avatar = models.ImageField(upload_to="static/images/users/", blank=True)
    is_shef = models.BooleanField(default=False)
    shef = models.OneToOneField(Shefs, blank=True, null=True, on_delete=models.CASCADE)
