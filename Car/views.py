from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.forms import forms
from .forms import *
from django.views.generic import ListView, CreateView, DetailView, DeleteView

# def car_list(request):

#     cars = Car.objects.all().order_by('-id')

#     search = request.GET.get('search')

#     if search: 
#         cars = Car.objects.filter(model__icontains=search)

#     context ={'cars': cars}

#     return render(request,
#                   template_name='car_list.html',
#                   context= context
#     )


# Abaixo temos uma class que herda da classe base de Views do django, e este é um jeito de 
# escrever uma class based view para fazer o tratamento de views e retorno de template para o usuario dentro 
# do django, é uma forma mais "pronta" por já possuir algumas funcoes e facilidades embutidas nas suas 
# classes base. bastando apenas implementar as mesmas.

# class CarListView(View):

#     def get(self, request):
#         cars = Car.objects.all().order_by('-id')

#         search = request.GET.get('search')

#         if search: 
#             cars = Car.objects.filter(model__icontains=search)

#         context ={'cars': cars}

#         return render(request,
#                     template_name='car_list.html',
#                     context= context
#         )

class CarListViewGeneric(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

    # Sobrescrevendo o método queryset para que possa ser utilizado na busca de carros
    def get_queryset(self):
        cars =  super().get_queryset().order_by('-id')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
    

# def new_car(request):
    
#     if request.method == "POST":
#         new_car = CarModelForm(request.POST, request.FILES)
        
#         if new_car.is_valid():
#             new_car.save()
#             return redirect('car_list')
#     else:
#         new_car = CarModelForm()

#     return render(request, 'new_car.html', context={'form': new_car})

# class NewCarView(View):
    
#     def get(self,request):
#         new_car = CarModelForm()
#         return render(request, 'new_car.html', context={'form': new_car})
    
#     def post(self,request):
#         new_car = CarModelForm(self.request.POST, self.request.FILES)
        
#         if new_car.is_valid():
#             new_car.save()
#             return redirect('car_list')   
             
#         return render(request, 'new_car.html', context={'form': new_car})
    

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = '/cars/car_list/'

class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarDeleteView(DeleteView):
    pass
    