from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.forms import forms
from .forms import *

def car_list(request):

    cars = Car.objects.all().order_by('-id')

    search = request.GET.get('search')

    if search: 
        cars = Car.objects.filter(model__icontains=search)

    context ={'cars': cars}

    return render(request,
                  template_name='car_list.html',
                  context= context
    )

def new_car(request):
    
    if request.method == "POST":
        # new_car = FormCar(request.POST, request.FILES)
        # if new_car.is_valid():
        #     new_car.save()
        #     return redirect('car_list')

        new_car = CarModelForm(request.POST, request.FILES)
        
        if new_car.is_valid():
            new_car.save()
            return redirect('car_list')
    else:
        new_car = CarModelForm()

    return render(request, 'new_car.html', context={'form': new_car})