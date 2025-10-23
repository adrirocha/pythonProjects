import pandas as pd
import datetime as dt
from random import randint
import smtplib

MY_USER="youremail@exampleemmail.com"
MY_PASSWORD="randomapppasword"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

df_birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in df_birthdays.iterrows()}

try:
    birthday_person = birthdays_dict[today_tuple]
except KeyError:
    print("There is no one having birthday today in your list.")
else:
    with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter_file:
        letter_to_send = letter_file.read()
        letter_to_send = letter_to_send.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_USER, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_USER, 
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Birthday Letter\n\n{letter_to_send}")
