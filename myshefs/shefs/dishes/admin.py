from django.contrib import admin
from .models import Dishes, Cuisines, Shefs

# Register your models here.
admin.site.register(Dishes)
admin.site.register(Cuisines)
admin.site.register(Shefs)
