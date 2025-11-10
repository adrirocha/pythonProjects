import requests
from twilio.rest import Client
import os

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

MY_NUMBER = os.environ.get("MY_NUMBER")
OTHER_NUMBER = os.environ.get("OTHER_NUMBER")


stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [data for (date, data) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    news_params = {
        "apiKey" :  NEWS_API_KEY,
        "q" : COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
            body=f"{STOCK}: {up_down} {diff_percent}%",
            from_=OTHER_NUMBER,
            to=MY_NUMBER
        )
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=OTHER_NUMBER,
            to=MY_NUMBER
        )


