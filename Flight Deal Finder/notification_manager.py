from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self._account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self._auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self._phone_number = os.getenv("TWILIO_PHONE_NUMBER")
        self._my_phone_number = os.getenv("TWILIO_MY_PHONE_NUMBER")
    
    def send_message(self, flight):
        client = Client(self._account_sid, self._auth_token)

        message = client.messages.create(
            body=f"Low price alert!\n Only £{flight.price} to fly from {flight.origin_airport} to {flight.destination_airport}\non {flight.out_date}",
            from_=self._phone_number,
            to=self._my_phone_number
        )

        print(message.body)
