import os, requests, json

from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    # "Content-Type" : "json"
}

exercise_params = {
    "query" : "ran 2 kilo",
    "gender" : "male",
    "weight_kg" : 72.5,
    "height_cm" : 167.64,
    "age" : 30
}

response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
print(response.text)