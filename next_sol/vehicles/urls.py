from django.urls import path
from .views import index, register_vehicle, list_vehicles

urlpatterns = [
    path('', index),
    path('register-vehicle', register_vehicle),
    path('list-all', list_vehicles),
]
