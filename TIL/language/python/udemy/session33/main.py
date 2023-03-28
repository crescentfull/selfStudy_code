import requests, json
from datetime import *



my_lat = 21.5666791
my_lng = -165.9782914

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if my_lat-5 <= iss_latitude <= my_lat+5 and my_lng-5 <= iss_longitude <= my_lng+5:
        return True
    
def is_night():
    parameters = {
                "lat" : my_lat,
                "lng" : my_lng,
                "formatted" : 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters )
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=4))
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = 13 #datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    

# send email
import os
import smtplib, time

from dotenv import load_dotenv

load_dotenv()

my_email = "songyeongrok11@gmail.com"
password = os.environ.get("PRIVATE_KEY")

# 같은 날짜일시에
while True:
    time.sleep(6)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="songyeongrok11@gmail.com",
                                msg=f"Subject:the sun is overhead\n\nhead up bro! look at the sky")
            print("***SEND EMAIL!***")
            break
