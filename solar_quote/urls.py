from django.urls import path
from . import views

app_name = 'solar_quote'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/calculate/', views.calculate_quote, name='calculate'),
]
