##################### Hard Starting Project ######################
import os
import pandas, random, smtplib

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

my_email = "songyeongrok11@gmail.com"
password = os.environ.get("PRIVATE_KEY")

# 날짜 pick
today = datetime.now()
today_tuple = (today.month, today.day)

# data 날짜 판별
data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }

# 같은 날짜일시에
if today_tuple in birthdays_dict:
    # 같은 날인 사람 data를 변수선언
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person)
    # letter_templates 3개중 하나기 선택되도록 설정 -> 변수 선언
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # 선택된 템플릿 파일내용에서 생일자에 대한 이름을 변경
    with open(file_path) as letter_file:
        contents = letter_file.read()
        print(contents)
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)
        # contents.replace()호출만해선서는 leter파일의 [NAME]이 변경되지 않는다. contents변수에 저장해줘야한다!
    # email send
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:HappyBirthday\n\n{contents}")