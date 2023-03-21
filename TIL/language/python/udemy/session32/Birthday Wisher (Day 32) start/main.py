import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

import datetime as dt
import pandas, random

# data = pandas.read_csv("quotes.txt")
# print(data)
# data_list = data.values.tolist()
# print(data_list)
# print()
# print(random.randint(0, len(data_list)-1))

# pick = data_list[random.randint(0, len(data_list)-1)]
# print(pick)
# pick_msg = str(pick)
# print(pick_msg)
# print(type(pick_msg))



now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_qutoes = quote_file.readlines()
        quote = random.choice(all_qutoes)
    
    print(quote)
    
    # send email
    my_email = "songyeongrok11@gmail.com"
    password = os.environ.get("PRIVATE_KEY")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="syr972@naver.com",
                            msg="Subject:Today's quote\n\n"+quote)