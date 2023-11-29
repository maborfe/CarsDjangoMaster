from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def car_home(request):
    return render(request,
                  template_name='carHome.html',
                  )