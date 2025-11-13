import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._endpoint = "https://test.api.amadeus.com/v1"
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self._headers = {
            "Authorization" : f"Bearer {self._token}"
        }
        self._flight_data = FlightData
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=f"{self._endpoint}/security/oauth2/token", headers=header, data=body)
        response.raise_for_status()
        
        return response.json()["access_token"]
    
    def get_iataCodes(self, city_names):
        iataCodes = []
        for city_name in city_names:
            params = {
                "keyword" : city_name,
                "max" : 1
            }

            response = requests.get(url=f"{self._endpoint}/reference-data/locations/cities", params=params, headers=self._headers)
            response.raise_for_status()
            
            iataCode = response.json()["data"][0]["iataCode"]
            iataCodes.append(iataCode)
        return iataCodes
    def _format_flight_data(self, flight):
        cheapestPrice = float(flight["price"]["total"])
        cheapestOrigin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        cheapestDestination_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        cheapestOut_date = flight["lastTicketingDate"]
        
        flight_data = self._flight_data(price=cheapestPrice, 
                                        origin_airport=cheapestOrigin_airport, 
                                        destination_airport=cheapestDestination_airport,
                                        out_date=cheapestOut_date
                                        )
        return flight_data
    
    def get_cheap_flights(self, iataCodes):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
        from_time = tomorrow.strftime("%Y-%m-%d")
        to_time = six_month_from_today.strftime("%Y-%m-%d")
        cheapestFlights = []
        for iataCode in iataCodes:
            print("Getting...")
            params = {
                "originLocationCode" : "LON",
                "destinationLocationCode" : iataCode,
                "departureDate" : from_time,
                "returnDate" : to_time,
                "adults" : 1,
                "nonStop" : "true",
                "currencyCode" : "GBP"
            }
            response = requests.get(f"https://test.api.amadeus.com/v2/shopping/flight-offers", params=params, headers=self._headers)
            response.raise_for_status()

            cheapestPrice = 0
            cheapestFlight = None
            try:
                flights = response.json()["data"]
            except KeyError:
                cheapestFlight = self._flight_data()
            else:
                for flight in flights:
                    if cheapestPrice == 0:
                        cheapestPrice = float(flight["price"]["total"])
                        cheapestFlight = self._format_flight_data(flight)
                    elif float(flight["price"]["total"]) < cheapestPrice:
                        cheapestPrice = float(flight["price"]["total"])
                        cheapestFlight = self._format_flight_data(flight)
            
            cheapestFlights.append(cheapestFlight)
            
        return cheapestFlights




