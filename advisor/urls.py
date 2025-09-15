from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),  # <-- this loads main.html first
    path('home/', views.index, name='index'),  # <-- your original index.html view
    path('plant-advisor/', views.plant_advisor, name='plant_advisor'),
    path('know-about-plants/', views.know_about_plants, name='know_about_plants'),
    path('plant-mart/', views.plant_mart, name='plant_mart'),
    path('nearby-stores/', views.nearby_stores, name='nearby_stores'),
]
