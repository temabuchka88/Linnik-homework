from django.db import models
from django.utils.text import slugify


class Cuisines(models.Model):
    FOOD_CHOICES = (
        ("Белорусская кухня", "Белорусская кухня"),
        ("Русская кухня", "Русская кухня"),
        ("Американская кухня", "Американская кухня"),
        ("Азиатская кухня", "Азиатская кухня"),
        ("Армянская кухня", "Армянская кухня"),
        ("Греческая кухня", "Греческая кухня"),
        ("Грузинская кухня", "Грузинская кухня"),
        ("Европейская кухня", "Европейская кухня"),
        ("Индийская кухня", "Индийская кухня"),
        ("Итальянская кухня", "Итальянская кухня"),
        ("Кавказская кухня", "Кавказская кухня"),
        ("Мексиканская кухня", "Мексиканская кухня"),
        ("Немецкая кухня", "Немецкая кухня"),
        ("Турецкая кухня", "Турецкая кухня"),
        ("Тайская кухня", "Тайская кухня"),
        ("Средиземноморская кухня", "Средиземноморская кухня"),
        ("Узбекская кухня", "Узбекская кухня"),
        ("Украинская кухня", "Украинская кухня"),
        ("Французская кухня", "Французская кухня"),
        ("Японская кухня", "Японская кухня"),
    )
    cuisine_of_country = models.CharField(max_length=35, choices=FOOD_CHOICES)

    def __str__(self):
        return self.cuisine_of_country


class Shefs(models.Model):
    name = models.CharField(max_length=30)
    about_me = models.CharField(max_length=700)
    cuisines_country = models.ManyToManyField(Cuisines)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_description = models.TextField()
    chef = models.ForeignKey(Shefs, on_delete=models.CASCADE, related_name="dishes")
    dish_prise = models.IntegerField()
    dish_weight = models.IntegerField()

    def __str__(self):
        return self.dish_name
