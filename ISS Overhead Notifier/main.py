import requests
from datetime import datetime
import smtplib
from time import sleep

MY_USER = "your email"
MY_PASSWORD = "your app password"

MY_LAT = 0 # Your latitude
MY_LONG = 0 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("the smtp email server") as connection:
            connection.starttls()
            connection.login(user=MY_USER, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_USER,
                                to_addrs="the email of the destination",
                                msg="Subject:ISS Notifier\n\nThe ISS is close! Look up!")
