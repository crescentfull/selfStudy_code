import os, requests, json

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("SHEET_ENDPOINT")

exercise_text = input("Tell me which exercises u did: ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    # "Content-Type" : "json"
}

exercise_params = {
    "query" : exercise_text,
    "gender" : "male",
    "weight_kg" : 72.5,
    "height_cm" : 167.64,
    "age" : 30
}

response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
result = response.json()

###
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["dureation_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    
    print(sheet_response.text)