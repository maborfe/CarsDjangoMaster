from django.urls import path
from Car.views import *

urlpatterns = [
    path('car_list/', car_list, name='car_list'),
    path('new_car/', new_car, name='new_car'),

]
