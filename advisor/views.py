import os
import joblib
import numpy as np
from django.shortcuts import render
from django.conf import settings
import requests
from .models import PlantProduct
def main_page(request):
    return render(request, 'advisor/main.html')  # This shows your hero section

def index(request):
    return render(request, 'advisor/index.html')

# Dictionary mapping each plant to its image in your static folder
plant_images = {
    'Areca Palm': 'advisor/images/areca_palm.jpg',
    'Bamboo Palm': 'advisor/images/bamboo_palm.jpg',
    'Snake Plant': 'advisor/images/snake_plant.jpg',
    'Spider Plant': 'advisor/images/spider_plant.jpg',
}

# Load your model once at server start
MODEL_PATH = os.path.join(settings.BASE_DIR, 'plant_recommendation_model.pkl')
model = joblib.load(MODEL_PATH)

def plant_advisor(request):
    predicted_plant = None
    recommended_image = None

    if request.method == 'POST':
        try:
            co = float(request.POST.get('CO', 0))
            no2 = float(request.POST.get('NO2', 0))
            so2 = float(request.POST.get('SO2', 0))
            pm25 = float(request.POST.get('PM2.5', 0))
            pm10 = float(request.POST.get('PM10', 0))

            features = np.array([co, no2, so2, pm25, pm10]).reshape(1, -1)
            predicted_plant = model.predict(features)[0]

            # Get the corresponding image path for the predicted plant
            recommended_image = plant_images.get(predicted_plant)

        except ValueError:
            predicted_plant = "Invalid input. Please enter numeric values only."

    # Pass both the plant name and image path to the template
    context = {
        'predicted_plant': predicted_plant,
        'recommended_image': recommended_image,
    }
    return render(request, 'advisor/plant_advisor.html', context)

def know_about_plants(request):
    # Render the Know About Plants page
    return render(request, 'advisor/know_about_plants.html')

def plant_mart(request):
    products = PlantProduct.objects.all()
    return render(request, 'plant_mart.html', {'products': products})

def nearby_stores(request):
    stores = []
    if request.method == "POST":
        location = request.POST.get("location")
        query = f"plant nursery near {location}"
        url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&limit=5"
        response = requests.get(url)
        stores = response.json()
    return render(request, 'nearby_stores.html', {'stores': stores})