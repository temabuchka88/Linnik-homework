from django.contrib.auth.models import User
from django.db import models
from dishes.models import Shefs


def user_is_shef(self):
    return hasattr(self, "shefs")


User.add_to_class("is_shef", user_is_shef)
