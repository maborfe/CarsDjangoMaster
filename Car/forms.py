from django import forms
from .models import *

class FormCar(forms.Form):

   model =  forms.CharField(label= 'Modelo' ,max_length=80, required=True)
   brand = forms.ModelChoiceField(Marca.objects.all(), label='Marca2222')
   modelYear = forms.IntegerField(label='Ano do Modelo', required=False)
   factoryYear = forms.IntegerField(label='Ano de Fábrica', required=False)
   plate = forms.CharField(label='Placa', max_length = 10)
   price = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2)
   photo = forms.ImageField(label='Foto(s)', required=False)
   
   def save(self):
      car = Car(
         model = self.cleaned_data['model'],
         brand = self.cleaned_data['brand'],
         modelYear = self.cleaned_data['modelYear'],
         factoryYear = self.cleaned_data['factoryYear'],
         plate = self.cleaned_data['plate'],
         price = self.cleaned_data['price'],
         photo = self.cleaned_data['photo'],
      )
      car.save()
      return car