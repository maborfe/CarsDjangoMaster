from django.db import models


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length = 80)
    
    def __str__(self):
        return self.brand
    

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length = 80)
    brand = models.ForeignKey("Marca", on_delete=models.PROTECT, related_name="brand_car")
    modelYear = models.IntegerField(blank=True, null=True)
    factoryYear = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank = True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.model
    
    
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    totalValue = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f'{self.quantity} - {self.totalValue}'


    