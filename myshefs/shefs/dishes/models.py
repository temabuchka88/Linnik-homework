from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Cuisines(models.Model):

    cuisine_of_country = models.CharField(max_length=35)

    def __str__(self):
        return self.cuisine_of_country


class Shefs(models.Model):
    photo = models.ImageField(upload_to="static/images/shefs/", blank=True)
    name = models.CharField(max_length=30)
    about_me = models.CharField(max_length=700, blank=True)
    cuisines_country = models.ManyToManyField(Cuisines)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_photo = models.ImageField(upload_to="static/images/dishes/")
    dish_description = models.TextField()
    chef = models.ForeignKey(Shefs, on_delete=models.CASCADE, related_name="dishes")
    dish_prise = models.IntegerField()
    dish_weight = models.IntegerField()

    def __str__(self):
        return self.dish_name
