import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

my_email = "songyeongrok11@gmail.com"
password = os.environ.get("PRIVATE_KEY")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="syr972@naver.com",
                    msg="Subject:smtp TEST\n\nTESTESTESTETST")
    