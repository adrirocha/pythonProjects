from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_all_data()
if not(sheet_data[0]["iataCode"]):
    
    # Get the City Names
    city_names = []
    for city_data in sheet_data:
        city_names.append(city_data["city"])
    
    # Get The iataCodes for each city by passing the city names
    iataCodes = flight_search.get_iataCodes(city_names)
    # Update the memory data (sheet_data) with the iata Codes
    for city_data, iataCode in zip(sheet_data, iataCodes):
        city_data["iataCode"] = iataCode
    
    # Now using the memory data (sheet_data) update the cloud data
    for city_data in sheet_data:
        data_manager.update_iataCode(id=city_data["id"], iataCode=city_data["iataCode"])

iataCodes = []
for city_data in sheet_data:
    iataCodes.append(city_data["iataCode"])
cheapestFlights = flight_search.get_cheap_flights(iataCodes)

for sheet_flight, new_flight in zip(sheet_data, cheapestFlights):
    if new_flight != None and new_flight.price != "N/A":
        if sheet_flight["lowestPrice"] > new_flight.price:
            notification_manager.send_message(new_flight)


