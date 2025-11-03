import requests
from twilio.rest import Client
import os

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

MY_LAT = 35.159635
MY_LONG = 129.004471

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(API_ENDPOINT, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for forecast in weather_data["list"]:
    condition_code = forecast["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☂️",
    from_="NUMBER_X",
    to="+MY_NUMBER",
    )

    print(message.status)




