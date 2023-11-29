from django.db import models


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length = 80)
    
# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length = 80)
    brand = models.ForeignKey("Marca", on_delete=models.PROTECT, related_name="brand_car")
    modelYear = models.IntegerField(blank=True, null=True)
    factoryYear = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank = True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    
    