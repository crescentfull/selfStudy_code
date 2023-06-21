# HTTP Requests
import requests
from datetime import datetime

USERNAME = "test1231888"
TOKEN = "jsifiidfn1in3in4ni5kkkdk"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : TOKEN,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# https://pixe.la/v1/users/test1231888/graphs/graph2.html

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# 헤더 넣어서 그래프 확인
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "9.74"  
}

# 자전거 사용기록 넘기기 확인
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)