from dotenv import load_dotenv
from twilio.rest import Client
import os
import requests, json

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_MOBILE_NUMBER = os.getenv("MY_MOBILE_NUMBER")
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
print("Status Code : ", response)

data = response.json()["Time Series (Daily)"]
new_data = json.dumps(data, indent=4)
print(new_data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_prcie = yesterday_data["4. close"]
print("어제 값 :", yesterday_closing_prcie)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print("그저께 값 :", day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_prcie) - float(day_before_yesterday_closing_price))
print("gap : ", difference)
up_down = None
if difference > 0: # 긍정적 신호. 상승
    up_down = "🔺"
else:
    up_down = "🔻"
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_prcie)) * 100)
print("percentage : ", diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then 관련기사 3개 출력
if abs(diff_percent) > 1.0:
    news_params ={
    "qInTitle" : COMPANY_NAME,
    "apikey" : NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)

    articles = news_response.json()["articles"]
    # new_newsData = json.dumps(news_data, indent=4)
    three_articles = articles[:3]
    print(json.dumps(three_articles, indent=4))
    
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\
                            \nHeadline: {article['title']}.\
                            \nBrief: {article['description']}" 
                        for article in three_articles]
    #TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_= "+13612739879",
            to   = MY_MOBILE_NUMBER
        )



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

