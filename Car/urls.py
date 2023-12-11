from django.urls import path
from Car.views import *


urlpatterns = [
    path('car_list/', CarListViewGeneric.as_view(), name='car_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car_detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car_delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
    path('car_update/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
]
