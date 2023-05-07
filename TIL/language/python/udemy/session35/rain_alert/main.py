import requests, json

lat = 37.566536 
lon = 126.977966


url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

# response = requests.get(url)
# print(response.status_code)
# data = response.json()
# print(data)

EndPoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat" : 37.566536,
    "lon" : 126.977966,
    "appid" : api_key
}

response = requests.get(EndPoint, params=weather_params)
print(response.status_code)
data = response.json()
print(data)
formateed_data = json.dumps(data, indent=4)
print()
print(formateed_data)