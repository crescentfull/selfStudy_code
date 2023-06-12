# HTTP Requests
import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "jsifiidfn1in3in4ni5kkkdk",
    "username" : "test1231888",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)