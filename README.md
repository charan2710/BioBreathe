🌿 BioBreathe — AI Powered Plant Recommender for Air Purification

BioBreathe is a machine learning–based web application that recommends air-purifying plants based on air quality parameters. The goal of the project is to promote sustainable and low-cost solutions for improving air quality using natural methods.

The system analyzes pollution inputs and suggests suitable plants that can help reduce specific pollutants, making environmental improvement simple and accessible.

🚀 Features

• AI-based plant recommendation
• User-friendly web interface
• Educational plant information
• Scalable architecture for future real-time data integration
• Supports sustainability and green living

🛠 Tech Stack

Backend: Django (Python)
Machine Learning: Scikit-learn, Pandas, NumPy
Frontend: HTML, CSS, JavaScript
Model: Trained plant recommendation model (.pkl)
Database: SQLite

📂 Project Structure
BioBreathe/
│
├── plant_recommendation_model.pkl   # Trained ML model
├── templates/                       # HTML templates
├── static/                          # CSS, JS, images
├── app/                             # Django app files
├── manage.py                        # Django entry point
└── requirements.txt                 # Dependencies

⚙️ Installation & Setup Guide

Follow these steps to run the project on your system.

1️⃣ Clone the Repository
git clone https://github.com/yourusername/biobreathe.git
cd biobreathe
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
Apply migrations (if needed)
python manage.py migrate

Start the server
python manage.py runserver

Now open your browser and go to:
http://127.0.0.1:8000/
