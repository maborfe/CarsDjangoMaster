from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ("model",)

admin.site.register(Car, CarAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ("brand",)

admin.site.register(Marca, MarcaAdmin)