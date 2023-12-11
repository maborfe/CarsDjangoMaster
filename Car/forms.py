from django import forms
from .models import *

# class FormCar(forms.Form):

#    model =  forms.CharField(label= 'Modelo' ,max_length=80, required=True)
#    brand = forms.ModelChoiceField(Marca.objects.all(), label='Marca2222')
#    modelYear = forms.IntegerField(label='Ano do Modelo', required=False)
#    factoryYear = forms.IntegerField(label='Ano de Fábrica', required=False)
#    plate = forms.CharField(label='Placa', max_length = 10)
#    price = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2)
#    photo = forms.ImageField(label='Foto(s)', required=False)
         

#    def save(self):
#       car = Car(
#          model = self.cleaned_data['model'],
#          brand = self.cleaned_data['brand'],
#          modelYear = self.cleaned_data['modelYear'],
#          factoryYear = self.cleaned_data['factoryYear'],
#          plate = self.cleaned_data['plate'],
#          price = self.cleaned_data['price'],
#          photo = self.cleaned_data['photo'],
#       )
#       car.save()
#       return car
    
class CarModelForm(forms.ModelForm):
   class Meta:
      model = Car
      fields = '__all__'
      exclude = ['id']
      widgets = {
         'price': forms.NumberInput(attrs={'class': 'form-control'}),
         'photo': forms.FileInput(attrs={'class': 'form-control'}),
         'model': forms.TextInput(attrs={'class': 'form-control'}),
         'brand': forms.Select(attrs={'class': 'form-control'}),
         'factoryYear': forms.NumberInput(attrs={'class': 'form-control'}),
         'plate': forms.TextInput(attrs={'class': 'form-control'}),
         'modelYear': forms.NumberInput(attrs={'class': 'form-control'}),    
         'bio': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px; height: 300px'}),     
      }
      labels = {
         'model': 'Modelo',
         'brand': 'Marca',
         'factoryYear': 'Ano de Fábrica',
         'plate': 'Placa',
         'photo': 'Foto(s)',
         'price': 'Preço',
         'bio': 'Bio'
      }
      # error_messages = {
      #    'price': {
      #      'required': 'O preço é obrigatório',
      #    },
      # }
      # help_messages = {
      #    'model': {
      #      'required': 'O modelo é obrigatório',
      #    }
      # }

   # Quando eu defino uma função no meu forms.py para validar especificamente algum
   # campo do formulário, a função precisa OBRIGATORIAMENTE começar com clean_ 
   # para que o django entenda que essa função precisa ser executada quando o
   # backend receber os dados do form e cair na função form.is_valid()
   # o is_valid está diretamente ligad com essas funções começando com o clean_

   # def clean_factoryYear(self):
   #    factoryYear = self.cleaned_data['factoryYear']
   #    if factoryYear < 1970:
   #       raise forms.ValidationError('Ano de Fábrica deve ser maior que 1999')
   #    return factoryYear
      
