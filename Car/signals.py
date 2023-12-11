from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from httpx import get
from .models import *
from openai_api.client import get_bio_openai

def update_car_inventory():
    quantity = Car.objects.all().count()
    # Instrução abaixo, retorna um dict, portanto adicionamos o nome da chave que queremos que de fato seja
    # retornado para dentro do campo totalValue, sendo totVal o nome do campo que o agregate "cria" dentro do retorno
    # da nossa query retornada em formato de dict
    totalValue = Car.objects.aggregate(
        totVal = Sum('price')
    )['totVal']

    inventory = Inventory.objects.create(
        quantity = quantity,
        totalValue = totalValue
        )



@receiver(post_save, sender = Car)
def car_post_save(sender, instance, **kwargs):
    update_car_inventory()

@receiver(post_delete, sender = Car)
def car_post_delte(sender, instance, **kwargs):
    update_car_inventory()

@receiver(pre_save, sender = Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        bio = get_bio_openai(instance.model, instance.brand, instance.modelYear)
        instance.bio = bio

    update_car_inventory()